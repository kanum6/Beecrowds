x = int(input())
cont = 6
if x%2 != 0:
    print (x)
    cont -=1

while cont != 0:
    x += 1
    if x%2 != 0:
        print (x)
        cont -= 1

    else:
        continue