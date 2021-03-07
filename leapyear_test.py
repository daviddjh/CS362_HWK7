import leapyear

def test_leapyear():
  assert leapyear.isleapyear(1) == False
  assert leapyear.isleapyear(4) == True
