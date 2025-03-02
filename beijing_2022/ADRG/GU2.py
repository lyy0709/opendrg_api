from Base import message,intersect,SS_VALID
from DRG import MDCG_DRG

def group(record):
  adrg_zd=["K22.100","K22.101","K22.102","K22.103","K25.000","K25.000x001","K25.000x002","K25.001","K25.300x001","K25.400x001","K25.400x002","K25.401","K25.700","K25.900x001","K25.901","K25.902","K25.903","K26.000","K26.001","K26.300","K26.400x003","K26.401","K26.701","K26.900x001","K26.900x002","K27.000","K27.300","K27.400","K27.400x001","K27.400x002","K27.400x004","K27.401","K27.700x001","K27.900x001","K27.900x002","K27.900x005","K27.901","K27.902","K28.000","K28.300x001","K28.400x002","K28.401","K28.700","K28.900x001","K28.901","K31.800x808","K63.302","K63.303","K63.304","K63.305","K63.306","K63.307"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  dept_list=[]
  
  if True and record.zdList[0] in adrg_zd:
    message('符合GU2入组条件，匹配规则：主诊断匹配')
    
    if MDCG_DRG.GU21_group(record):
      return 'GU21'

    if MDCG_DRG.GU23_group(record):
      return 'GU23'

    if MDCG_DRG.GU25_group(record):
      return 'GU25'

    return 'GU2'
  else:
    return ''

