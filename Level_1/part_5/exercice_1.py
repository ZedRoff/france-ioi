nbMembres = int(input())
poids_1 = []
poids_2 = []
for i in range(0, nbMembres):
  for x in range(0, 1):
    pds_entree_1 = int(input())
    pds_entree_2 = int(input())
    poids_1.append(pds_entree_1)
    poids_2.append(pds_entree_2)

if sum(poids_1) > sum(poids_2):
  print("L'équipe 1 a un avantage")
else:
  print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 : {}".format(sum(poids_1)))
print("Poids total pour l'équipe 2 : {}".format(sum(poids_2)))
    
 
