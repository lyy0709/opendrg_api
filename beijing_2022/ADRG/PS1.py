from Base import message,intersect,SS_VALID
from DRG import MDCP_DRG

def group(record):
  adrg_zd=["P07.200","P07.200x011","P07.200x021","P07.300","P07.300x001","P07.300x011","P07.300x021"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and intersect(record.zdList,adrg_zd) and record.weight and record.weight<1500 and record.ageDay!=None and record.ageDay<=28:
    message('符合PS1入组条件，匹配规则：某一诊断匹配、体重小于1500克、新生儿')
    
    if MDCP_DRG.PS19_group(record):
      return 'PS19'

    return 'PS1'
  else:
    return ''

