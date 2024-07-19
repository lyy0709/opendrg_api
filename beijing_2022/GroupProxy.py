from enum import Enum
import os
import sys
import time
import re
from collections import namedtuple
from Grouper_beijing_2022 import Grouper_beijing_2022 as Grouper
from Base import Reader,MedicalRecord,DrgGroupStatus,GroupResult,tuple_to_str

class GroupProxy:
  def __init__(self,**kwargs):
    self.DEBUG=kwargs.get('DEBUG') if 'DEBUG' in kwargs else 0
    self.TRANS_CODE=kwargs.get('TRANS_CODE') if 'TRANS_CODE' in kwargs else 0
    self.load_data()
    self.grouper=Grouper(**kwargs)
    self.check_messages=[]
    
  def load_data(self):
    reader=Reader('ICD')
    self.ZD_INFO=reader.read('ZD_INFO').to_dict()
    self.SS_INFO=reader.read('SS_INFO').to_dict()
    self.ZD_MAP=reader.read('ZD_MAP').to_dict()
    self.SS_MAP=reader.read('SS_MAP').to_dict()

  def message(self,*args):
    message=' '.join(args)
    self.check_messages.append(message)

  def return_messages(self):
    result=self.check_messages.copy()
    self.check_messages.clear()
    return result

  def group_df(self,df,writer,cols=[]):
    if cols:
      df.index.name=MedicalRecord._fields[0]
      df.rename(columns=dict(zip(cols[1:],MedicalRecord._fields[1:])),inplace=True)
    df.fillna('',inplace=True)
    print('record count',len(df))
    t1=time.time()
    results=self.group_iter(df.itertuples())
    columns=list(df.columns)
    if cols:
      for x,y in zip(cols[1:],MedicalRecord._fields[1:]):
        columns[columns.index(y)]=x
      df.index.name=cols[0]
    writer.write('{},{},{}\n'.format(df.index.name,','.join(columns),','.join(GroupResult._fields)))
    while True:
        try:
          writer.write(tuple_to_str(next(results))+'\n')
        except StopIteration:
          break
    t2=time.time()
    print('group time',int((t2-t1)*1000))

  def group_iter(self,it):
    while True:
      try:
        record=next(it)
      except StopIteration:
        break
      yield record+self.group(record)

  def group(self,record):
    # 如果设置了TRANS_CODE，进行转换处理
    if self.TRANS_CODE:
        # 对记录进行转换
        trans_result = self.trans(record)
        # 如果转换结果是DrgGroupStatus类型，创建GroupResult对象
        if isinstance(trans_result, DrgGroupStatus):
            result = GroupResult(record.Index, trans_result.value, self.return_messages(), '0000', '00', '0000')
            # 如果开启了DEBUG模式，打印结果
            if self.DEBUG:
                print(result)
            return result
        # 如果不是DrgGroupStatus类型，更新record为转换结果
        record = trans_result
    else:
        # 如果没有设置TRANS_CODE，处理zdList字段，将其分割成列表
        record = record._replace(zdList=re.split(',|\|', record.zdList))
        # 如果ssList字段不为空，也进行分割处理
        if record.ssList:
            record = record._replace(ssList=re.split(',|\|', record.ssList))
        else:
            # 如果ssList字段为空，将其替换为空列表
            record = record._replace(ssList=[])
    # 对更新后的记录进行检查
    check_result = self.check(record)
    if check_result:
        # 如果检查有结果，创建GroupResult对象
        result = GroupResult(record.Index, check_result.value, self.return_messages(), '0000', '00', '0000')
    else:
        # 如果检查无结果，调用grouper的group方法进行分组
        result = self.grouper.group(record)
        group_messages = result.messages
        # 将返回的消息插入到分组结果的消息列表中
        for message in reversed(self.return_messages()):
            group_messages.insert(0, message)
    return result

  def trans(self,record):
    # zd_list=record.zdList.split(',')
    zd_list=re.split(',|\|',record.zdList)
    zd_no_map=[]
    for x in zd_list:
      if x in self.ZD_MAP:
        zd=self.ZD_MAP.get(x)
        if zd!=x:
          zd_list[zd_list.index(x)]=self.ZD_MAP.get(x)
          # self.message('{}->{}'.format(x,zd))
      else:
        zd_list[zd_list.index(x)]=''
        zd_no_map.append(x)
    if zd_list and zd_list[0]=='-':
      zd_no_map.append(record.zdList.partition(',')[0])
    if zd_no_map:
      self.message('诊断{}无法转换为分组器支持的编码'.format('、'.join(zd_no_map)))
      return DrgGroupStatus.ZD_NOT_MAPPING
    record=record._replace(zdList=[x for x in zd_list if x and x!='-'])
    if not record.ssList:
      record=record._replace(ssList=[])
      return record
    # ss_list=record.ssList.split(',')
    ss_list=re.split(',|\|',record.ssList)
    ss_no_map=[]
    for x in ss_list:
      if x in self.SS_MAP:
        ss=self.SS_MAP.get(x)
        if ss!=x:
          ss_list[ss_list.index(x)]=self.SS_MAP.get(x)
          # self.message('{}->{}'.format(x,ss))
      else:
        ss_list[ss_list.index(x)]=''
        ss_no_map.append(x)
    if ss_list and ss_list[0]=='-':
      ss_no_map.append(record.ssList.partition(',')[0])
    if ss_no_map:
      self.message('手术操作{}无法转换为分组器支持的编码'.format('、'.join(ss_no_map)))
      return DrgGroupStatus.SS_NOT_MAPPING
    record=record._replace(ssList=[x for x in ss_list if x and x!='-'])
    return record

  def check(self,record):
    try:
      if record.gender==None:
        self.message('病人性别为空')
        return DrgGroupStatus.CHECK_FAILED
      if not (record.gender in [1,'1','男'] or record.gender in [2,'2','女']):
        self.message('病人性别取值必须为1或2：{}'.format(record.gender))
        return DrgGroupStatus.CHECK_FAILED
      if record.age==None:
        self.message('病人年龄为空')
        return DrgGroupStatus.CHECK_FAILED
      if int(record.age)==0 and record.ageDay==None:
        self.message('病人年龄0时，年龄天数必须有值')
        return DrgGroupStatus.CHECK_FAILED
      if int(record.age)==0 and int(record.ageDay)<=28 and record.weight==None:
        self.message('新生儿的出生体重必须有值')
        return DrgGroupStatus.CHECK_FAILED
      if not record.zdList:
        self.message('诊断信息为空')
        return DrgGroupStatus.CHECK_FAILED
    except:
      self.message('病案信息解析出错')
      return DrgGroupStatus.CHECK_FAILED
    for x in record.zdList:
      self.message('{} {}'.format(x,self.ZD_INFO.get(x,'未知名称')))
    for x in record.ssList:
      self.message('{} {}'.format(x,self.SS_INFO.get(x,'未知名称')))
    return 

  def group_record(self,record_str):
    record=MedicalRecord(**dict(zip(MedicalRecord._fields,record_str.split(','))))
    return self.group(record)

  def group_txt(self):
    path=os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    lines=open(os.path.join(path,'input.txt')).read().splitlines()
    if len(lines)==0:
      print('input.txt文件无数据')
      sys.exit(-1)
    file=open(os.path.join(path,'output.txt'),'w')
    for line in lines[1:]:
      file.write(str(self.group_record(line))+'\n')

  def group_csv(self,filename,cols):
    filename=filename.replace('.csv','_python_result.csv')
    import pandas as pd
    df=pd.read_csv(filename,index_col=cols[0])
    self.group_df(df,open(filename,'w',encoding='utf-8-sig'),cols)

if __name__ == "__main__":
  grouper=GroupProxy()
  record=MedicalRecord(Index='1653890', age=10, ageDay=21, weight=3200, gender='2', dept='28',inHospitalTime=14,leavingType='1',
  zdList='S06.500,I21.900x011,I62.001,G93.501,S06.202,I63.908,S02.900x002,J98.414,J96.000,J81.x00x002', 
  ssList='96.7201,01.2400x005,03.3100x001,33.2403,31.1x00x005,38.9301,38.9303')
  print(record)
  result=grouper.group(record)
  print(result)