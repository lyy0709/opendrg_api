from Base import message,intersect,SS_VALID
from DRG import MDCM_DRG

def group(record):
  adrg_zd=["C60.000","C60.100","C60.200","C60.201","C60.800","C60.900","C60.901","C61.x00","C62.000","C62.001","C62.100","C62.900","C62.901","C63.000","C63.100","C63.200","C63.201","C63.700","C63.701","C63.702","C63.800","C63.801","C63.900","C79.800x228","C79.800x231","C79.800x233","C79.815","C79.816","C79.817","C79.818","C79.819","C79.820","D07.400","D07.401","D07.402","D07.500","D07.601","D07.602","D07.603","D40.000x001","D40.001","D40.100x002","D40.101","D40.700x001","D40.700x002","D40.700x003","D40.701","D40.702","D40.703","D40.704","D40.900x001","D40.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合MR1入组条件，匹配规则：主诊断匹配')
    
    if MDCM_DRG.MR13_group(record):
      return 'MR13'

    if MDCM_DRG.MR15_group(record):
      return 'MR15'

    return 'MR1'
  else:
    return ''

