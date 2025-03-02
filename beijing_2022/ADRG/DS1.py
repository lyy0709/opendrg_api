from Base import message,intersect,SS_VALID
from DRG import MDCD_DRG

def group(record):
  adrg_zd=["H81.000","H81.100","H81.101","H81.200","H81.301","H81.302","H81.303","H81.400","H81.400x003","H81.800","H81.900","H81.901","H81.902","H83.000","H83.000x001","H83.000x002","H83.100","H83.101","H83.200","H83.200x001","H83.200x002","H83.200x003","H83.300x001","H83.301","H83.302","H83.800x002","H83.800x003","H83.800x004","H83.801","H90.000","H90.100","H90.200","H90.300","H90.400","H90.500","H90.501","H90.502","H90.600","H90.700","H90.801","H91.000","H91.001","H91.100","H91.200","H91.200x001","H91.300x001","H91.801","H91.900","H91.900x002","H91.900x004","H91.901","H93.001","H93.100","H93.101","H93.102","H93.103","H93.200x002","H93.200x005","H93.201"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合DS1入组条件，匹配规则：主诊断匹配')
    
    if MDCD_DRG.DS13_group(record):
      return 'DS13'

    if MDCD_DRG.DS15_group(record):
      return 'DS15'

    return 'DS1'
  else:
    return ''

