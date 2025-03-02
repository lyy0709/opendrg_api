from Base import message,intersect,SS_VALID
from DRG import MDCG_DRG

def group(record):
  adrg_zd=["C18.100","K35.200","K35.201","K35.300","K35.301"]
  adrg_zd1=[]
  adrg_ss=["47.0100","47.0901","47.0902","47.0903","47.1100","47.2x00","47.2x01","47.9100","47.9200","47.9901"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合GD1入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    if MDCG_DRG.GD19_group(record):
      return 'GD19'

    return 'GD1'
  else:
    return ''

