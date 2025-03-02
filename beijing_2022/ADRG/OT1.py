from Base import message,intersect,SS_VALID
from DRG import MDCO_DRG

def group(record):
  adrg_zd=["O00.000","O00.001","O00.100","O00.101","O00.102","O00.103","O00.104","O00.105","O00.106","O00.107","O00.108","O00.109","O00.110","O00.111","O00.112","O00.113","O00.114","O00.115","O00.116","O00.117","O00.200","O00.201","O00.800x006","O00.801","O00.802","O00.803","O00.804","O00.805","O00.807","O00.808","O00.809","O00.900","O00.901","O00.902","O08.006","O08.100x003","O08.104","O08.105","O08.106","O08.200x002","O08.302","O08.400x004","O08.600x005","O08.800x006","O08.806"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合OT1入组条件，匹配规则：主诊断匹配')
    
    if MDCO_DRG.OT19_group(record):
      return 'OT19'

    return 'OT1'
  else:
    return ''

