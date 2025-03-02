from Base import message,intersect,SS_VALID
from DRG import MDCE_DRG

def group(record):
  adrg_zd=["I26.900x001","I26.900x002","I26.900x003","I26.900x005","I26.900x006","I26.900x007","I26.900x008","I26.900x009","I26.900x010","I26.900x011","I26.900x012","I26.900x013","I26.900x015","I26.900x016","I26.900x017","I26.900x018","I26.901","I26.902","I28.800x010"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合ER2入组条件，匹配规则：主诊断匹配')
    
    if MDCE_DRG.ER21_group(record):
      return 'ER21'

    if MDCE_DRG.ER25_group(record):
      return 'ER25'

    return 'ER2'
  else:
    return ''

