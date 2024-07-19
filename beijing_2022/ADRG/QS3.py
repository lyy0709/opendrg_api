from Base import message,intersect,SS_VALID
from DRG import MDCQ_DRG

def group(record):
  adrg_zd=["D60.000x001","D60.100x001","D60.800","D60.900x001","D61.000","D61.000x006","D61.001","D61.002","D61.003","D61.004","D61.005","D61.006","D61.007","D61.101","D61.102","D61.200x002","D61.201","D61.202","D61.300","D61.800x002","D61.801","D61.802","D61.900","D61.900x001","D61.901","D61.902","D61.903","D61.904","D61.905","D61.906","D61.907","D61.908","D61.909"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合QS3入组条件，匹配规则：主诊断匹配')
    
    if MDCQ_DRG.QS31_group(record):
      return 'QS31'

    if MDCQ_DRG.QS35_group(record):
      return 'QS35'

    return 'QS3'
  else:
    return ''

