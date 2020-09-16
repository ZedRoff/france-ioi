tab = []
nHabitants = int(input())

for x in range(0, nHabitants, 1):
  entree = int(input())
  tab.append(entree)

tab.sort()

if len(tab) // 2 < len(tab) / 2:
  print(tab[len(tab) // 2])
else:
  print((tab[(len(tab) // 2) - 1] + tab[(len(tab) // 2)]) / 2 )
