from math import * 

qtt = input()
qtt = float(qtt)

q = 60
prix = 45

sacs = 0
count = 0
if qtt == 0:
  count = 0
else:
  while sacs < qtt:
    sacs+=60
    count+=1

print(floor(count * 45))
