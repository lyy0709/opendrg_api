from Base import message,intersect,SS_VALID  # 从Base模块导入message函数、intersect函数和SS_VALID变量
from ADRG import AA1,AB1,AC1,AD1,AE1,AF1,AG1,AG2,AH1_1,AH1_2,AH1_3  # 从ADRG模块导入各ADRG规则对象

def group(record):  # 定义group函数，用于根据记录分组
  mdc_zd=[]  # 初始化mdc_zd列表，用于存储某些数据，但在此代码中未使用
  dept_list=[]  # 初始化dept_list列表，用于存储某些数据，但在此代码中未使用
  if not (True and record.ssList and record.ssList[0] in SS_VALID):  # 如果记录的ssList为空或ssList的第一个元素不在SS_VALID中，则返回空字符串
    return ''
  
  message('符合MDCA入组条件，匹配规则：存在手术')  # 调用message函数，输出符合MDCA入组条件的信息

  # 以下部分依次调用AA1至AH1_3的group函数，尝试对记录进行分组
  result=AA1.group(record)
  if result:
    return result
  result=AB1.group(record)
  if result:
    return result
  result=AC1.group(record)
  if result:
    return result
  result=AD1.group(record)
  if result:
    return result
  result=AE1.group(record)
  if result:
    return result
  result=AF1.group(record)
  if result:
    return result
  result=AG1.group(record)
  if result:
    return result
  result=AG2.group(record)
  if result:
    return result
  result=AH1_1.group(record)
  if result:
    return result
  result=AH1_2.group(record)
  if result:
    return result
  result=AH1_3.group(record)
  if result:
    return result

  # 如果代码执行到这里，说明没有任何ADRG规则匹配，检查是否符合AQY入组条件
  if False and record.ssList and intersect(SS_VALID,record.ssList):  # 此条件永远不成立，因为以False开始
    message('符合AQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))  # 如果条件成立，输出符合AQY入组条件的信息
    return 'AQY'

  message('不符合MDCA的ADRG入组条件')  # 如果所有条件都不满足，输出不符合MDCA的ADRG入组条件的信息