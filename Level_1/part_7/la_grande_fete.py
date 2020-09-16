hdebut = int(input())
hfin = int(input())

tab = [_ for _ in range(hdebut, hfin+1, 1)]

nbInvites = int(input())
count = 0
for x in range(0, nbInvites, 1):
  harrivee = int(input())
  hdepart = int(input())
  if hdepart >= hdebut and harrivee <= hfin:
    count+=1
  else:
    pass

print(count)
