k = int(input())
Tt = 0

for i in range(k):
    a, b = [int(x) for x in input().split()]
    if a == 1001:
        Tt += 1.50*b

    elif a == 1002:
        Tt += 2.50*b

    elif a == 1003:
        Tt += 3.50*b

    elif a == 1004:
        Tt += 4.50*b

    elif a == 1005:
        Tt += 5.50*b

print (f"{Tt:.2f}")