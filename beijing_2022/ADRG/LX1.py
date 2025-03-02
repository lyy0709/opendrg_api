from Base import message,intersect,SS_VALID
from DRG import MDCL_DRG

def group(record):
  adrg_zd=["M10.005+N22.8*","N13.000","N13.100x001","N13.201","N13.202","N13.203","N13.204","N13.300x005","N13.301","N13.302","N13.400","N13.500x010","N13.501","N13.502","N13.503","N13.504","N13.506","N13.901","N20.000","N20.000x001","N20.000x002","N20.000x003","N20.001","N20.002","N20.100","N20.200x001","N20.900","N20.900x001","N20.901","N21.000","N21.001","N21.100","N21.800","N21.900","N32.000","N32.001","N32.002","N35.000","N35.000x001","N35.100x001","N35.800","N35.900","N35.901","N99.100","N99.100x003","N99.100x005","N99.101","N99.805","N99.806","Q62.100","Q62.100x802","Q62.100x902","Q62.101","Q62.103","Q62.104","Q62.300x902","Q62.300x903","Q62.300x904","Q62.300x905"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合LX1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LX13_group(record):
      return 'LX13'

    if MDCL_DRG.LX15_group(record):
      return 'LX15'

    return 'LX1'
  else:
    return ''

