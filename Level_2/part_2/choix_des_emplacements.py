nbMarchands = int(input())
tab = [0] * nbMarchands
for x in range(0, nbMarchands, 1):
  entree = int(input())
  tab[entree] = x

for x in range(0, len(tab), 1):
  print(tab[x])
