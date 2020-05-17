def primary():
  import random

  last = 13
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  for i in range(3):
    rnd = random.randint(0, last)
    print(quotes[rnd])

if __name__== "__main__":
  primary()
