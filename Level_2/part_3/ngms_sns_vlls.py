tlivre = input()
alivre = input()

voyelles = ["A", "E", "I", "O", "U", "Y"]
tab = []
tab2 = []
for x in range(0, len(tlivre), 1):
  if tlivre[x] in voyelles:
    pass
  elif tlivre[x] == " ":
    pass
  else:
    tab.append(tlivre[x])

for x in range(0, len(alivre), 1):
  if alivre[x] in voyelles:
    pass
  elif alivre[x] == " ":
    pass
  else:
    tab2.append(alivre[x])

res1 = ""
for x in range(0, len(tab), 1):
  res1+=tab[x]

res2 = ""
for x in range(0, len(tab2), 1):
  res2+=tab2[x]

print(res1)
print(res2)
