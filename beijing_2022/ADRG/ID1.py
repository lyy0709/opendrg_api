from Base import message,intersect,SS_VALID
from DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["77.5200","77.5900x001","79.7801","79.7802","79.8801","79.8802","79.8803","80.0800x001","80.0800x002","80.0801","80.1800x003","80.1801","80.1802","80.4800x002","80.4800x005","80.4801","80.4802","80.4803","80.4804","80.7800","80.7800x002","80.7801","80.8800x003","80.8800x004","80.8801","80.8802","80.9800","80.9800x001","81.1400x002","81.1401","81.1700x001","81.1700x003","81.9301","81.9302","84.1101","84.1102","84.1103"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合ID1入组条件，匹配规则：主手术匹配')
    
    if MDCI_DRG.ID19_group(record):
      return 'ID19'

    return 'ID1'
  else:
    return ''

