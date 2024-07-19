from Base import message,intersect,SS_VALID
from DRG import MDCR_DRG

def group(record):
  adrg_zd=["Z51.101","Z51.102","Z51.103","Z51.104"]
  adrg_zd1=[]
  adrg_ss=["03.8x01","54.9701","54.9702","54.9703","99.2500x036","99.2500x037","99.2500x038","99.2500x039","99.2502","99.2503","99.2504","99.2505","99.2506","99.2800x006","99.2801"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合RE1入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    if MDCR_DRG.RE12_group(record):
      return 'RE12'

    if MDCR_DRG.RE14_group(record):
      return 'RE14'

    if MDCR_DRG.RE16_group(record):
      return 'RE16'

    return 'RE1'
  else:
    return ''

