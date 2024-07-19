from Base import message,intersect,SS_VALID
from DRG import MDCA_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["41.0000","41.0200","41.0300","41.0500","41.0600","41.0800x001"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合AG1入组条件，匹配规则：主手术匹配')
    
    if MDCA_DRG.AG11_group(record):
      return 'AG11'

    if MDCA_DRG.AG15_group(record):
      return 'AG15'

    return 'AG1'
  else:
    return ''

