from robot import *
max = 10
depart = 0

iterator = 0
for x in range(depart, max, 1):
  iterator = iterator + 1
  for i in range(0, iterator, 1):
    droite()
  ramasser()
  for i in range(0, iterator, 1):
    gauche()
  deposer()
