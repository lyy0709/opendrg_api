from Base import message,intersect,SS_VALID
from ADRG import CB1,CB2,CB3,CB4,CC1,CD1,CD2,CJ1,CR1,CS1,CT1,CU1,CV1,CW1,CX1,CZ1

def group(record):
  mdc_zd=["H31.300","S04.000x001","D22.100x004","H01.100x006","H15.100","Q11.200x001","D31.602","H33.000x007","E11.300x015+H36.0*","H59.800x013","H16.100x008","H31.302","H02.500","A18.504+H22.0*","D31.605","H05.104","A30.900x007+H32.0*","A52.701+H22.0*","D16.408","S05.810","H16.900","H33.100x005","S05.902","D31.900","Q10.700","E14.300x071+H36.0*","C69.900x001","H59.003","H53.400x007","B02.302+H19.2*","E11.300x052+H22.1*","H11.400","H04.900x001","T20.700x012","H01.101","H18.502","H21.505","H50.300","H35.015","C69.900","E10.300x041+H36.0*","H01.801","H10.200x001","B00.501+H19.1*","H05.800","H21.300x009","S05.307","H53.102","H40.502","H04.105","Q14.200x002","H02.805","T79.800x006","H16.004","H34.202","H17.802","H33.401","H35.501","H02.504","H25.000x006","E11.300x014+H36.0*","E11.300x043+H36.0*","C69.901","T26.100x003","H44.600x006","H35.400x003","H25.900","R94.106","T20.000x011","I70.800x003","H53.600","H31.200","Q14.900","H02.803","H43.800x005","H35.800x008","Q10.303","H11.403","H50.200","E05.902+H58.8*","E14.300x034+H36.0*","H05.500x002","H05.900x003","T26.400","H20.900x006","H59.805","S05.300x010","E10.300x013+H36.0*","H21.300x008","H02.802","H05.900x002","H50.100x004","H31.901","H30.200","Q14.300x001","E10.300x042+H36.0*","H18.700x005","D31.604","H43.000","B49.x03+H19.2*","H49.810","Z52.500","H21.204","H31.000x002","H49.900","H44.700x009","S05.200x006","E11.300x053+H36.0*","T85.201","H54.600","C44.101","H44.800","A18.507+H19.0*","B00.500x002+H58.8*","H50.100x007","H11.808","S05.500x003","H04.509","H31.404","H05.201","H50.801","S05.002","H47.002","H53.100x004","E50.000x001+H13.8*","D09.200","B30.200+H13.1*","H44.700x005","H02.808","Q10.400","Q14.000","H35.400x005","H20.100","H43.200","B02.304+H13.1*","C44.100x004","H21.500x013","Q14.100x003","Q14.001","T85.300x003","H35.000x014","C69.500x003","H53.800x002","T15.000","S00.100x001","T26.101","H50.404","H21.508","H35.500x004","H40.100x001","H18.504","A18.500x010+H32.0*","S05.207","H52.400","H50.107","D48.705","T20.500x011","A50.300x002+H19.2*","H11.201","H47.001","H34.800x001","H15.800x009","H18.000","H26.100","T85.800x809","S05.301","H33.500x006","Q14.203","H02.503","H57.002","D48.900x014+H36.8*","H15.001","H21.402","A52.708+H58.8*","E10.300x091+H28.0*","C79.200x002","E65.x00x006","H47.500x003","H20.801","E11.300x022+H36.0*","H04.101","H21.103","T85.312","S05.812","E14.300x021+H36.0*","H35.806","H59.900","I86.803","H30.903","H01.901","H35.600","H11.804","H59.800x008","T26.900x001","H35.809","Q15.000","H18.002","T85.311","H18.805","C69.400x005","Q10.403","H10.300","S05.102","D31.200","Q13.900","H50.301","D31.600","H44.501","H55.x00","H21.301","B25.802+H32.0*","H43.801","H18.600","T20.100x011","Q11.000","H44.700x002","T20.400x011","Q11.202","H26.401","S02.311","H01.100x003","H17.901","L65.905","H30.000x002","H05.801","H20.101","S05.604","H53.500x005","H50.600","S05.500x001","H47.302","E05.002+H06.2*","H33.506","S05.300","H17.000","H50.003","A71.100x002","H16.804","H54.601","S05.204","H31.301","Q10.401","H44.401","H20.900x004","H35.306","A51.403+H32.0*","H53.801","E10.300x011+H36.0*","H11.200","H52.300x002","H44.000x007","H40.600","H44.700x003","H30.800x002","Q85.900x046","H21.003","A36.800x006+H22.8*","H18.800x007","C69.503","T26.001","H31.300x004","H40.800x004","H21.203","H05.800x006","D48.706","H35.400x001","E14.300x035+H36.0*","A52.102+H58.0*","H35.000x020","E14.300x047+H36.0*","H33.002","H35.014","H26.400x002","E11.300x031+H36.0*","T20.200x011","H31.200x004","T86.800x811","H01.100x005","H40.200x007","H40.503","H46.x02","T15.800x001","H44.700x008","H44.001","C69.502","H47.300x005","H18.000x005","H33.502","H50.803","E11.302+H28.0*","A18.506+H19.2*","H11.901","S05.305","H10.900","H47.005","S05.210","T26.602","T15.800x002","H21.502","H35.700x005","H05.100x005","H33.500x002","H40.100","H11.102","H47.304","Q15.900","E11.300x041+H36.0*","H30.901","H25.100","S05.206","Q14.200","T20.400x010","H54.200","H20.102","H27.800x001","E11.300x036+H36.0*","E10.300x044+H36.0*","H16.302","D03.100x003","H50.805","H25.000x003","S05.304","H02.700x001","H18.100","B30.000+H19.2*","H02.000","H35.400x007","H02.200","D21.003","H21.200","S05.800x007","E13.300x271+H36.0*","H47.101","H40.200x009","H26.202","Q14.200x004","H35.800x009","T85.300x001","H33.000","S01.000x002","H49.800x002","A30.900x006+H19.2*","H40.800x005","H18.807","H30.801","H05.500x001","H02.506","H40.200x006","H35.300x009","H10.102","E10.300x046+H36.0*","H31.101","T20.500x012","H21.002","E10.300x014+H36.0*","T85.202","Q13.101+H42.8*","D48.200x010","H05.200","H40.200x011","C69.400","H50.102","H33.300x006","Q87.800x910","H26.002","H21.300x006","Q10.300x011","T26.700x001","H59.800x009","H05.301","T85.800x806","D03.100x002","H02.300","H18.804","H18.000x006","H31.000x004","H40.500x009","H21.802","H04.103","E14.300x015+H36.0*","H02.600","C79.407","H02.003","H16.800x014","Z44.201","E14.400x180+G59.0*","H27.100","S05.805","S04.100","H47.500x002","H35.808","H11.000","A18.503+H48.8*","H44.000","H00.001","H59.809","H18.808","C79.409","C69.604","E85.418","E14.300x013+H36.0*","B02.306+H22.0*","H35.013","H16.000","H50.800x010","D31.601","H44.402","E14.300x054+H22.1*","H21.200x009","E10.300x024+H36.0*","H26.200","H34.801","H01.900","H05.300x003","H33.504","Q10.600","H53.500x007","T26.500","S05.001","E50.400x001+H19.8*","H50.500","H59.807","H21.300x005","H31.800x002","D23.100x001","Q10.300x012","H04.000x004","C69.300","D18.000x002","E50.500x001+H58.1*","S04.000x002","H33.302","H50.300x004","H04.604","H21.400","H18.700","Q13.000","S05.201","C44.100x002","Q15.803","B30.001+H19.2*","H35.300x010","H05.100x003","H30.100x002","H02.501","H04.603","D31.300","S00.202","H40.800x002","H18.400x004","A18.500x013+H22.0*","H02.703","E10.300x032+H36.0*","H44.003","Q12.900","D18.000x821","H10.200","Q13.203","H35.012","H35.805","H50.602","H55.x01","H18.800x005","H02.812","H10.401","H00.000x001","H46.x01","H26.300x001","T85.304","H04.600","H43.804","T26.800x001","H11.105","H44.802","Q13.301","H18.403","H02.400","H21.500x004","H40.102","H04.304","H49.400","S05.103","B25.800x002+H19.2*","H57.000x003","H53.300x002","T26.600x001","E14.300x023+H36.0*","H15.802","Q12.800","H35.800x010","H53.500x009","H35.400x004","H33.301","H33.300","H25.004","H52.500x003","Q10.601","B26.801+H13.1*","H35.007","H40.001","A50.000x001+H32.0*","C69.601","H16.800x003","H54.000","H35.807","H00.002","H11.803","H21.202","H16.100x005","S05.209","S05.801","N18.504+H32.8*","H31.400x003","H26.000x001","H35.200","H53.900","H35.100","H10.500x001","Q10.000","Q13.500","B05.800x001+H19.2*","H35.500x009","E11.300x012+H36.0*","H53.400x004","H35.702","H33.400","E83.500x006+H28.1*","E10.300x047+H36.0*","E14.300x014+H36.0*","H15.806","H11.300","H40.600x002","Q13.400x001","Q13.803","H04.502","S01.102","H47.100","H35.300x008","H40.202","T85.200x001","H04.600x003","H21.200x006","Q14.202","S05.804","H21.901","H04.003","I77.004","H50.103","Q13.405","A18.500x002","H05.000","C69.401","T20.000x012","Q85.804","H59.808","H15.900","E11.300x032+H36.0*","H44.500","H30.201","H50.302","H34.203","H35.800x011","B87.200x001+H58.8*","H57.800x004","T20.600x012","H44.600x003","H21.403","H16.102","H01.802","A52.702+H32.0*","Q10.300x008","H59.000","H33.503","T85.800x805","T86.800x812","H11.900","H26.003","H18.400","H18.300x002","E10.300x051+H42.0*","H53.400x005","H04.501","H31.800x001","H04.505","H59.806","S05.302","E88.906+H28.1*","H50.400","H02.705","B02.303+H03.1*","H21.300x013","H18.300","S05.400x001","H21.506","T26.301","H16.800x010","H50.002","H47.200x003","S05.900x003","H21.104","D18.000x804","H34.000","H21.300x011","S05.601","H57.800x003","Q10.600x002","H59.800x004","H50.007","E11.300x024+H36.0*","H53.101","H57.003","D31.000x002","H40.000","T85.308","H49.806","Q14.101","S05.800x001","H21.500","H50.800x002","H47.300","H20.200x001","H20.100x002","H25.200","T86.800x802","H44.700x007","H34.900","E50.100x002+H13.8*","H53.500x003","H16.300x004","C69.600","T20.100x010","T20.700x011","Q10.301","A51.404+H58.8*","H25.002","S05.605","H53.500x002","E12.300","H02.101","H04.601","S04.000x004","H59.812","H47.301","H05.202","H20.200","H16.000x010","C79.408","Q12.300","Q11.203","H25.800","B00.509+H03.1*","S01.100","T85.800x807","H02.100","H01.100x004","H50.403","H17.801","H53.104","T20.400x012","H53.501","B37.807+H48.8*","B02.305+H22.0*","H50.000x009","H18.001","H44.200","H11.806","A54.302+H13.1*","H31.402","H05.203","Q11.300","H35.000x004","T26.603","T26.600x002","H26.001","H33.500x008","Q10.500x003","H35.301","B00.500x009+H22.0*","S05.303","H02.700","B58.000","E11.300x011+H36.0*","H21.500x003","H35.010","H04.504","T26.400x001","H47.600x001","S00.100x003","H21.801","I72.803","H44.000x005","H18.500x007","S05.300x005","R94.105","H18.803","A52.700x015+H58.8*","H59.002","B00.500x005+H19.1*","A18.502+H32.0*","H35.503","H59.801","A18.500x008+H13.1*","S05.104","H18.800x014","H04.303","H59.813","T85.200","H27.800","H02.806","H40.000x001","H18.806","D22.100","H52.701","H04.800x002","H11.401","H11.100","H04.901","H05.800x005","H26.200x005","H35.000x017","E10.300x036+H36.0*","H53.300x003","H04.602","H57.800x007","H04.305","H21.000","H50.601","D31.402","Q11.100","H10.101","H16.802","H16.300x005","E10.300x021+H36.0*","H31.000x001","C79.406","H49.001","T86.809","T15.101","H49.805","H18.400x003","H16.100","B00.500x007+H22.0*","H40.300","H18.404","Z42.003","H44.901","H51.200","Q15.003","B00.502+H13.1*","E14.300x051+H42.0*","H50.802","H40.000x004","H54.500","T26.002","H52.500x004","H10.000","E14.300x036+H36.0*","H35.303","H49.803","H25.000","H21.300x012","E11.301+H36.0*","S04.000x003","A71.900","Q13.801","H02.800x016","H40.002","S05.200x003","Q14.104","H26.400","T20.300x012","H18.300x001","Q75.500","H02.811","H40.500","S02.801","H20.001","B07.x02","H50.001","H11.100x001","B00.504+H03.1*","S05.200x007","H02.002","E11.300x013+H36.0*","H04.104","T26.102","D31.901","H50.105","Q13.401","H21.800x001","H31.800x004","H10.100","H50.104","H31.401","H43.805","H53.300","E14.300x032+H36.0*","H54.900","H16.301","B30.900","H11.108","T26.100x001","H49.801","H43.802","Q11.200","H18.500x005","S05.600x002","D31.603","H16.100x006","H11.801","H40.400","H53.105","H57.001","H47.003","H05.800x003","Q15.002","H15.801","H50.100","E11.303+H22.1*","T85.903","T86.800x804","H35.011","H15.804","H05.901","H15.805","H04.300x004","H16.303","T85.302","A71.101","H35.601","H59.800x011","H54.100","C69.501","D48.700x021","H44.302","H04.800x003","H25.001","H21.300x007","H21.302","H35.602","H53.100x001","E10.300x045+H36.0*","H31.100","H35.000x019","H02.502","A18.501+H32.0*","H35.500x006","T20.200x012","D86.800x003+H22.1*","H26.000x005","H11.402","S05.903","H31.102","A18.500x005+H32.0*","S00.201","T20.000x010","H21.900","H02.800x018","E14.300x061+H28.0*","T26.604","H50.101","H44.300x003","S05.807","H49.201","H40.505","H02.901","H51.800","H40.103","H44.502","D23.302","H35.500","Q13.802","H47.500","H47.200x004","Q10.602","H34.800","H44.503","H01.000","D09.201","H21.200x007","E14.300x041+H36.0*","H53.103","H50.005","H26.901","H18.501","H16.103","H21.102","H05.300","Q87.005","H16.005","H35.802","H20.003","H47.200","T20.300x011","H18.003","H02.702","H50.500x003","H50.200x004","B30.201+H13.1*","H02.300x004","H10.400","H35.803","B89.x02+H06.1*","H59.800x010","S05.602","H05.001","E14.300x053+H36.0*","H52.000","H40.401","H35.300x011","Q10.306","A74.000+H13.1*","H04.401","E14.300x052+H22.1*","H35.900","E10.300x034+H36.0*","S01.101","H18.901","H31.000x005","A50.301+H19.2*","Z48.801","H25.800x001","H40.200","S05.811","H52.600","H21.503","H33.101","H47.004","Q15.801","H59.803","H10.801","Q10.307","H16.204","H53.300x001","H40.900","Q14.201","R44.100","H21.800","Q10.402","H35.400x006","S05.300x004","B30.300+H13.1*","H30.100x003","E10.300x012+H36.0*","H16.801","T85.310","H16.800x006","H53.100","S05.806","H49.400x001","H16.006","B30.800+H13.1*","H33.000x005","H33.501","H44.100x003","Q13.300","C79.405","H53.000x001","H04.506","T90.101","M35.005+H19.3*","D48.703","H35.500x007","H10.901","T26.601","H50.004","H50.402","H05.802","H57.100x002","E20.902+H28.1*","H18.200","H35.801","H02.900","A51.405+H58.8*","H40.500x001","H17.902","H18.402","H55.x00x002","H02.001","H55.x00x005","E14.300x043+H36.0*","H59.800x015","H11.805","E11.300x091+H28.0*","H30.900x001","H52.500x001","H57.000","H50.006","H02.004","R94.101","H04.002","T26.000","H18.405","E14.300x031+H36.0*","S05.800x009","H59.810","H51.900","H40.403","E11.300x025+H36.0*","S02.811","H35.004","B60.100x002+H13.1*","H40.200x012","D23.101","H04.500x004","H33.000x006","R93.800x008","H11.103","H50.600x003","H50.401","A39.801+H13.1*","H50.806","H43.100","Q10.500x004","Q15.004","H53.002","H59.802","A50.001+H58.8*","D31.000x001","H26.300x004","H11.800x006","H49.809","H46.x00","C49.003","D31.500x003","S05.100x004","H11.104","Q15.000x001","Q82.800x017","H40.101","H44.700","T85.300x009","H44.300x002","H02.801","H18.401","E10.301+H36.0*","H05.205","H44.102","E13.300x571+H36.0*","H05.004","H02.804","H02.800x014","H52.500","H44.300","H53.800x001","S05.101","H35.700","H49.300","H21.500x015","A71.000","H16.100x004","H26.400x003","D31.400","H54.400","H34.200x004","H16.200x001","T20.100x012","H16.400","H35.305","H11.800x005","Q10.701","H35.304","H44.100","S05.202","H34.900x001","B02.307+H19.2*","H16.000x001","B00.505+H22.0*","H26.201","H53.400x006","H44.600x007","T85.300x004","H35.300","H18.802","H31.200x006","H34.100","H31.000","D31.600x001","H44.301","H26.300","Q13.400x004","H16.800x005","H10.800x001","A52.100x012+H48.1*","H05.101","H51.801","T85.800x808","H15.800x010","A51.402+H22.0*","H50.405","H54.001","Q10.200","S01.103","D23.100x002","H25.000x002","S05.700","A50.300x003+H32.0*","H34.201","H53.401","H04.900","T20.600x011","H43.806","Q14.200x001","H44.400","D23.100x003","C44.102","T26.600x003","C69.600x001","T15.900","H16.805","H20.000x003","H34.200x005","H40.506","T85.303","S05.205","H27.900","H35.000","Q12.001","H31.403","H21.504","Q10.404","T85.300x005","E11.300x034+H36.0*","T26.401","H33.200","E50.300x001+H19.8*","Q13.400x006","Z03.801","H51.000","H35.307","D21.000","H01.100x007","H50.807","H04.508","Q13.201","T26.500x003","H04.100","H33.001","H44.300x001","Q10.302","Q18.803","T85.301","B00.507+H19.1*","H50.600x005","H18.701","H31.801","H53.402","Q12.100","T66.x02+H47.5*","H49.804","H26.900","H02.700x008","H52.200","H44.103","Q14.002","H05.103","Q10.500","H21.300x010","H20.802","E14.300x042+H36.0*","T26.500x002","H50.106","H16.200x006","H18.506","H43.200x001","H11.802","S05.200x005","H16.002","H11.404","H54.400x002","H35.002","E11.300x047+H36.0*","H21.510","H52.101","H40.801","H15.800x008","T20.700x010","H00.100","H35.009","S05.901","H16.201","B00.506+H22.0*","H15.000x002","S05.208","H34.804","H59.800x014","Q12.801","H21.507","H25.000x007","E11.300x021+H36.0*","H55.x00x001","Q11.201","H50.000","E50.600x001+H19.8*","D04.100x001","H02.800x011","Q14.000x006","T86.810","H30.000","H43.800x003","H21.201","H34.803","H18.801","H44.600","H16.203","T85.300x006","H04.102","S05.808","H04.503","H20.900","C69.800","H50.201","S05.401","E11.300x044+H36.0*","H59.800x007","H53.000","H50.500x002","H35.302","H27.102","H40.200x010","T20.300x010","H33.100x006","B58.001+H32.0*","Q14.102","E11.300x033+H36.0*","S05.803","H34.802","S05.802","D31.502","H05.000x002","H30.001","H43.800x004","S05.809","C43.100x001","H05.100","H26.000x002","H15.803","H53.001","H04.001","H33.200x004","H53.500x004","H05.204","T86.801","H16.402","Q10.304","H53.200","H53.500x008","D31.501","H35.500x005","A71.100","H35.804","H40.100x004","H49.807","H50.500x004","H20.804","H35.300x012","D17.700x005","T86.800x816","H31.200x003","H50.200x006","H26.100x002","H26.802","T20.500x010","H50.804","H11.106","Q10.100","H02.500x008","H31.802","S05.400x002","D86.801","B02.301+H58.8*","S00.100x006","H04.200","H20.000x004","H50.100x002","H11.301","T26.902","H02.813","B00.508+H22.0*","Q12.400","N18.508+H32.8*","Q14.003","H04.402","H50.202","H53.300x004","H31.900","B60.100x004+H19.2*","A06.801","I70.800x007","H02.102","H15.000","H49.901","H02.809","H27.000","H44.700x004","H53.500x006","C69.200","H59.800x003","E10.300x022+H36.0*","H30.902","B02.308+H19.0*","H01.100","A54.303+H22.0*","H47.000x009","Z46.000","H53.400x003","H18.900","H50.603","T85.200x002","E10.302+H28.0*","A54.300x002+H19.2*","T26.605","E10.300x023+H36.0*","Q13.100","Q13.500x002","D31.500x001","Q14.103","D09.202","H53.000x004","E11.300x035+H36.0*","H30.900","D48.704","H10.500","H05.102","H05.100x008","H35.000x021","H50.900","H11.100x007","C44.100x003","H50.600x004","H11.807","H40.203","S05.800x008","C69.602","H59.804","H21.401","H40.504","H49.800x007","Q15.802","H21.200x005","S05.900","H20.004","H10.103","H43.100x003","H35.005","H44.801","Q12.000","H02.301","H05.400","H05.900x004","E10.300x043+H36.0*","H59.001","H47.500x004","H47.303","H43.300","E11.300x042+H36.0*","E70.302","H05.800x002","S05.200x004","E14.300x011+H36.0*","H11.101","S05.603","H53.500","E50.200x001+H19.8*","H11.107","H30.000x005","H35.500x008","Q10.300","E11.300x046+H36.0*","H44.104","E10.300x025+H36.0*","H35.001","E14.300x012+H36.0*","H35.008","H33.304","H52.301","S05.000x002","H34.204","Z41.101","H47.006","H18.500","H04.000","H40.000x002","H25.000x005","E50.701+H19.8*","H04.302","H04.300x005","H21.101","H05.000x006","H16.003","E14.300x022+H36.0*","H43.900","Q12.002","T26.901","H20.803","H18.800x009","Q14.801","H52.501","D31.100","A36.801+H13.1*","H35.300x007","H53.400","H35.800x005","H04.500x001","H21.303","A50.300+H58.8*","D04.101","E14.300x091+H28.0*","H27.101","H05.005","C43.101","H02.900x003","E10.300x052+H22.1*","E14.300x033+H36.0*","H18.000x004","T85.300x007","H16.100x007","H31.400","C69.100","T26.900","S05.203","A51.400x005+H22.0*","C79.400x014","A71.100x003","D18.000x805","H02.000x004","E11.300x051+H42.0*","H50.300x002","H35.500x003","H33.102","H59.811","E10.300x033+H36.0*","H17.100","H53.000x005","H16.007","H35.200x001","H34.200","T20.600x010","H05.500","E14.300x046+H36.0*","H44.200x001","H40.500x002","H51.000x001","H16.000x006","H51.100","H47.400","H57.900","E14.300x045+H36.0*","H44.000x002","B30.301+H13.1*","H50.000x004","E10.300x015+H36.0*","H43.803","T26.200x001","H04.400","H52.100","H35.701","T85.309","E10.300x035+H36.0*","H44.803","H04.801","E10.300x031+H36.0*","B49.x04+H19.2*","Z42.004","H33.200x002","H02.704","H20.901","H20.002","Q15.005","H21.500x011","H52.700","H16.205","E11.300x045+H36.0*","S00.101","H57.100","H11.405","H50.800x007","T15.100x001","C69.603","H20.900x002","H16.200","H30.000x004","H35.006","H18.702","H16.803","S05.306","T85.300x008","E11.300x023+H36.0*","H43.001","E10.300x053+H36.0*","H54.300","H17.803","H18.800x012","H30.100","H34.200x002","H40.500x008","H25.800x002","H16.401","H33.100","E10.303+H22.1*","H35.502","B00.503+H58.8*","H33.303","H49.800","H53.803","H02.807","H16.101","E14.300x025+H36.0*","H35.400","H02.103","H31.800x003","H44.900","H50.800x006","H26.801","H05.002","H04.300","H21.200x008","H05.900","S00.200","Q14.301","H35.703","H02.810","H33.500","H44.101","H33.100x004","H47.000","H20.800","H50.000x002","H04.507","H50.008","H16.001","H40.501","H44.600x005","H21.100","Q12.200","E14.300x024+H36.0*","H21.501","H00.003","H44.600x004","H31.200x002","H50.800x003","C69.000x001","H53.802","T20.200x010","E14.300x044+H36.0*","H49.808","H44.002","I70.801","B30.100+H13.1*","S05.500x002","H30.900x002","H31.200x005","H44.600x002","I80.801","Q13.202","H16.100x009","H26.301","Q14.100","T15.801","B60.100x003+H19.2*"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCC入组条件，匹配规则：主诊断匹配')

  result=CB1.group(record)
  if result:
    return result
  result=CB2.group(record)
  if result:
    return result
  result=CB3.group(record)
  if result:
    return result
  result=CB4.group(record)
  if result:
    return result
  result=CC1.group(record)
  if result:
    return result
  result=CD1.group(record)
  if result:
    return result
  result=CD2.group(record)
  if result:
    return result
  result=CJ1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合CQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'CQY'

  result=CR1.group(record)
  if result:
    return result

  result=CS1.group(record)
  if result:
    return result

  result=CT1.group(record)
  if result:
    return result

  result=CU1.group(record)
  if result:
    return result

  result=CV1.group(record)
  if result:
    return result

  result=CW1.group(record)
  if result:
    return result

  result=CX1.group(record)
  if result:
    return result

  result=CZ1.group(record)
  if result:
    return result

  message('不符合MDCC的ADRG入组条件')

