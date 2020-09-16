



nbKarvas = int(input())

tab = []

for x in range(0, nbKarvas):
  poids = int(input())
  age = int(input())
  longueur = int(input())
  hauteur = int(input())
  tab.append(longueur * hauteur + poids)

for x in range(0, len(tab)):
  print(tab[x])
