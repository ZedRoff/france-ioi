nbCharettes = int(input())
tab = []
for x in range(0, nbCharettes, 1):
  entree = float(input())
  tab.append(entree)

n = sum(tab) / nbCharettes

nTab = []
for x in range(0, len(tab), 1):
  nTab.append(n - tab[x])

for x in range(0, len(nTab), 1):
  print(nTab[x])
