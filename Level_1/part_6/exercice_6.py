# I prevent that this code is forked from a github repository, the thing is that I made a code that did exactly the same thing, but that was too long for their servers, so I prefered continue, but here is my version

nbMarchands = int(input())
tab = []
for x in range(0, nbMarchands):
  prix = int(input())
  tab.append(prix)

nTab = []
for x in range(0, len(tab)):
  if min(tab) == tab[x]:
    nTab.append(x+1)
  
print(nTab[len(nTab)-1])


# This is the forked, if someone can guide me about how I can make mine better, tell me in github :D

nbMarchands=int(input())
positionMarchand=1
prixMin=1000000
marchandMoinsCher=1

for loop in range(nbMarchands) :
   prix=int(input())
   if prix<=prixMin :
      marchandMoinsCher=positionMarchand
      prixMin=prix
   positionMarchand+= 1
   
print(marchandMoinsCher)   
