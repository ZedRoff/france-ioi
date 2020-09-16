nLignes = int(input())

for _ in range(0, nLignes, 1):
  ligne = input()
  ligne = list(ligne)
  ligne.reverse()
  print("".join(ligne))
