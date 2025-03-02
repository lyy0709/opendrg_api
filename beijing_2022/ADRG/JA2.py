from Base import message,intersect,SS_VALID
from DRG import MDCJ_DRG

def group(record):
  adrg_zd=["D05.000","C50.900","C50.902","C50.900x005","C50.001","D05.100","C50.803","D03.501","C50.400","C44.502","C50.800","C79.200x007","C50.000x001","C50.800x005","C50.802","C79.806","C50.000","D04.501","C50.500","C50.804","C50.901","C50.300","C44.501","C50.200","D05.900","C50.600","C50.801","C50.100"]
  adrg_zd1=[]
  adrg_ss=["85.4300x003","85.4300x004","85.4301","85.4302","85.4303","85.4401","85.4402","85.4403","85.4500","85.4500x001","85.4500x003","85.4501","85.4600","85.4700","85.4800","85.2100x003","85.2100x019","85.2200","85.2300x001","85.2301","85.3300x001","85.3400x002","85.3401","85.3500x001","85.3600x001","85.3601","85.4100x001","85.4200x001","85.4200x003","40.2100","40.2200","40.2300","40.2900x002","40.2901","40.2910","40.3x00x001","40.3x00x002","40.3x00x003","40.3x00x005","40.4100","40.4200","40.5000","40.5100","40.5101","40.5901","40.5914"]
  adrg_ss1=["1","1","1","1","1","1","1","1","1","1","1","1","1","1","1","2","2","2","2","2","2","2","2","2","2","2","2","2","2","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3","3"]
  dept_list=[]
  
  ss_matched=[adrg_ss1[adrg_ss.index(x)] for x in record.ssList if x in adrg_ss]
  
  if True and record.zdList[0] in adrg_zd and ("1" in ss_matched or ("2" in ss_matched and "3" in ss_matched)):
    message('符合JA2入组条件，匹配规则：主诊断匹配、NA1特殊规则、多手术处理')
    
    if MDCJ_DRG.JA29_group(record):
      return 'JA29'

    return 'JA2'
  else:
    return ''

