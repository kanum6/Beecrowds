a = int(input())

for i in range(a):
    a, b = [int(x) for x in input().split()]
    if b == 0:
        print ("divisao impossivel")
        continue
    print (a/b)