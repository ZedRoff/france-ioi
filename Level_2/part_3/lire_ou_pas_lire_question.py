nbLivres = int(input())

tab = []
for x in range(0, nbLivres, 1):
  entree = input()
  tab.append(entree)

nTab = []
counter = 0
for x in range(0, len(tab), 1):
  
  if len(tab[x]) > counter:
    nTab.append(tab[x])
    counter = len(tab[x])
  else:
    pass

for x in range(0, len(nTab), 1):
  print(nTab[x])
