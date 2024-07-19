from Base import message,intersect,SS_VALID
from DRG import MDCR_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["92.2200","92.2201","92.2300","92.2301","92.2302","92.2303","92.2400","92.2400x002","92.2400x003","92.2400x004","92.2400x005","92.2400x006","92.2400x007","92.2500","92.2501","92.2601","92.2602","92.2900x001","92.3100","92.3101","92.3102","92.3200","92.3200x001","92.3201","92.3202","92.3300","92.3900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合RC1入组条件，匹配规则：主手术匹配')
    
    if MDCR_DRG.RC12_group(record):
      return 'RC12'

    if MDCR_DRG.RC14_group(record):
      return 'RC14'

    if MDCR_DRG.RC16_group(record):
      return 'RC16'

    if MDCR_DRG.RC18_group(record):
      return 'RC18'

    return 'RC1'
  else:
    return ''

