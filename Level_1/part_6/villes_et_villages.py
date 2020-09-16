nbLieux = int(input())
count = 0
for x in range(0, nbLieux, 1):
  nbGens = int(input())
  if nbGens > 10000:
    count+=1
  else:
    count = count
  
print(count)
