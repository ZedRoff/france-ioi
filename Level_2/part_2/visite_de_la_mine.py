nDeplacements = int(input())

tab = []
for _ in range(0, nDeplacements, 1):
  entree = int(input())
  tab.append(entree)

nTab = []
for x in range(0, len(tab), 1):
  if tab[x] == 1:
    nTab.append(2)
  elif tab[x] == 2:
    nTab.append(1)
  elif tab[x] == 3:
    nTab.append(3)
  elif tab[x] == 4:
    nTab.append(5)
  elif tab[x] == 5:
    nTab.append(4)

nTab.reverse()
for x in range(0, len(nTab), 1):
  print(nTab[x])
