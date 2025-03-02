from Base import message,intersect,SS_VALID
from DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.2400x001","00.5601","00.5602","00.5700","00.5900x003","00.5901","00.5902","37.2000","37.2000x003","37.2100","37.2200","37.2300","37.2600x001","37.2700","37.2901","38.2400","38.2601","38.2602","88.5000","88.5201","88.5202","88.5301","88.5302","88.5400x001","88.5500","88.5500x002","88.5600","88.5600x002","88.5700x003","88.5701","88.5800","88.5900"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FM3入组条件，匹配规则：主手术匹配')
    
    if MDCF_DRG.FM31_group(record):
      return 'FM31'

    if MDCF_DRG.FM35_group(record):
      return 'FM35'

    return 'FM3'
  else:
    return ''

