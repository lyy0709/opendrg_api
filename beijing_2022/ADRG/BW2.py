from Base import message,intersect,SS_VALID
from DRG import MDCB_DRG

def group(record):
  adrg_zd=["G80.000","G80.000x011","G80.000x021","G80.100","G80.101","G80.200","G80.200x001","G80.300","G80.300x003","G80.301","G80.302","G80.303","G80.305","G80.400","G80.800","G80.801","G80.802","G80.900","G81.000","G81.100","G81.900","G81.900x002","G81.901","G81.902","G81.903"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合BW2入组条件，匹配规则：主诊断匹配')
    
    if MDCB_DRG.BW21_group(record):
      return 'BW21'

    if MDCB_DRG.BW25_group(record):
      return 'BW25'

    return 'BW2'
  else:
    return ''

