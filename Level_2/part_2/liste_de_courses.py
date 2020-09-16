l1 = [9, 5, 12, 15, 7, 42, 13, 10, 1, 20]
l2 = []
for x in range(0, len(l1), 1):
  ent = int(input())
  l2.append(ent)

l3 = []
for x in range(0, len(l2), 1):
  l3.append(l1[x] * l2[x])

print(sum(l3))
