from Base import message,intersect,SS_VALID
from DRG import MDCI_DRG

def group(record):
  adrg_zd=["A18.000x018+M49.0*","A18.000x047+M49.0*","A18.000x048+M49.0*","A18.000x049+M49.0*","A18.000x066+M49.0*","A18.005+M49.0*","A18.006+M49.0*","A18.007+M49.0*","A18.008+M90.0*","A18.009+M49.0*","A18.010+M49.0*","A18.011+M49.0*","A18.012+M49.0*","A18.013+M49.0*","A23.901+M49.1*","M24.203","M24.204","M24.205","M24.301","M24.302","M40.000","M40.000x091","M40.100","M40.100x051","M40.101","M40.200x021","M40.200x041","M40.200x061","M40.201","M40.300","M40.401","M40.402","M40.500","M40.501","M41.000","M41.101","M41.200","M41.300","M41.400","M41.400x091","M41.401","M41.500","M41.501","M41.800","M41.900","M41.900x061","M41.901","M42.900","M43.001","M43.002","M43.003","M43.004","M43.005","M43.006","M43.007","M43.008","M43.009","M43.100x011","M43.100x021","M43.100x041","M43.100x061","M43.100x062","M43.100x071","M43.100x091","M43.101","M43.102","M43.201","M43.202","M43.203","M43.300","M43.400","M43.501","M43.502","M43.503","M43.504","M43.505","M43.600","M43.601","M43.602","M43.801","M43.802","M43.803","M43.804","M43.805","M43.901","M46.000","M46.000x093","M46.000x094","M46.001","M46.002","M46.003","M46.004","M46.100","M46.300","M46.300x021","M46.300x041","M46.300x061","M46.301","M46.302","M46.400","M46.401","M46.402","M46.403","M46.500x091","M46.500x092","M46.501","M46.502","M46.503","M46.504","M46.800x091","M46.800x093","M46.802","M46.803","M46.900","M47.201","M47.202","M47.203","M47.204","M47.205","M47.800x024","M47.800x031","M47.800x032","M47.801","M47.802","M47.803","M47.804","M47.806","M47.901","M47.902","M47.903","M47.904","M48.000x081","M48.001","M48.002","M48.003","M48.004","M48.005","M48.006","M48.100","M48.100x091","M48.200","M48.200x021","M48.200x041","M48.200x061","M48.300x091","M48.301","M48.302","M48.303","M48.304","M48.305","M48.500x092","M48.501","M48.502","M48.503","M48.800x022","M48.800x091","M48.801","M48.802","M48.803","M48.804","M48.805","M48.806","M48.808","M48.810","M48.811","M48.812","M48.900x002","M48.901","M48.902","M48.903","M48.904","M50.200x001","M50.201","M50.202","M50.300x001","M50.301","M50.800","M50.900","M50.901","M51.200x001","M51.200x004","M51.200x005","M51.201","M51.202","M51.203","M51.204","M51.205","M51.301","M51.302","M51.303","M51.304","M51.305","M51.400","M51.800x003","M51.800x004","M51.801","M51.802","M51.803","M51.901","M53.201","M53.202","M53.203","M53.204","M53.205","M53.206","M53.207","M53.208","M53.209","M53.210","M53.211","M53.212","M53.301","M53.302","M53.303","M53.304","M53.305","M53.306","M53.801","M53.802","M53.900","M54.100","M54.100x021","M54.101","M54.102","M54.103","M54.104","M54.105","M54.106","M54.107","M54.200","M54.300","M54.400","M54.500","M54.501","M54.502","M54.503","M54.504","M54.505","M54.507","M54.600","M54.801","M54.900","M62.600x081","M84.100x081","M85.000x001","M85.000x002","M85.000x004","M85.000x007","M85.000x008","M96.100","M96.200","M96.300","M96.400","M96.500","M96.802","M96.803","M99.200x001","M99.200x002","M99.200x003","M99.200x004","M99.200x005","M99.200x006","M99.300x001","M99.300x002","M99.300x003","M99.300x004","M99.300x005","M99.300x006","M99.400x001","M99.400x002","M99.400x003","M99.400x004","M99.400x005","M99.400x006","M99.500x001","M99.500x002","M99.500x003","M99.500x004","M99.500x005","M99.500x006","M99.600","M99.700x002","Q67.500","Q67.501","Q67.502","Q67.503","Q76.000x002","Q76.000x003","Q76.000x004","Q76.000x005","Q76.001","Q76.100","Q76.100x004","Q76.200","Q76.200x103","Q76.201","Q76.202","Q76.203","Q76.300","Q76.300x011","Q76.400x101","Q76.400x102","Q76.400x201","Q76.400x203","Q76.400x301","Q76.400x302","Q76.400x303","Q76.400x304","Q76.400x305","Q76.400x306","Q76.400x307","Q76.400x308","Q76.400x310","Q76.400x313","Q76.400x324","Q76.400x903","Q76.400x905","Q76.400x906","Q76.401","Q76.402","Q76.403","Q76.404","Q76.405","Q76.406","Q76.407","Q76.408","Q76.409","Q76.412","Q76.413","Q76.414","Q76.415","Q76.416","Q76.417","Q76.418","Q76.419","Q85.900x034","S12.000","S12.000x002","S12.010","S12.100","S12.100x002","S12.100x003","S12.110","S12.200x011","S12.200x021","S12.200x031","S12.200x041","S12.200x051","S12.210","S12.700","S12.710","S12.900x001","S12.900x003","S12.900x004","S12.900x005","S12.900x006","S12.910","S13.000","S13.100","S13.100x021","S13.100x022","S13.100x031","S13.100x032","S13.100x041","S13.100x042","S13.100x051","S13.100x052","S13.100x061","S13.100x062","S13.100x071","S13.100x072","S13.100x081","S13.100x082","S13.101","S13.102","S13.103","S13.104","S13.200x003","S13.201","S13.202","S13.203","S13.300","S13.400x006","S16.x00x001","S16.x00x002","S22.000x003","S22.000x005","S22.000x006","S22.000x007","S22.000x009","S22.000x011","S22.000x021","S22.000x031","S22.000x041","S22.000x051","S22.000x061","S22.010","S22.100","S22.110","S23.000","S23.100x011","S23.100x012","S23.100x021","S23.100x022","S23.100x031","S23.100x032","S23.100x041","S23.100x042","S23.100x051","S23.100x052","S23.100x061","S23.100x071","S23.101","S29.000x001","S29.000x002","S32.000x002","S32.000x011","S32.000x021","S32.000x031","S32.000x041","S32.000x051","S32.010","S32.100","S32.110","S32.200","S32.210","S32.702","S32.800x021","S32.800x022","S32.800x023","S32.800x024","S32.810","S32.813","S33.000","S33.100x011","S33.100x021","S33.100x031","S33.100x041","S33.100x051","S33.201","S33.301","S33.500","S33.500x011","S33.501","S33.502","S33.600","S33.601","S33.700x002","S33.700x003","S33.703","S39.906","T08.x00","T08.x10","T09.200x001","T09.200x002","T09.200x003","T09.200x004","T09.200x007"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合IU2入组条件，匹配规则：主诊断匹配')
    
    if MDCI_DRG.IU23_group(record):
      return 'IU23'

    if MDCI_DRG.IU25_group(record):
      return 'IU25'

    return 'IU2'
  else:
    return ''

