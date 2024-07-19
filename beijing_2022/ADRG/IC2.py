from Base import message,intersect,SS_VALID
from DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["00.8500x001","00.8600x001","00.8700x001","81.5100","81.5200x004","81.5201","81.5202","81.5400","81.5400x004","81.5400x005","81.5400x007","81.5400x008","81.5401","81.5600","81.5700x001","81.5700x002","81.8000","81.8000x003","81.8100","81.8101","81.8400","81.8400x002","81.8401","81.8800"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合IC2入组条件，匹配规则：主手术匹配')
    
    if MDCI_DRG.IC29_group(record):
      return 'IC29'

    return 'IC2'
  else:
    return ''

