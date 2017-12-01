def showBase(n, b):
  digits = "0123456789abcdefghijklmnopqrstuvwxyz"
  def go(n, b):
    xs = ""
    while (n > 0):
      xs += digits[n % b]
      n = n // b
    else:
      xs = "0" if xs == "" else xs
    return xs[::-1]
  try:
    return go(n, b)
  except (IndexError):
    print("Base should be between 2 and 36.")

def readBase(s, b):
  digits = "0123456789abcdefghijklmnopqrstuvwxyz"
  def go(s, b):
    n = 0
    power = 1
    while (s != ""):
      n += digits.index(s[-1:]) * power
      power *= b
      s = s[:-1]
    return n
  try:
    return go(s, b)
  except (IndexError):
    print("Base should be between 2 and 36.")

def test():
  for b in range(2, 37):
    print("Base " + str(b) + ":")
    for i in range(20):
      print(showBase(i, b), end=" ")
      assert i == readBase(showBase(i, b), b)
    print()

test()
