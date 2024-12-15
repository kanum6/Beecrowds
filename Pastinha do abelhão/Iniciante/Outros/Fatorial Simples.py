n = int(input())
Ft = n
for i in range (n):
    Ft -= 1
    if Ft == 1:
        break
    n *= Ft

print (n)