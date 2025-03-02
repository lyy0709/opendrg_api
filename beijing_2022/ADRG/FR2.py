from Base import message,intersect,SS_VALID
from DRG import MDCF_DRG

def group(record):
  adrg_zd=["I11.001","I11.002","I13.000x001","I13.200x001","I50.000","I50.000x005","I50.000x006","I50.001","I50.002","I50.100","I50.100x006","I50.101","I50.102","I50.103","I50.104","I50.105","I50.900","I50.900x001","I50.900x002","I50.900x007","I50.900x008","I50.900x009","I50.900x010","I50.900x014","I50.900x015","I50.900x016","I50.900x017","I50.900x018","I50.900x019","I50.907","I50.908","I97.100x004","I97.101","I97.102","I97.803","R57.000","R57.100","R57.101","R57.200","R57.800x003","R57.801","R57.802","R57.803","R57.900","R57.900x002","R57.901","T81.800x010"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合FR2入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FR21_group(record):
      return 'FR21'

    if MDCF_DRG.FR25_group(record):
      return 'FR25'

    return 'FR2'
  else:
    return ''

