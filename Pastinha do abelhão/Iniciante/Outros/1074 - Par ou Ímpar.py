n = int(input())

for i in range(n):
    pi = int(input())
    if pi == 0:
        print ("NULL")

    elif pi%2 == 0:
        if pi > 0:
            print ("EVEN POSITIVE")

        else:
            print ("EVEN NEGATIVE")

    else:
        if pi > 0:
            print ("ODD POSITIVE")

        else:
            print ("ODD NEGATIVE")

