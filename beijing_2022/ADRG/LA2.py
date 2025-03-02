from Base import message,intersect,SS_VALID
from DRG import MDCL_DRG

def group(record):
  adrg_zd=["C64.x00x001","C64.x00x003","C64.x00x004","C65.x00","C65.x01","C65.x02","C67.000","C67.100","C67.200","C67.300","C67.400","C67.500","C67.501","C67.700","C67.800","C67.900","C67.900x002","C68.803","C68.804","C76.301","C79.101","D41.400x001"]
  adrg_zd1=[]
  adrg_ss=["57.4900x001","57.4901","57.4902","57.4903","57.4904","57.5100","57.5100x001","57.5100x003","57.5101","57.5102","57.5900x001","57.5900x002","57.5901","57.5902","57.5903","57.5905","57.5906","57.6x00","57.6x01","57.6x02","57.6x03","57.6x04","57.6x05","57.6x06","57.7100","57.7101","57.7102","57.7103","57.7900x001","57.7901","57.8700x005","57.8700x006","57.8700x007","57.8700x008","57.8700x009","57.8701","57.8702","57.8703","57.8704","57.8706"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合LA2入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    if MDCL_DRG.LA21_group(record):
      return 'LA21'

    if MDCL_DRG.LA25_group(record):
      return 'LA25'

    return 'LA2'
  else:
    return ''

