nbLegumes = int(input())

p = []
a = []
pr = []
for x in range(0, nbLegumes, 1):
  pds = float(input())
  p.append(pds)
  age = float(input())
  a.append(age)
  prix = float(input())
  pr.append(prix)

for x in range(0, nbLegumes, 1):
  print(pr[x] / p[x])
