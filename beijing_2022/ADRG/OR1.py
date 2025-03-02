from Base import message,intersect,SS_VALID
from DRG import MDCO_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=["Z37.000","Z37.000x001","Z37.001","Z37.002","Z37.100","Z37.100x002","Z37.200","Z37.200x003","Z37.201","Z37.202","Z37.203","Z37.204","Z37.300","Z37.300x001","Z37.301","Z37.302","Z37.303","Z37.400","Z37.400x001","Z37.500","Z37.500x001","Z37.501","Z37.502","Z37.600","Z37.600x001","Z37.700","Z37.700x001","Z37.900","Z37.900x003"]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and intersect(record.zdList[1:],adrg_zd1):
    message('符合OR1入组条件，匹配规则：其他诊断匹配')
    
    if MDCO_DRG.OR19_group(record):
      return 'OR19'

    return 'OR1'
  else:
    return ''

