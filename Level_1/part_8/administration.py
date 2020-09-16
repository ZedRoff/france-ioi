running = True
res = 0
while running:
    entree = int(input())
    if entree == -1:
        running = False
    else:
        res+=entree
    
print(res)
