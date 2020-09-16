nbPersonnes = int(input())

names = []
surnames = []
for x in range(0, nbPersonnes, 1):
  entree = input()
  entree = entree.split(" ")
  names.append(entree[0])
  surnames.append(entree[1])

for x in range(0, len(surnames), 1):
  print("{} {}".format(surnames[x], names[x]))
