population = int(input())
croissance = float(input())
from math import *

calc =  (population * croissance) / 100

print(floor(calc + population))
