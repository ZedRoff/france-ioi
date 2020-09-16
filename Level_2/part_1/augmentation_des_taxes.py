from math import *
 
pourc1 = float(input())
pourc2 = float(input())
prix = float(input())
 
prix_initial = prix/(1 + pourc1/100)
prix_nouveau = round(prix_initial*(1 + pourc2/100), 2)

print(round(prix_nouveau, 2))
