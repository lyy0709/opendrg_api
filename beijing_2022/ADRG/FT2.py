from Base import message,intersect,SS_VALID
from DRG import MDCF_DRG

def group(record):
  adrg_zd=["A18.820+I39.8*","A18.821+I41.0*","A32.802+I39.8*","A39.500","A39.502+I39.8*","A39.504+I52.0*","A52.000+I98.0*","A52.006+I39.8*","A54.802+I39.8*","B33.200x002+I39.8*","B37.600+I39.8*","I01.100","I33.000x001","I33.000x004","I33.000x006","I33.000x007","I33.000x008","I33.000x011","I33.000x012","I33.000x019","I33.000x020","I33.000x021","I33.000x022","I33.000x024","I33.001","I33.002","I33.003","I33.004","I33.005","I33.006","I33.007","I33.900","T82.703"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合FT2入组条件，匹配规则：主诊断匹配')
    
    if MDCF_DRG.FT29_group(record):
      return 'FT29'

    return 'FT2'
  else:
    return ''

