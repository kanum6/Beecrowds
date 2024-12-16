a, b, c = [int(x) for x in input().split()]
a1, b2, c3 = [int(x) for x in input().split()]
Rr = 0

if a1 > a:
    Rr += a1 - a
    

if b2 > b:
    Rr += b2 - b

if c3 > c:
    Rr += c3 - c

print (Rr)