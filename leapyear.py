

def isleapyear(year):
  if year % 4 != 0:
    return False
  else:
    if year % 100 != 0:
      return True
