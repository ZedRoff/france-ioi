nb_positions = int(input())
tab = []
nb_changements = int(input())
for _ in range(0, nb_positions, 1):
  entree = int(input())
  tab.append(entree)

for x in range(0, nb_changements, 1):
  ent1 = int(input())
  
  ent2 = int(input())
  

  
  
  tab[ent1], tab[ent2] = tab[ent2], tab[ent1]


for x in range(0, len(tab), 1):
  print(tab[x])
