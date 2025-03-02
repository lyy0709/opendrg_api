from Base import message,intersect,SS_VALID
from DRG import MDCR_DRG

def group(record):
  adrg_zd=["C90.000","C90.000x004","C90.000x005","C90.000x008+M90.6*","C90.000x009","C90.000x011","C90.000x012","C90.000x014","C90.000x021","C90.000x022","C90.000x023","C90.000x024","C90.000x025","C90.000x026","C90.000x027","C90.000x028","C90.000x029","C90.000x030","C90.000x031","C90.000x032","C90.000x033","C90.000x034","C90.000x035","C90.000x036","C90.000x037","C90.000x038","C90.000x039","C90.000x040","C90.000x041","C90.001","C90.002","C90.100","C90.100x002","C90.100x011","C90.200","C90.200x008","C90.200x009","C90.200x013","C90.300","C90.300x001","C90.300x002","C90.300x003","C90.300x004","C90.301","C90.302","C90.303","D89.801"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合RS2入组条件，匹配规则：主诊断匹配')
    
    if MDCR_DRG.RS23_group(record):
      return 'RS23'

    if MDCR_DRG.RS25_group(record):
      return 'RS25'

    return 'RS2'
  else:
    return ''

