from Base import message,intersect,SS_VALID
from DRG import MDCZ_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["17.1100x001","17.1200x001","17.1300x001","17.1300x002","17.2100x001","17.2200x001","17.2300x001","17.2400x001","17.3100","17.3101","17.3200","17.3200x001","17.3300","17.3300x002","17.3400","17.3401","17.3500","17.3500x001","17.3600","17.3600x001","17.3900x002","17.3900x003","17.3901","39.2401","41.2x01","41.4200x002","41.4200x003","41.4300","41.5x00","41.5x01","41.9501","43.0x00x003","43.0x02","43.1900x003","43.1900x005","43.5x00x003","43.5x00x007","43.6x00x005","43.6x00x006","43.6x01","43.6x02","43.7x00x001","43.7x03","43.8100","43.8201","43.8901","43.8903","43.9101","43.9900x002","43.9900x003","43.9900x004","43.9901","43.9903","43.9905","44.5x00x002","44.5x00x004","44.5x00x005","44.6100x003","44.6200","44.6300x001","44.6400","44.6500x001","44.6500x002","44.6600x002","44.6601","44.6701","44.6800x002","44.6902","44.9201","45.0100x005","45.0201","45.0203","45.0300x002","45.0302","45.1101","45.6100","45.6201","45.6202","45.6203","45.6204","45.6205","45.6206","45.6207","45.6300","45.7100x001","45.7200x002","45.7200x004","45.7202","45.7300x003","45.7300x006","45.7300x007","45.7301","45.7302","45.7400x003","45.7401","45.7500","45.7500x001","45.7600x008","45.7601","45.7900x002","45.7901","45.8100","45.8200","45.9100x006","45.9100x008","45.9103","45.9104","45.9200","45.9300x012","45.9300x013","45.9300x014","45.9300x015","45.9301","45.9302","45.9303","45.9304","45.9305","45.9306","45.9307","45.9310","45.9400x004","45.9400x009","45.9400x012","45.9400x016","45.9401","45.9402","45.9403","45.9405","45.9406","45.9407","45.9502","45.9503","45.9504","46.0100x001","46.0101","46.0300x001","46.0300x003","46.0400x002","46.0401","46.1000x007","46.1100","46.1300","46.1301","46.2100","46.2300x001","46.2400","46.3200x002","46.3900x002","46.3900x006","46.3900x007","46.3901","46.3902","46.3904","46.3905","46.4200","46.4300x004","46.4300x005","46.4302","46.5100x002","46.5100x004","46.5100x006","46.5101","46.5102","46.5200x006","46.5200x010","46.5200x011","46.5201","46.5202","46.5203","46.5204","46.7100","46.7200","46.7300x005","46.7301","46.7302","46.7400x004","46.7403","46.7500x004","46.7501","46.7502","46.7503","46.7504","46.7505","46.7601","46.7602","46.7603","46.7900x009","46.7902","46.8101","46.8102","46.8201","46.8202","47.1100","47.1900x001","47.9200","48.0x00x002","48.0x00x003","48.0x02","48.0x03","48.1x00","48.2101","48.4900x002","48.4900x003","48.4901","48.5100","48.5100x002","48.5200","48.5201","48.5900x001","48.6100","48.6200","48.6301","48.6302","48.6400x001","48.6500x001","48.6902","48.6903","48.6904","48.6905","48.7100","48.7200","48.7300x001","48.7301","48.7303","48.7400","48.7401","48.7501","48.7600x001","48.7600x002","48.7600x008","48.7601","48.7602","48.7603","48.7900x003","48.9100","50.0x00x008","50.0x00x016","50.0x01","50.2200","50.2200x003","50.2200x004","50.2200x005","50.2200x006","50.2200x007","50.2200x008","50.2200x009","50.2201","50.2205","50.3x01","50.3x02","50.3x03","50.4x00","50.6101","50.6900x002","50.6901","50.9900x003","51.2100","51.2200","51.2200x004","51.2201","51.3100","51.3201","51.3202","51.3400","51.3601","51.3602","51.3700x001","51.3700x002","51.3700x003","51.3700x007","51.3701","51.3702","51.3703","51.3704","51.3900x005","51.3901","51.3902","51.3903","51.3904","51.3905","51.3906","51.4201","51.4302","51.4304","51.5100","51.5101","51.5900x001","51.5900x005","51.5900x006","51.5900x008","51.5900x009","51.5901","51.5903","51.7200x001","51.7201","51.7202","51.7203","51.7900x002","51.7900x005","51.7900x006","51.7901","51.7902","51.7903","51.7904","51.7906","51.8100","51.8200x001","51.8200x002","51.8300x003","51.8301","51.9100","51.9200","51.9300x001","51.9301","51.9305","52.5100x001","52.5101","52.5102","52.5103","52.5104","52.5201","52.5202","52.5203","52.5204","52.5300","52.5901","52.5905","52.6x00","52.6x00x003","52.6x01","52.7x00","52.7x00x003","52.9201","52.9500x001","52.9500x002","52.9501","52.9504","52.9601","52.9602","53.7101","53.7201","53.7202","54.0x00x001","54.0x00x002","54.0x00x004","54.0x00x006","54.0x00x010","54.0x00x013","54.0x00x018","54.0x00x021","54.0x00x022","54.0x00x023","54.0x00x024","54.0x00x025","54.0x01","54.0x02","54.0x03","54.1100","54.1101","54.1201","54.1900x001","54.1900x005","54.1900x006","54.1900x010","54.1900x011","54.1900x020","54.1900x023","54.1901","54.1902","54.1904","54.1906","54.1907","54.3x04","54.6101","54.6301","54.6400","54.6401","54.7100","54.7200x001","54.7300x001","54.7400x001","54.7400x002","54.7400x003","54.7400x004","54.7400x005","54.7400x006","54.7404","54.7500x002","54.7501","54.9201","54.9300x001","54.9300x011","54.9501","54.9502","54.9900x017","55.0100x010","55.0101","55.0107","55.0109","55.1100x001","55.5100","55.5101","55.5103","55.5104","55.5200","55.5201","55.5300x001","55.5400","55.5401","55.8101","55.8701","55.8702","55.8703","55.8704","55.8901","56.4105","56.4200","56.5102","56.6100x001","56.6100x003","56.6100x004","56.7100x002","56.7101","56.7103","56.7200","56.7400","56.7402","56.7501","56.8200x002","56.8201","56.8500","56.8900x001","56.8901","56.8902","56.8908","57.1901","57.1903","57.1905","57.2100","57.7101","57.7900x001","57.7901","57.8100","57.8500x002","57.8501","57.8700x005","57.8700x006","57.8700x007","57.8700x008","57.8700x009","57.8701","57.8704","57.8706","57.8900x001"]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合ZD1入组条件，匹配规则：主手术匹配')
    
    if MDCZ_DRG.ZD19_group(record):
      return 'ZD19'

    return 'ZD1'
  else:
    return ''

