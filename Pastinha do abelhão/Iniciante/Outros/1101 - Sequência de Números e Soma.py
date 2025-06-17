while True:
    soma = 0
    a, b = [int(x) for x in input().split()]
    if a <= 0 or b <= 0:
        break

    if a > b:
        val1 = b
        val2 = a

    elif b > a:
        val1 = a
        val2 = b

    for i in range (val1, val2 + 1):
        print (i, end=(" "))
        soma += i

    print (f"Sum={soma}")