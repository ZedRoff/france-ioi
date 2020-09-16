nbLivres = int(input())
longueurMinimale = int(input())


titles = []
resumes = []
for x in range(0, nbLivres, 1):
  titre = input()
  titles.append(titre)
  resume = input()
  resumes.append(resume)


tab = []
for x in range(0, len(titles), 1):
  if len(resumes[x]) < longueurMinimale:
    tab.append(titles[x])
  else:
    pass
  
for x in range(0, len(tab), 1):
  print(tab[x])
