from Base import message,intersect,SS_VALID
from DRG import MDCD_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["20.9500","20.9501","20.9502","20.9601","20.9602","20.9701","20.9702","20.9801","20.9802"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合DB2入组条件，匹配规则：主手术匹配')
    
    if MDCD_DRG.DB29_group(record):
      return 'DB29'

    return 'DB2'
  else:
    return ''

