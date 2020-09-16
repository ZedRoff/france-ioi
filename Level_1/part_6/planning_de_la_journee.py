pActuel = int(input())
nVillage = int(input())
tab = []
for x in range(0, nVillage, 1):
  pos = int(input())
  tab.append(pos)


nTab = []
for x in range(0, len(tab), 1):
  res = pActuel - tab[x]
  nTab.append(abs(res))


nTab2 = []
for x in range(0, len(nTab), 1):
  if nTab[x] <= 50:
    nTab2.append(nTab[x])
  
print(len(nTab2))
