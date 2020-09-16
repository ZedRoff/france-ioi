nbMD = int(input())
alt = []
desc = []
for x in range(0, nbMD, 1):
  vAltitude = int(input())
  if vAltitude < 0:
    desc.append(abs(vAltitude))
  else:
    alt.append(abs(vAltitude))
  
print(sum(alt))
print(sum(desc))
