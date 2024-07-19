from Base import message,intersect,SS_VALID
from DRG import MDCG_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["29.3201","29.5302","31.9500","31.9501","34.0200x001","42.0100","42.0900x001","42.0900x002","42.0901","42.0902","42.1000","42.1100","42.1200","42.1901","42.2100","42.2200","42.2500","42.3100x001","42.3101","42.3200x003","42.3200x006","42.3201","42.3900","42.7x00x001","42.7x01","42.7x02","42.7x04","42.8200","42.8300","42.8400","42.8500","42.8501","42.8502","42.8600","42.8701","42.8900","42.9100x002","43.0x00x003","43.0x01","43.0x02","43.0x03","43.1900x003","43.1900x005","43.1900x006","43.4900","43.8200","43.8201","43.8202","44.0000","44.0001","44.0100","44.0200","44.0200x002","44.0300x001","44.1500","44.2900x003","44.3100","44.4000","44.4100x008","44.4101","44.4102","44.4200x001","44.4200x003","44.4201","44.4202","44.4300x003","44.4400x001","44.4400x005","44.4401","44.4402","44.4403","44.4901","44.4902","44.5x00x002","44.5x00x004","44.5x00x005","44.5x01","44.5x02","44.6100x003","44.6200","44.6300x001","44.6301","44.6302","44.6400","44.6401","44.6500","44.6500x001","44.6500x002","44.6500x003","44.6501","44.6701","44.6800x002","44.6801","44.6901","44.6902","44.9100x001","44.9100x002","44.9100x005","44.9101","44.9201","44.9501","44.9502","44.9601","44.9602","44.9701","44.9800x003","44.9800x004","44.9801","44.9802","45.0100x005","45.0100x006","45.0101","45.0102","45.0200x002","45.3101","45.3102","45.3200x001","45.6202","46.0100","46.0100x001","46.0101","46.0102","46.7100","46.7200","46.7900x009","46.7901","46.7902","46.7903","46.7904","51.8200x001","51.8200x002","97.5901","97.5902","97.5903","98.0200x001","98.0201"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合GC1入组条件，匹配规则：主手术匹配')
    
    if MDCG_DRG.GC11_group(record):
      return 'GC11'

    if MDCG_DRG.GC13_group(record):
      return 'GC13'

    if MDCG_DRG.GC15_group(record):
      return 'GC15'

    return 'GC1'
  else:
    return ''

