nb = int(input())

running = True
nb_tests = 0
while running:
    entree = int(input())
    nb_tests+=1
    if entree < nb:
        print("c'est plus")
    elif entree > nb:
        print("c'est moins")

    elif entree == nb:
        print("Nombre d'essais nécessaires :\n{}".format(nb_tests))
        running = False

