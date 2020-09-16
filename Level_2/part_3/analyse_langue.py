lettre = input()
n = int(input())
count = 0
for x in range(0, n, 1):
  ligne = input()
  for x in range(0, len(ligne), 1):
    if ligne[x] == lettre:
      count+=1
    else:
      pass
print(count)
