from Base import message,intersect,SS_VALID
from DRG import MDCG_DRG

def group(record):
  adrg_zd=["K25.100x001","K25.200x001","K25.500x001","K25.501","K25.600","K26.100","K26.200x001","K26.200x002","K26.500x001","K26.501","K26.600","K27.100x001","K27.200","K27.500","K27.500x001","K27.500x002","K27.500x005","K27.501","K27.502","K27.503","K27.600","K27.600x001","K28.100","K28.200","K28.500","K28.500x001","K28.600","K28.600x001","K28.900x002","K63.103","K63.104","K63.105"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合GU1入组条件，匹配规则：主诊断匹配')
    
    if MDCG_DRG.GU13_group(record):
      return 'GU13'

    if MDCG_DRG.GU15_group(record):
      return 'GU15'

    return 'GU1'
  else:
    return ''

