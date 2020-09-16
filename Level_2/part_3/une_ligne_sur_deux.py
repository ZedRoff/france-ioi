nbLignes = int(input())
tab = []
for x in range(0, nbLignes, 1):
  entree = input()
  tab.append(entree)

nTab = []

count = 1

while count <= len(tab):
  print(tab[count-1])
  count+=2
