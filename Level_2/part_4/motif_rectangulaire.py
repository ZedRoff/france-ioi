def create(n, m, l):
  tab = []
  for x in range(0, m, 1):
    tab.append(l)
  for i in range(0, n, 1):
    print("".join(tab))
    
  
n = int(input())
m = int(input())
l = input()

create(n, m, l)
