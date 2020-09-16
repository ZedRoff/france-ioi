nbJetons = int(input())
xs = []
ys = []
for _ in range(0, nbJetons, 1):
  x = int(input())
  xs.append(x)
  y = int(input())
  ys.append(y)

for x in range(0, len(xs), 1):
  if xs[x] >= 10 and xs[x] <= 85 and ys[x] <= 20 and ys[x] >= 10:
    print("Dans une zone bleue")
  elif xs[x] >= 10 and xs[x] <= 25 and ys[x] <= 45 and ys[x] >= 10:
    print("Dans une zone bleue")
  elif xs[x] >= 50 and xs[x] <= 85 and ys[x] <= 45 and ys[x] >= 10:
    print("Dans une zone bleue")
  elif xs[x] >= 10 and xs[x] <= 85 and ys[x] >= 45 and ys[x] <= 55 and ys[x] >= 10:
    print("Dans une zone bleue")
  elif xs[x] >= 15 and xs[x] <= 45 and ys[x] >= 60 and ys[x] <= 70:
    print("Dans une zone rouge")
  elif xs[x] >= 60 and xs[x] <= 85 and ys[x] and ys[x] >= 60 and ys[x] <= 70:
    print("Dans une zone rouge")
  elif xs[x] >= 0 and xs[x] <= 90 and ys[x] <= 10 and ys[x] >= 0:
    print("Dans une zone jaune")
  elif xs[x] >= 0 and xs[x] <= 10 and ys[x] <= 55 and ys[x] >= 10:
    print("Dans une zone jaune")
  elif xs[x] >= 85 and xs[x] <= 90 and ys[x] >= 10 and ys[x] <= 55:
    print("Dans une zone jaune")
  elif xs[x] >= 0 and xs[x] <= 90 and ys[x] >= 55 and ys[x] <= 60:
    print("Dans une zone jaune")
  elif xs[x] >= 0 and xs[x] <= 15 and ys[x] >= 60 and ys[x] <= 70:
    print("Dans une zone jaune")
  elif xs[x] >= 45 and xs[x] <= 60 and ys[x] >= 60 and ys[x] <= 70:
    print("Dans une zone jaune")
  elif xs[x] >= 85 and xs[x] <= 90 and ys[x] >= 60 and ys[x] <= 70:
    print("Dans une zone jaune")
  elif xs[x] >= 25 and xs[x] <= 50 and ys[x] >= 20 and ys[x] <= 45:
    print("Dans une zone jaune")
  else:
    print("En dehors de la feuille")
