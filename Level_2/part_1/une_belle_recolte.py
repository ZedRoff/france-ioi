nbPersonnes = int(input())
nbFruits = int(input())

res = nbFruits / nbPersonnes

res = str(res).split(".")


if res[1] == '0':
  print("oui")
else:
  print("non")
