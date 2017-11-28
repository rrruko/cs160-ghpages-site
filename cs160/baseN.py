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

def test():
  for b in range(2, 37):
    print("Base " + str(b) + ":")
    for i in range(20):
      print(showBase(i, b), end=" ")
    print()
