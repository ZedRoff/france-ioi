
tab1 = []
tab2 = []

for x in range(0, 6, 1):

  auteur = input()
  tab1.append(auteur)
  titre = input()
  tab2.append(titre)

nTab1 = []
nTab2 = []


b = 1

for x in range(0, len(tab1), 1):
  nTab2.append(tab2[x])
  nTab1.append(tab1[b-1])
  b+=1
  

for x in range(0, len(nTab1), 1):
  print(nTab2[x])
  print(nTab1[x])
