nbMarches = int(input())
nbMarches = abs(nbMarches)
tab = []
for x in range(0, nbMarches, 1):
  dParcouru = int(input())
  tab.append(dParcouru)
print(max(tab))
