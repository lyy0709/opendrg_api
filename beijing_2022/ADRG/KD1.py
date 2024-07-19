from Base import message,intersect,SS_VALID
from DRG import MDCK_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["06.1301","06.2x00","06.2x01","06.2x02","06.2x03","06.2x04","06.3900x001","06.3900x003","06.3900x004","06.3900x011","06.3900x012","06.3900x013","06.3901","06.3902","06.3903","06.3904","06.3905","06.3906","06.3907","06.3908","06.4x00","06.4x01","06.4x02","06.5000","06.5100","06.5101","06.5200","06.6x00","06.9401","40.4100","40.4200","40.5901"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合KD1入组条件，匹配规则：主手术匹配')
    
    if MDCK_DRG.KD19_group(record):
      return 'KD19'

    return 'KD1'
  else:
    return ''

