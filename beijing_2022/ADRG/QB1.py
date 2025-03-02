from Base import message,intersect,SS_VALID
from DRG import MDCQ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.6601","39.1x07","41.2x01","41.2x02","41.2x03","41.2x04","41.4100","41.4200x002","41.4200x003","41.4300","41.4301","41.5x00","41.5x01","41.9300","41.9301","41.9400","41.9500x001","41.9501","41.9502","41.9503","41.9504","41.9901"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合QB1入组条件，匹配规则：主手术匹配')
    
    if MDCQ_DRG.QB19_group(record):
      return 'QB19'

    return 'QB1'
  else:
    return ''

