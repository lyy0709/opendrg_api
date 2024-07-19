from Base import message,intersect,SS_VALID
from ADRG import XJ1,XR1,XR2,XR3,XS1,XS2,XT1,XT2,XT3

def group(record):
  mdc_zd=["T85.802","T85.902","T92.502","Z01.501","Z47.800x003","Q98.500","Z47.800x008","Z58.900","Z63.200x001","Z72.000","Z03.800x701","Z46.501","T93.206","Z54.000x014","T92.300x011","Z10.100","R18.x00x003","T92.100x008","R47.802","Z65.300x001","T92.500x014","T95.100x001","Z57.507","Z63.300x001","Z73.100x001","T90.203","Z63.000","T95.200x003","Z12.500","Z47.800x018","T93.400","Z30.000x002","Z75.100","Z24.300","Q93.100","Z03.800x721","R79.000x001","Z47.800x013","Q95.300","T85.801","T92.600","Z50.600","Z45.101","Z57.508","R62.000x003","T90.102","R49.800x003","Z20.001","Z24.400","T93.800x001","Z01.502","T90.000","Z47.900","Z76.800x001","Z71.200","Q97.200","Z75.400","T95.001","Z29.201","Z11.100","Z70.900","R87.900x003","T93.300x005","R46.801","R46.100","Z65.900","Z44.300","Z57.700","R58.x00x005","Z23.100","Z76.500","T95.000x010","Q89.901","Z01.800x001","Z54.000x016","Q90.200","Q98.400","T93.801","T92.500x011","R89.200","T92.300x002","Z47.800x035","Z29.200x001","Z45.200","Z28.101","R41.200","T92.106","R25.200x009","Z23.500","Z51.800","Z54.000x012","R79.803","Z09.900x001","Z63.500x002","Z57.100","M23.208","Q99.200","T95.000x002","M23.204","R62.900","R19.002","R93.202","B90.801","M24.803","Z13.800x022","Z03.900","Z03.101","Z23.200","R89.500","Z32.000x001","T92.800x001","Z45.202","Z71.800","T92.503","Z09.001","Z59.800","Z57.300","T84.901","Z58.500","Z64.400x002","T92.100","T73.100","T92.401","Z30.505","Z46.503","Z63.700x091","R17.001","T92.301","Z47.800x020","R58.x00x002","R54.x00x003","Z31.401","Z42.900","Z10.000","Z54.000x019","T92.400x006","T93.300x008","T92.500x017","T92.105","T95.000x007","T98.300x007","Z03.803","Z50.300","R71.x00x005","T92.900","Z02.300","Z30.500x011","Z46.602","Z46.800x001","Z56.000","T97.x01","Z23.700","Z29.101","T80.800","T92.600x003","Z11.901","Z01.700","R74.000x001","R47.000x006","R17.000","Z31.900","Z75.900x001","B94.100","Z58.600","Z54.800x001","R77.200","B94.000","R89.400","T90.204","R13.x00","Z04.500","R25.200x002","R72.x00x002","Z22.100","Z03.800","Z54.000x013","R84.900x004","T92.500x003","Z61.200x001","Q99.100x003","Z56.700","T95.103","Z63.800x003","Z50.500","Z65.300x002","Z47.800x006","Z63.800x004","Z59.100","Q95.800","B90.200x002","T91.000x002","T85.806","Z00.200","Z01.900","Z11.902","Z22.801","Z51.300","R11.x02","Q92.700","T93.200x012","Z30.400x004","Z59.000x001","Z57.506","Z61.000x001","Q91.200","Q95.900","Q96.200","T96.x00x002","Z12.800","R53.x00x006","I69.400","T91.800x010","R54.x00","T93.900","Q93.200","Q99.100","T95.000x005","T92.300x013","T90.800x002","R60.000","R79.000x004","R19.003","T92.500x018","R61.900","R79.000x006","T93.300x009","T98.200x031","Z13.300x003","Q91.500","Z22.302","Z45.900","T95.300x003","Z30.202","Z60.100x001","R79.000x003","Z11.803","Z43.101","T92.603","Z28.201","M24.805","Z31.600x001","T90.207","T95.101","R79.000x002","R54.x01","Z41.800x002","Z72.100","Z04.001","Z01.101","Z10.300","Z13.300","Z43.302","R68.101","Q92.300","T91.502","T92.300","T92.500x013","Z09.802","Z46.603","Z56.500","Z54.100","Z22.101","Z30.103","T92.300x017","Z46.502","R74.900x001","Z50.000","R47.003","T92.801","Z50.100x001","Z20.400","Z50.900x001","Z65.300x005","Z20.801","R25.200x008","R74.804","Z63.500x001","Z57.201","R62.000x002","Q95.500","Z25.100","Z28.100","T95.800x004","R77.800x001","Z22.102","Z73.000","R52.200","Z74.900","R25.200x006","R59.901","T90.500x003","R11.x03","M24.806","Z26.000","T91.002","Z58.800","Z52.000","T91.802","T95.900","Z59.700","Z65.400x002","Z43.400x002","Z74.300","R18.x00x005","R70.101","Q98.300","Z20.000","Z47.800x019","Z57.800","Z46.601","Q87.800x905","R23.100x002","Z23.600","Z13.100","R89.900x002","Q96.400","Z09.300","Z54.000x007","E89.900","T70.400","R63.200x002","Z00.300","R68.100x002","T91.800x007","Z43.400x003","R85.901","Z46.600x001","Z20.802","Z22.700","T95.000x012","R68.000","B90.002","Z30.800x003","Z20.701","Z65.300x003","T95.100x003","Z01.300","R52.901","Z65.100x001","B90.800x006","R74.801","Z01.002","Z61.400x001","Z01.102","Z63.700x011","T94.102","Z56.400","Z30.000x001","B90.804","Z04.900","Z30.400x001","Z64.300","Z65.300x004","R62.801","Z24.100","R63.200","Z45.803","T95.800x002","Z65.400x003","Z30.301","R52.100","Z22.103","I69.801","Z43.102","B90.803","M24.807","Z55.300","Z01.800x002","Z60.400","Z62.200x001","Z24.500","Q99.800","T90.208","Q87.800x907","Z65.500x003","Z61.500x001","T95.301","T95.400","Q97.300","Z40.800","T95.300x002","Q96.000","R46.000","Z43.600x002","Z24.001","Z63.400x003","T93.400x005","R74.800x007","T94.100","Z46.700","Z47.800x030","T73.900","Z72.500","Z63.700x001","Z76.900","Q99.000","R85.902","R77.200x001","B90.001","T92.300x001","R19.000x003","Z22.200","Z26.900","Z04.400","T92.101","Z43.403","T92.400x004","R23.100","Z30.800x001","R47.000x001","T95.202","Z13.000x001","Q93.600","T93.203","Z54.900x001","Z56.300","Z71.500","B90.100","R63.000","Z20.100","Z27.100","Z03.802","Z31.400x003","R84.901","T93.205","Z54.800x008","Z75.000","Z27.200","Z27.900","Z58.000","Z63.900","R74.001","Z75.200","R18.x00x001","Z43.700","Z43.300","Z13.800x051","T92.103","T91.000x001","Z50.800x002","T98.301","Z40.900x001","Z47.800x028","Z46.500x001","Q93.000","R89.800","R74.800x006","Z62.600x001","R60.901","B94.801","T93.300x003","R58.x00x007","R98.x00x002","T90.400x002","Z11.800x001","Z47.800x017","Z48.900x001","Q92.100","R23.000","R61.001","Q87.806","R64.x00x002","T91.200x002","R77.801","T92.104","T92.204","R44.801","T92.500x004","Z54.800x009","B94.900","T73.300","Z43.402","B90.903","T91.206","Z54.800x006","R76.100","R58.x00x004","R76.800x001","Z26.800","Z75.300","B90.902","T81.601","Q85.914","R93.301","Z02.500","Z63.800x001","T91.800x008","Z70.800","Z12.400","Z57.504","R41.800x002","Z54.000x010","Z73.900","R46.700","R53.x00x002","Z72.900","Z28.800","R25.200x007","R96.100x001","Z24.600","R47.100x001","R61.901","R23.101","Z39.100x001","Q92.800","T92.100x005","T94.001","T91.000x003","Z01.001","Z43.500","Z54.000x004","T92.300x006","Z20.900","T95.800x006","Z57.400","T92.200","Z54.800x004","T90.401","Z74.100x001","Z13.200","T80.202","Z59.900","R89.700","Z46.800x002","R89.300","Z00.500x001","Z29.000","T93.600x003","T95.800x003","Z28.000","T92.505","Z20.200","Z27.800","Z50.501","Z04.002","Z51.401","Z55.800","R63.300x002","T90.500x002","R76.900","Z13.800x011","T92.000","T93.200x001","T93.200x014","T90.400x004","Z03.800x731","Z24.200","Z30.800x002","R49.801","T95.000x003","Z54.000x005","Z13.300x002","Z58.700","R93.501","Z61.800","Z03.100","R87.900x001","Z54.000x006","Z54.000","Z03.300","T70.900","Q97.000","T92.001","Q93.700","Z76.000","R53.x00x012","Q97.100","T93.600x002","Z22.600","Z42.000","T92.300x008","Z50.400x001","Z54.800x010","Z54.800x005","Z57.503","T84.400","Z02.800","R69.x00","R53.x00x010","T92.302","T92.800x002","Z63.500x003","Z63.700x021","Z64.100x001","R46.300","R79.000","Q98.200","Z65.800","T95.000x009","Q95.400","R53.x00x003","Z20.300","T92.400","Z43.802","Z22.000","Z01.503","T92.304","Z00.100","Z12.300","Z13.900","R77.800x004","T91.800x005","T92.303","Z13.801","Z23.000","Z44.200x002","Z54.700","B94.101","Z76.400","T93.800","T95.201","Z43.400x004","Z31.400x004","R77.800x003","B90.201","Z71.700","Z73.200","Q96.300","B90.901","B90.200x003","T84.900","Z13.800x032","Z54.000x002","Z48.000x001","T91.803","R68.800x003","T90.100","T91.800x004","B94.200","R68.100x001","T91.800x002","Z54.800x003","Z50.200","T90.200x012","T95.801","T95.200x005","Z22.402","Z62.500x001","M23.201","Q91.000","T86.900","Z71.100","T96.x00x001","R46.500","T92.305","T95.000x006","Z03.103","Z30.800x005","Z61.300x001","T92.402","Z47.800x031","Z54.000x022","K07.601","Q89.900","T93.600x001","Q89.400","T92.400x007","T92.500x015","T95.200x001","Z65.500x002","Q92.600","T92.300x012","M23.202","Z04.300","Z11.300","Z45.201","T93.000","Q98.600","T91.400","Z61.900x001","T73.800","T93.500x002","R53.x00x005","Z41.300","R19.000x008","T80.203","R53.x00x011","Z54.000x018","Z11.200","Z22.400","Z13.001","R76.801","R93.800x002","T95.102","Z55.100","R52.900","Z75.500","Z03.800x711","Z41.900","Z63.400x001","R74.802","Q91.700","R60.900","Z22.900x001","Z10.800","T95.802","Z39.100x003","R77.800x006","R87.900x002","Z13.600","T93.300x002","R89.600","T91.202","R62.803","T91.500x003","Q96.900","R68.200","R68.300","T95.300x001","Z13.500x001","Z51.400x002","Z63.400x002","T91.204","Z73.400","Q99.102","R47.000x008","T93.400x003","Z47.800x036","Z51.400x001","M23.215","Z70.300","Q97.800","R60.100","Z46.900","T90.400x003","T93.208","Z27.000","R19.000x016","Q93.300","T92.500x008","T92.102","Z30.201","Q99.101","Q99.801","Z01.600","R79.804","Z43.602","Z13.700","R53.x00x001","Z27.300","R47.000x005","Q96.100","B92.x00","R41.100","T92.300x015","Z31.500","T93.300x001","T91.900x003","R79.800x005","R89.900x001","Z23.300","R76.000x001","T91.201","T92.306","T90.200","T95.000x004","T98.200x032","Z01.600x001","R63.400","Z12.200","Z43.301","R53.x00x004","T91.501","Z43.201","T92.602","Z52.300x002","Z57.900","Z58.400","R68.800x002","R47.001","Z59.600","R47.100x002","R19.000x012","Z23.400","R25.200x005","R47.002","Z47.800x007","B91.x00","R26.100","Z09.804","Z45.802","Q98.100","Z46.701","Z47.800x011","Z55.400","Z60.300x002","T94.000","Z62.100x001","Q98.000","Z30.504","Q98.900","T95.200x002","Z04.601","T90.400x001","B90.800x005","T93.200x007","T97.x00x003","T92.100x011","T93.301","T80.801","T91.900","Z11.600","Z46.600","T92.100x010","T91.800x001","Q98.800","Z30.203","Q96.800","Z32.100","Z54.400","Z09.700","R93.800x003","Z03.102","Z74.800","Z61.700x001","Z71.600","B94.800x003","Z13.501","Z54.800x007","T93.501","M23.214","Z72.600","Z59.300","R74.803","R68.800x001","T92.307","I69.800x002","Z72.200","Z30.501","B90.802","R23.200x002","T84.700x001","Z54.800x002","T95.000x011","Z57.600","Z76.100","T91.001","Z60.200x001","Z63.700x092","Z00.401","Z50.801","Q89.700","R77.901","R84.902","R46.800x001","T95.000x001","T92.400x005","T92.506","Z54.000x021","Z62.300x001","R10.201","T93.200","Z71.000","T75.200","T95.800x008","Z09.803","R19.000x013","Z11.500","R10.200x001","Q95.200","Z11.801","Z24.601","T92.201","Z30.302","Z62.800","Z12.000","R41.000","T95.800x005","Z65.400x001","Z75.800x001","T87.200","Z43.604","Z47.800x021","T90.201","Z64.400x001","Z73.500","Z76.201","Z41.801","Z55.900","R99.x00x002","R25.200x004","T92.100x009","Q99.802","R77.800x002","R62.802","Q97.900","T92.202","T95.100x002","R63.601","M23.501","Z00.001","Z22.800","Z25.000","T84.700","R63.100","Z43.601","R61.000","Z47.800x023","Z29.800","Z73.600","B90.200","R74.800x003","Z09.801","T93.200x011","R47.801","T90.205","T92.500x010","Z22.300","T93.207","Z01.600x002","Z47.800x014","Z02.400","R89.100","R63.100x002","T91.401","T94.002","Z47.800x010","Z76.300","T92.501","M24.810","R70.100","Z47.800x027","Z31.402","Z63.600","Q91.100","T93.200x008","Z03.600x001","M24.808","Z02.600","T90.202","Z47.800x016","Z43.900x001","R52.000","R60.001","Q93.800","Z23.800x001","T93.400x006","Z02.700","N81.800x006","R76.802","Z30.400x003","T91.800x003","Z60.000x001","Z62.400x001","Q92.000","T88.901","T90.206","Z27.400x001","Z10.200","R89.900x003","T92.500x009","Z54.000x015","R53.x00x009","Z64.200","Q92.500","M23.211","R63.300x003","Z00.300x001","Z02.000","Z31.800","R74.800x005","Z47.800x024","Z74.200","Z13.400x001","Z00.800","T92.300x016","T92.601","T93.202","Z47.800x009","R76.100x001","T93.201","Z57.505","T92.600x002","Z60.800","Z47.800x033","R77.900","B90.800x004","Q90.100","B94.802","Z20.702","Z48.000x002","Q91.600","R71.x00","R77.803","Z02.200","R47.004","Z52.001","Z47.800x012","Q99.900","R19.000x009","Z63.800x002","Z39.200x001","Z04.800","Z55.200","Z54.300","Z43.603","M23.209","T92.300x005","T93.200x002","T93.800x002","Z61.600x001","R74.800x008","Z45.806","R82.500x001","T95.000x008","Z70.200","T93.001","T93.500x001","T95.002","Z56.200","Z30.503","T96.x00x003","T91.000x004","Z73.300","R77.000","Z54.000x009","Z01.200","Z56.100","M24.100x091","Z25.800x001","T90.200x008","T92.504","T78.900","T93.400x004","Z64.400x003","Z09.400","Z20.500","Z71.300","Z45.805","T91.205","Z47.800x034","Z28.900","Z70.100","T92.300x007","Z71.400","Z22.301","Z59.500","Z04.100","Q91.400","T82.812","Z47.800x025","Z22.401","R79.900","T93.200x013","Z59.400","B90.000","R18.x01","Z54.000x020","T92.400x008","Z51.901","R41.001","T92.100x004","T73.200","T92.500x001","Z43.401","Z61.100x001","Z52.900","Z54.000x008","T95.200x006","Z04.200","Z29.900","R19.001","Z30.000x003","Z43.100","R54.x00x002","Z43.200","Z39.100x002","Z43.801","Z12.100","Z54.000x017","Z63.700x093","Z70.000","Q87.801","R11.x01","T97.x02","R68.300x002","R76.200","Z20.600","Z58.100","R77.802","T91.900x002","Z47.800x015","Z60.900","Z62.000x001","Z72.400","R82.100","Z02.900","Z13.800x021","Z71.900","T92.500x007","Q92.900","T93.200x010","Z72.800","T93.204","T98.000","Z51.600","T92.500x002","Z57.000","Z57.501","R77.101","R89.000","Z65.500x001","B90.904","Z56.600","T91.200","T95.803","Z51.400x003","Z65.000","T92.400x003","Z47.800x026","Q95.000","Z31.202","R41.300x001","Z54.000x003","R46.600","B90.202","Z60.500","R79.805","Q92.400","R47.101","Z11.000","Z47.800x004","Z59.200","M23.212","R26.100x001","Z62.900","R58.x00x006","Z73.800","Z55.000","T69.900","T98.200","R71.x00x004","Z09.000x001","R63.500","T91.500x001","Z74.000","Z58.200","Q95.100","I69.802","Z13.800x061","R61.100","Z45.807","Z01.800x004","Z63.100x001","Z02.100","Z40.000x001","T92.500x012","T92.400x002","R99.x01","T93.400x002","T92.500x006","B94.800x001","Z13.800x031","Z43.400x005","Z72.300","Z54.200x001","R53.x00x008","Z50.700x001","Z45.804","Z12.900x001","T91.200x005","T93.600","T90.901","T91.800x009","B90.101","Z12.600","Z13.500","Z22.303","T95.200x004","Z03.900x001","Z57.502","Z30.900","R76.200x002","Z50.101","Z30.800x004","T90.900","Q92.200","R18.x00","M23.203","R19.004","Z31.203","Z47.800x005","R77.100","Z47.800x022","T95.800x001","Z58.300","Z30.101","R79.800x003","Q98.700","T85.800","Z00.600","T91.800x006","Z12.901","Z47.800x029","Z65.200","R70.000","B94.201","T93.800x003","T95.800x007","Z29.100","M24.102","Z11.400","T92.203","Z30.102","Z11.802","Z13.800x041","Z47.800x032"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCX入组条件，匹配规则：主诊断匹配')

  result=XJ1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合XQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'XQY'

  result=XR1.group(record)
  if result:
    return result

  result=XR2.group(record)
  if result:
    return result

  result=XR3.group(record)
  if result:
    return result

  result=XS1.group(record)
  if result:
    return result

  result=XS2.group(record)
  if result:
    return result

  result=XT1.group(record)
  if result:
    return result

  result=XT2.group(record)
  if result:
    return result

  result=XT3.group(record)
  if result:
    return result

  message('不符合MDCX的ADRG入组条件')

