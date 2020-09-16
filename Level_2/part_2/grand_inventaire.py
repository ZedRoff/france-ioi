produits = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
nbOpe = int(input())
for x in range(0, nbOpe, 1):
  entier1 = int(input())
  entier2 = int(input())
  if entier2 < 0:
    produits[entier1-1] = produits[entier1-1] - abs(entier2)
  else:
    produits[entier1-1] = produits[entier1-1] + entier2
  
for x in range(0, len(produits), 1):
  print(produits[x])
