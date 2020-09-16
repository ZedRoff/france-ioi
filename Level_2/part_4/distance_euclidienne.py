from math import *

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

def square(n):
   return n ** 2

print(sqrt(square(x2 - x1) + square(y2 - y1)))
