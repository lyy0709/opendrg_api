from flask import Flask, request, jsonify
from enum import Enum
import os
import re
import time
from collections import namedtuple
from Grouper_beijing_2022 import Grouper_beijing_2022 as Grouper
from Base import Reader, MedicalRecord, DrgGroupStatus, GroupResult, tuple_to_str

app = Flask(__name__)

class GroupProxy:
    def __init__(self, **kwargs):
        self.DEBUG = kwargs.get('DEBUG') if 'DEBUG' in kwargs else 0
        self.TRANS_CODE = kwargs.get('TRANS_CODE') if 'TRANS_CODE' in kwargs else 0
        self.load_data()
        self.grouper = Grouper(**kwargs)
        self.check_messages = []

    def load_data(self):
        reader = Reader('ICD')
        self.ZD_INFO = reader.read('ZD_INFO').to_dict()
        self.SS_INFO = reader.read('SS_INFO').to_dict()
        self.ZD_MAP = reader.read('ZD_MAP').to_dict()
        self.SS_MAP = reader.read('SS_MAP').to_dict()

    def message(self, *args):
        message = ' '.join(args)
        self.check_messages.append(message)

    def return_messages(self):
        result = self.check_messages.copy()
        self.check_messages.clear()
        return result

    def group(self, record):
        if self.TRANS_CODE:
            trans_result = self.trans(record)
            if isinstance(trans_result, DrgGroupStatus):
                result = GroupResult(record.Index, trans_result.value, self.return_messages(), '0000', '00', '0000')
                if self.DEBUG:
                    print(result)
                return result
            record = trans_result
        else:
            record = record._replace(zdList=re.split(',|\|', record.zdList))
            if record.ssList:
                record = record._replace(ssList=re.split(',|\|', record.ssList))
            else:
                record = record._replace(ssList=[])
        check_result = self.check(record)
        if check_result:
            result = GroupResult(record.Index, check_result.value, self.return_messages(), '0000', '00', '0000')
        else:
            result = self.grouper.group(record)
            group_messages = result.messages
            for message in reversed(self.return_messages()):
                group_messages.insert(0, message)
        return result

    def trans(self, record):
        zd_list = re.split(',|\|', record.zdList)
        zd_no_map = []
        for x in zd_list:
            if x in self.ZD_MAP:
                zd = self.ZD_MAP.get(x)
                if zd != x:
                    zd_list[zd_list.index(x)] = self.ZD_MAP.get(x)
            else:
                zd_list[zd_list.index(x)] = ''
                zd_no_map.append(x)
        if zd_list and zd_list[0] == '-':
            zd_no_map.append(record.zdList.partition(',')[0])
        if zd_no_map:
            self.message('诊断{}无法转换为分组器支持的编码'.format('、'.join(zd_no_map)))
            return DrgGroupStatus.ZD_NOT_MAPPING
        record = record._replace(zdList=[x for x in zd_list if x and x != '-'])
        if not record.ssList:
            record = record._replace(ssList=[])
            return record
        ss_list = re.split(',|\|', record.ssList)
        ss_no_map = []
        for x in ss_list:
            if x in self.SS_MAP:
                ss = self.SS_MAP.get(x)
                if ss != x:
                    ss_list[ss_list.index(x)] = self.SS_MAP.get(x)
            else:
                ss_list[ss_list.index(x)] = ''
                ss_no_map.append(x)
        if ss_list and ss_list[0] == '-':
            ss_no_map.append(record.ssList.partition(',')[0])
        if ss_no_map:
            self.message('手术操作{}无法转换为分组器支持的编码'.format('、'.join(ss_no_map)))
            return DrgGroupStatus.SS_NOT_MAPPING
        record = record._replace(ssList=[x for x in ss_list if x and x != '-'])
        return record

    def check(self, record):
        try:
            if record.gender == None:
                self.message('病人性别为空')
                return DrgGroupStatus.CHECK_FAILED
            if not (record.gender in [1, '1', '男'] or record.gender in [2, '2', '女']):
                self.message('病人性别取值必须为1或2：{}'.format(record.gender))
                return DrgGroupStatus.CHECK_FAILED
            if record.age == None:
                self.message('病人年龄为空')
                return DrgGroupStatus.CHECK_FAILED
            if int(record.age) == 0 and record.ageDay == None:
                self.message('病人年龄0时，年龄天数必须有值')
                return DrgGroupStatus.CHECK_FAILED
            if int(record.age) == 0 and int(record.ageDay) <= 28 and record.weight == None:
                self.message('新生儿的出生体重必须有值')
                return DrgGroupStatus.CHECK_FAILED
            if not record.zdList:
                self.message('诊断信息为空')
                return DrgGroupStatus.CHECK_FAILED
        except:
            self.message('病案信息解析出错')
            return DrgGroupStatus.CHECK_FAILED
        for x in record.zdList:
            self.message('{} {}'.format(x, self.ZD_INFO.get(x, '未知名称')))
        for x in record.ssList:
            self.message('{} {}'.format(x, self.SS_INFO.get(x, '未知名称')))
        return
    
def contains_chinese(string):
    """检查字符串中是否包含中文字符"""
    for ch in string:
        if '\u4e00' <= ch <= '\u9fff':
            return True
    return False

def convert_chinese_to_code(data, zd_info, ss_info):
    def convert(item, info_dict, errors, error_key):
        if not contains_chinese(item):
            return item
        codes = []
        for part in item.split(','):
            code = None
            for k, v in info_dict.items():
                if v == part:
                    code = k
                    break
            if code:
                codes.append(code)
            else:
                codes.append(part)  # If no match is found, keep original
                if part not in info_dict.values():
                    errors[error_key].append(part)
        return '|'.join(codes)

    errors = {'zd_errors': [], 'ss_errors': []}
    data['main_zd'] = convert(data['main_zd'], zd_info, errors, 'zd_errors')
    data['other_zd'] = convert(data.get('other_zd', ''), zd_info, errors, 'zd_errors')
    data['main_ss'] = convert(data.get('main_ss', ''), ss_info, errors, 'ss_errors')
    data['other_ss'] = convert(data.get('other_ss', ''), ss_info, errors, 'ss_errors')
    return data, errors

@app.route('/api/group', methods=['POST'])
def group_record():
    data = request.json
    required_fields = ['main_zd', 'gender', 'age', 'weight']
    errors = []

    for field in required_fields:
        if field not in data:
            errors.append(f'Missing required field: {field}')
    
    if errors:
        return jsonify({'errors': errors}), 400

    grouper = GroupProxy()
    data, convert_errors = convert_chinese_to_code(data, grouper.ZD_INFO, grouper.SS_INFO)

    errors.extend([f'zd_errors: {err}' for err in convert_errors['zd_errors'] if err])
    errors.extend([f'ss_errors: {err}' for err in convert_errors['ss_errors'] if err])

    # 检查age是否大于等于0
    if data['age'] < 0:
        errors.append('Age cannot be less than 0')

    # 如果age大于0小于1，确保age_days存在且大于0
    if 0 < data['age'] < 1:
        if 'age_days' not in data or data['age_days'] <= 0:
            errors.append('For ages between 0 and 1 year, age_days must be greater than 0')

    # 如果age_days存在，确保其不小于0
    if 'age_days' in data and data['age_days'] < 0:
        errors.append('age_days cannot be less than 0')
    
    record = MedicalRecord(
        Index='1',  # Dummy value for Index
        age=data['age'],
        ageDay=data.get('age_days', 0),
        weight=data['weight'],
        gender=data['gender'],
        dept=data.get('dept', 'N/A'),
        inHospitalTime=data.get('inHospitalTime', 0),
        leavingType=data.get('leavingType', 'N/A'),
        zdList=data['main_zd'] + '|' + data.get('other_zd', ''),
        ssList=data.get('main_ss', '') + '|' + data.get('other_ss', '')
    )
    
    result = grouper.group(record)
    
    # 提取有效字段并添加错误信息
    response = {
        'status': result.status,
        'mdc': result.mdc,
        'adrg': result.adrg,
        'drg': result.drg,
        'errors': errors
    }
    
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')
