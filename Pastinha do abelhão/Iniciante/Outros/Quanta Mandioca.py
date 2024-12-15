C = int(input())
B1 = int(input()) 
B2 = int(input())
M = int(input())
L = int(input())
Tt = 0
Tt2 = C + B1 + B2 + M + L
while Tt2 != 0:
    Tt2 -= 1
    if C >= 1:
        Tt += 300
        C -= 1

    elif B1 >= 1:
        Tt += 1500
        B1 -= 1

    elif B2 >= 1:
        Tt += 600
        B2 -= 1

    elif M >= 1:
        Tt += 1000
        M -= 1

    elif L >= 1:
        Tt += 150
        L -= 1

print (Tt + 225)