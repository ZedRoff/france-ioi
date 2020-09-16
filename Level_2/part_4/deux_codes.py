

running = True
status = 0


while running:
  n = int(input("Entrez le code : \n"))
  if n == 4242 and status == 0:
    status = 1
    print("Premier code bon.")
  elif n == 2121 and status == 1:
    print("Bravo.")
    running = False
  else:
    pass
