from Base import message,intersect,SS_VALID
from DRG import MDCN_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["68.1601","68.2100x002","68.2101","68.2201","68.2202","68.2204","68.2206","68.2300","68.2300x005","68.2301","68.2302","68.2900x013","68.2900x028","68.2900x031","68.2900x035","68.2900x037","68.2900x038","68.2900x048","68.2901","68.2902","68.2903","68.2904","68.2905","68.2906","68.2907","68.2909","68.2910","68.2911","68.2912","68.2913","68.2914","68.2915","68.2916","68.2917","68.2918","69.7x00","98.1600x001","98.1600x002"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合NE1入组条件，匹配规则：主手术匹配')
    
    if MDCN_DRG.NE19_group(record):
      return 'NE19'

    return 'NE1'
  else:
    return ''

