from Base import message,intersect,SS_VALID
from DRG import MDCD_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["27.5301","27.5302","27.5303","27.5400","27.5401","27.5700x006","27.5900x011","27.5900x017","27.5900x018","27.5900x019","27.5900x020","27.5901","27.5902","27.5903","27.5904","27.5905","27.5906","27.5907","27.5908","27.5909","27.5910","27.5911","27.5912","27.5913","27.5914","27.5915","27.6100","27.6200x002","27.6200x003","27.6201","27.6300x002","27.6301","27.6302","27.6400","27.6900x003","27.6900x004","27.6900x007","27.6900x008","27.6901","27.6902","27.6903","27.6904","27.6905","27.6906","27.6907","27.6908","27.6909","27.7100","27.7202","27.7300","27.9100x001","27.9101"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合DB3入组条件，匹配规则：主手术匹配')
    
    if MDCD_DRG.DB33_group(record):
      return 'DB33'

    if MDCD_DRG.DB35_group(record):
      return 'DB35'

    return 'DB3'
  else:
    return ''

