tab = []
nParticipants = int(input())


for x in range(0, nParticipants, 1):
  entier = int(input())
  tab.append(entier)

tab.sort()

for x in range(0, len(tab) // 2, 1):
  print("{} {}".format(tab[x], tab[len(tab)-(x+1)]))
