entree1 = int(input())
entree2 = int(input())

tab = []

while entree1+1 > entree2:
  tab.append(entree1 * entree1)
  entree1 = entree1 - 1

print(sum(tab))
