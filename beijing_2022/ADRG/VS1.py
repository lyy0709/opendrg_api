from Base import message,intersect,SS_VALID
from DRG import MDCV_DRG

def group(record):
  adrg_zd=["T78.000","T78.101","T78.102","T78.200","T78.201","T78.300","T78.300x003","T78.300x004","T78.301","T78.400","T78.400x002","T80.300","T80.300x001","T80.400","T80.500","T80.500x001","T80.600x004","T80.600x005","T80.600x006","T80.601","T80.602","T80.603","T80.900x003","T80.901","T80.903","T88.600","T88.601","T88.700x004"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合VS1入组条件，匹配规则：主诊断匹配')
    
    if MDCV_DRG.VS19_group(record):
      return 'VS19'

    return 'VS1'
  else:
    return ''

