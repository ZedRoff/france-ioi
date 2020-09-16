nX = int(input())
nhash = int(input())
nRow = int(input())
triangle = int(input())
print("X" * nX)
print()
print("#" * nRow)
nhash = nhash - 2
if nhash < 0:
  nhash = 0
for x in range(0, nhash, 1):
  if nRow == 1:
    print("#")
  else:
    print("#"+" "*(nRow-2)+"#")
print("#" * nRow)
print()
for x in range(0, triangle, 1):
  if x == 0:
    print("@")
  elif x == 1:
    print("@@")
  elif x == triangle-1:
    print("@" * (triangle))
  else:
    print("@"+" "*(x-1)+"@")
