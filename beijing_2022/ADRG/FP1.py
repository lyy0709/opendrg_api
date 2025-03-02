from Base import message,intersect,SS_VALID
from DRG import MDCF_DRG

def group(record):
  adrg_zd=["I11.001","I11.002","I13.000x001","I13.200x001","I50.000","I50.000x005","I50.000x006","I50.001","I50.002","I50.100","I50.100x006","I50.101","I50.102","I50.103","I50.104","I50.105","I50.900","I50.900x001","I50.900x002","I50.900x007","I50.900x008","I50.900x009","I50.900x010","I50.900x014","I50.900x015","I50.900x016","I50.900x017","I50.900x018","I50.900x019","I50.907","I50.908","R57.000","R57.100","R57.101","R57.200","R57.800x003","R57.801","R57.802","R57.803","R57.900","R57.900x002","R57.901"]
  adrg_zd1=[]
  adrg_ss=["37.6101","37.6600x001","37.6800x001","37.6800x002","37.6800x003","37.6800x004","37.6800x005","39.9500x004","39.9500x005","39.9500x006","39.9500x007","39.9501","39.9600x002","39.9600x003","96.7101"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合FP1入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    if MDCF_DRG.FP11_group(record):
      return 'FP11'

    if MDCF_DRG.FP15_group(record):
      return 'FP15'

    return 'FP1'
  else:
    return ''

