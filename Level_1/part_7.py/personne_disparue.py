tab = []
numero = int(input())
tailleliste = int(input())

for x in range(0, tailleliste, 1):
  entree = int(input())
  tab.append(entree)

if numero in tab:
  print("Sorti de la ville")
else:
  print("Encore dans la ville")
