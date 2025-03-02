from Base import message,intersect,SS_VALID
from DRG import MDCL_DRG

def group(record):
  adrg_zd=["A02.205+N16.0*","B65.002+N22.0*","N10.x02","N11.000x001","N11.100","N11.801","N11.802","N11.900x001","N11.900x003","N12.x02","N13.600","N13.600x001","N13.600x002","N13.600x004","N13.601","N13.602","N13.603","N13.604","N13.605","N15.101","N15.102","N15.801","N15.900x002","N15.900x003","N15.900x004","N15.901","N28.801","N28.834","N28.836","N28.838","N28.839","N30.000","N30.201","N30.300","N30.801","N34.000","N34.000x005","N34.001","N34.002","N34.100","N34.101","N34.102","N34.200x003","N34.200x004","N34.200x006","N34.201","N34.202","N34.203","N34.204","N34.205","N34.300","N39.000","N39.001","T83.500","T83.500x002","T83.500x003","T83.501"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合LU1入组条件，匹配规则：主诊断匹配')
    
    if MDCL_DRG.LU11_group(record):
      return 'LU11'

    if MDCL_DRG.LU13_group(record):
      return 'LU13'

    if MDCL_DRG.LU15_group(record):
      return 'LU15'

    return 'LU1'
  else:
    return ''

