from Base import message,intersect,SS_VALID
from DRG import MDCK_DRG

def group(record):
  adrg_zd=["C48.000x002","C73.x00","C73.x00x003","C74.000","C74.100","C74.900","C75.000","C75.100","C75.800","C75.900","C79.700","C79.800x839","C79.805","C79.825","D09.300","D09.301","D09.302","D09.303","D09.304","D17.700x029","D18.000x810","D18.000x839","D34.x00","D34.x00x003","D34.x00x005","D34.x01","D35.000","D35.001","D35.100","D35.100x002","D35.200","D35.200x004","D35.200x007","D35.200x008","D35.200x009","D35.200x010","D35.200x011","D35.601","D35.800","D35.900","D44.000x001","D44.001","D44.100x001","D44.101","D44.200x001","D44.201","D44.300x001","D44.301","D44.800x002","D44.801","D44.802","D44.900x001","D44.901"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合KR1入组条件，匹配规则：主诊断匹配')
    
    if MDCK_DRG.KR13_group(record):
      return 'KR13'

    if MDCK_DRG.KR15_group(record):
      return 'KR15'

    return 'KR1'
  else:
    return ''

