n = int(input())

q = []
for x in range(0, n, 1):
  note = int(input())
  q.append(note)

print(sum(q) / n)
