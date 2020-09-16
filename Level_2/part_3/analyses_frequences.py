nbLM = input().split(" ")
nbLignes = int(nbLM[0])
nbMots = int(nbLM[1])

tab = []
for x in range(0, nbLignes, 1):
  entree = input()
  tab.append(entree)
  
nTab = []
for x in range(0, len(tab), 1):
  nTab.append(tab[x].split(" "))


act = [0] * nbMots
for x in range(0, len(nTab), 1):
  for i in range(0, len(nTab[x]), 1):
    if len(nTab[x][i]) > nbMots:
      pass
    else:
      act[i+1] = act[i+1] + len(nTab[x][i])
    
  
print(act)
