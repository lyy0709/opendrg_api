from Base import message,intersect,SS_VALID
from DRG import MDCG_DRG

def group(record):
  adrg_zd=["I85.000x001","I86.401","I86.800x014","I86.812","K22.804","K55.800x003","K55.900x004","K91.800x102","K91.800x103","K91.800x106","K91.800x501","K92.000","K92.100x001","K92.200x001","K92.200x005","K92.201","K92.202","K92.203","K92.204","K92.205","K92.206","K92.207","K92.208","K92.209","K92.210","K92.800x001","K92.800x002","K92.800x003","K92.800x004","K92.800x005","K92.800x007","K92.800x011","R19.501"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合GS1入组条件，匹配规则：主诊断匹配')
    
    if MDCG_DRG.GS11_group(record):
      return 'GS11'

    if MDCG_DRG.GS15_group(record):
      return 'GS15'

    return 'GS1'
  else:
    return ''

