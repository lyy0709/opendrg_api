from Base import has_mcc,has_cc,intersect
def KB19_group(record):
  return True
def KC19_group(record):
  return True
def KD19_group(record):
  return True
def KD29_group(record):
  return True
def KE19_group(record):
  return True
def KU19_group(record):
  return True
def KJ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KZ11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def KR13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KS13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KT13_group(record):
  return len(record.zdList)>1 and (has_mcc(record.zdList[0],record.zdList[1:]) or has_cc(record.zdList[0],record.zdList[1:]))
def KJ15_group(record):
  return True
def KR15_group(record):
  return True
def KS15_group(record):
  return True
def KT15_group(record):
  return True
def KV15_group(record):
  return True
def KZ15_group(record):
  return True

