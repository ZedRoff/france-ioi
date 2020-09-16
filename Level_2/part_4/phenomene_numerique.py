from math import *

tab = []

def check(n):
  running = True
  while running:
    x = n/2
  
    if x.is_integer():
      n = n/2
      tab.append(round(n))
    elif n == 1:
      running = False
    else:
      n = n * 3 +1
      tab.append(round(n))
  print(" ".join(list(map(lambda g: str(g), tab))))

  
entree = int(input())
check(entree)
