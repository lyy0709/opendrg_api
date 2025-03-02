from Base import message,intersect,SS_VALID
from DRG import MDCT_DRG

def group(record):
  adrg_zd=["F04.x00x001","F04.x00x901","F05.000","F05.000x001","F05.001","F05.100","F05.101","F05.801","F05.802","F05.900","F05.901","F05.902","F06.000","F06.100","F06.200","F06.300","F06.300x002","F06.300x010","F06.300x020","F06.300x021","F06.300x030","F06.301","F06.302","F06.400","F06.400x003","F06.500","F06.600","F06.700","F06.800","F06.800x002","F06.800x003","F06.800x004","F06.800x005","F06.800x006","F06.800x007","F06.800x008","F06.800x009","F06.800x010","F06.800x011","F06.800x012","F06.800x013","F06.800x014","F06.800x015","F06.800x016","F06.800x017","F06.800x018","F06.800x019","F06.800x020","F06.800x021","F06.800x023","F06.800x024","F06.800x025","F06.800x026","F06.800x027","F06.800x032","F06.800x033","F06.800x034","F06.800x037","F06.800x038","F06.800x039","F06.800x040","F06.800x041","F06.800x042","F06.800x043","F06.800x044","F06.800x045","F06.800x046","F06.800x047","F06.800x048","F06.800x049","F06.800x050","F06.801","F06.802","F06.803","F06.804","F06.805","F06.806","F06.807","F06.808","F06.809","F06.810","F06.811","F06.900","F07.000","F07.001","F07.100","F07.200","F07.201","F07.800x001","F07.800x002","F07.800x003","F07.900","F07.900x001","F07.901","F09.x00x003","F09.x00x004","F09.x01","F09.x02","F09.x03","F53.800","F99.x00","Q91.300","R41.801","R48.800x005","R48.801","R68.803"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合TW1入组条件，匹配规则：主诊断匹配')
    
    if MDCT_DRG.TW19_group(record):
      return 'TW19'

    return 'TW1'
  else:
    return ''

