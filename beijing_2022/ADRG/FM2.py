from Base import message,intersect,SS_VALID
from DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.0200x001","00.6600x004","00.6601","17.5500x002","17.5500x003","17.5500x004","17.5501","36.0400","36.3400","36.9900x011","36.9900x012","37.2800","37.3400x001","37.3400x002","37.3500x004","37.4900x008","37.4900x017","37.4900x018","37.6101","37.7800","37.9200x001","37.9900x002","37.9900x003","39.4900x012"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FM2入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FM29_group(record):
      return 'FM29'

    return 'FM2'
  else:
    return ''

