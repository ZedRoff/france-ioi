cArignon = int(input())
cErwan = int(input())

rArignon = cArignon ** 2
rErwan = cErwan ** 2

if cArignon - cErwan>10:
  print("La famille {} a un champ trop grand".format("Arignon"))
elif cErwan - cArignon > 10:
  print("La famille {} a un champ trop grand".format("Evaran"))
else:
  print("")
