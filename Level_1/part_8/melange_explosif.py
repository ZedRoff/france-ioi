nb_mesures = int(input())
nb_min = int(input())
nb_max = int(input())
running = True
count = 0


for x in range(0, nb_mesures, 1):
  entree = int(input())
  if entree >= nb_min and entree <= nb_max:
    print("Rien à signaler")
  else:
    print("Alerte !!")
    break
