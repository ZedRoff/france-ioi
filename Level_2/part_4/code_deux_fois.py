running = True

status = 0
while running:
  code = int(input("Entrez le code : \n"))
  if code == 4242:
    status = 1
    print("Encore une fois.")
    while status == 1:
      code2 = int(input("Entrez le code : \n"))
      if code2 == 4242:
        print("Bravo.")
        running = False
        status = 0
