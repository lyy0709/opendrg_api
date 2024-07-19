from Base import message,intersect,SS_VALID
from DRG import MDCW_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in SS_VALID:
    message('符合WJ1入组条件，匹配规则：存在手术')
    
    if MDCW_DRG.WJ11_group(record):
      return 'WJ11'

    if MDCW_DRG.WJ15_group(record):
      return 'WJ15'

    return 'WJ1'
  else:
    return ''

