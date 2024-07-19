from Base import message,intersect,SS_VALID
from DRG import MDCX_DRG

def group(record):
  adrg_zd=["B90.902","R10.200x001","R10.201","R13.x00","R41.100","R41.200","R47.000x001","R47.000x005","R47.000x006","R47.000x008","R47.001","R47.002","R47.003","R47.004","R47.100x001","R47.100x002","R47.101","R47.801","R47.802","R49.800x003","R49.801","R53.x00x001","R53.x00x003","R53.x00x004","R62.000x002","R62.000x003","R62.801","R62.802","R62.803","R62.900","Z50.000","Z50.600","Z54.800x010"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合XR3入组条件，匹配规则：主诊断匹配')
    
    if MDCX_DRG.XR31_group(record):
      return 'XR31'

    if MDCX_DRG.XR33_group(record):
      return 'XR33'

    if MDCX_DRG.XR35_group(record):
      return 'XR35'

    return 'XR3'
  else:
    return ''

