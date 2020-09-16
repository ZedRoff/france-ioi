entree1 = int(input())
entree2 = int(input())
if entree1 > 6:
  entree1 = 6
elif entree2 > 6:
  entree2 = 6

resultat = entree1 + entree2
if resultat >= 10:
  print("Taxe spéciale !")
  print("36")
else:
  print("Taxe régulière")
  entree1 = entree1 * 2
  entree2 = entree2 * 2
  print(entree1 + entree2)
