from Base import message,intersect,SS_VALID
from DRG import MDCQ_DRG

def group(record):
  adrg_zd=["D46.000","D46.000x002","D46.000x003","D62.x00","D64.000","D64.001","D64.100","D64.200","D64.300","D64.300x002","D64.400x001","D64.401","D64.800x002","D64.801","D64.802","D64.803","D64.900","D64.900x006","D64.900x007","D64.901","D64.902","D64.903","D64.904","E80.000","E80.000x004","E80.001","E80.002","E80.003","E80.100","E80.100x002","E80.200x001","E80.200x004","E80.200x005","E80.200x007","E80.200x008","E80.201","E80.202","E80.203","N18.300x001+D63.8*","N18.400x001+D63.8*","N18.500x001+D63.8*","N18.900x012+D63.8*"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合QS4入组条件，匹配规则：主诊断匹配')
    
    if MDCQ_DRG.QS41_group(record):
      return 'QS41'

    if MDCQ_DRG.QS45_group(record):
      return 'QS45'

    return 'QS4'
  else:
    return ''

