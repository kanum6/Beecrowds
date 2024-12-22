while True:
    a, b = [int(x) for x in input().split()]
    if a == b:
        break

    elif a > b:
        print ("Decrescente")
        continue

    elif b > a:
        print ("Crescente")
        continue