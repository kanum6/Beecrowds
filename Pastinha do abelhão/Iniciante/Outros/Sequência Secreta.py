a = int(input())
Nt = 0
numC = 1

for i in range (a):
    num = int(input())
    if num != numC:
        Nt += 1
    numC = num
    

print (Nt+1)