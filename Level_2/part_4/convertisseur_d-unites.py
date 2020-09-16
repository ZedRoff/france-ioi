nValeurs = int(input())

tab = []
for x in range(0, nValeurs, 1):
  entree = input()
  tab.append(entree)
nTab = []
for x in range(0, len(tab), 1):
  q = tab[x].split(" ")
  if q[1] == "m":
    print("{} {}".format(float(q[0])/0.3048, "p"))
  elif q[1] == "g":
    print("{} {}".format(float(q[0]) * 0.002205, "l"))
  elif q[1] == "c":
    print("{} {}".format(32 + 1.8 * float(q[0]), "f"))
 
