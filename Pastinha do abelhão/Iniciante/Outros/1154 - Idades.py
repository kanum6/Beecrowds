Ti = 0
Tm = 0
while True:
    a = int(input())
    if a < 0:
        print (f"{Ti/Tm:.2f}")
        exit()
    Ti += a
    Tm += 1