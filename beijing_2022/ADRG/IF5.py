from Base import message,intersect,SS_VALID
from DRG import MDCI_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["76.9700","76.9700x001","76.9700x002","76.9701","76.9702","77.0101","77.0102","77.0103","77.0104","77.7101","77.7102","77.8909","78.5900x025","78.6100x004","78.6101","78.6102","78.6103","78.6104","78.6105","78.6106","78.6107","78.6108","78.6201","78.6202","78.6301","78.6302","78.6303","78.6304","78.6401","78.6402","78.6403","78.6404","78.6501","78.6502","78.6600x002","78.6600x003","78.6601","78.6602","78.6701","78.6702","78.6703","78.6704","78.6705","78.6706","78.6800x005","78.6801","78.6802","78.6803","78.6804","78.6900x002","78.6900x008","78.6900x010","78.6900x016","78.6900x017","78.6901","78.6902","78.6903","78.6904","78.6905","78.6906","78.6907","78.6908"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合IF5入组条件，匹配规则：主手术匹配')
    
    if MDCI_DRG.IF53_group(record):
      return 'IF53'

    if MDCI_DRG.IF55_group(record):
      return 'IF55'

    return 'IF5'
  else:
    return ''

