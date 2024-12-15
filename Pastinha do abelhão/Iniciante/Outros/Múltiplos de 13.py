a = int(input())
b = int(input())
Tt = 0
if b < a:
    for i in range (b, a+1):
        if i%13 != 0:
            Tt += i

else:
    for i in range (a, b+1):
        if i%13 != 0:
            Tt += i

print (Tt)