from Base import message,intersect,SS_VALID
from DRG import MDCG_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["45.4200x003","45.4201","45.4300x008","45.4300x013","45.4301","45.4302","45.4303","45.4304","45.4305","45.4306","45.4307","46.3200x002","46.3201","46.8500x008","46.8500x009","46.8502","46.8504","46.8505","46.8506","46.8507","46.8508","46.8509","46.8511","46.8600","46.8600x001","46.9501","46.9600x001","46.9601","46.9602","47.0900x001","47.9900x002","48.3301","48.3600x001","48.3600x002","48.3600x004","48.3600x005","48.9900x005","49.3101","97.5201","97.5900x001","97.5900x003","98.0303","98.0400x002","98.0401"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合GK3入组条件，匹配规则：主手术匹配')
    
    if MDCG_DRG.GK33_group(record):
      return 'GK33'

    if MDCG_DRG.GK35_group(record):
      return 'GK35'

    return 'GK3'
  else:
    return ''

