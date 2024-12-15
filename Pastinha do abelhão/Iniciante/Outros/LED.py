qnt = int(input())

n1 = 2
n2 = 5
n3 = 5
n4 = 4
n5 = 5
n6 = 6
n7 = 3
n8 = 7
n9 = 6
n0 = 6
qleds = 0

for i in range (qnt):
    leds = input("")

    for carac in leds:
        if carac == "1":
            qleds += n1

        if carac == "2":
            qleds += n2

        if carac == "3":
            qleds += n3

        if carac == "4":
            qleds += n4
        
        if carac == "5":
            qleds += n5

        if carac == "6":
            qleds += n6

        if carac == "7":
            qleds += n7

        if carac == "8":
            qleds += n8

        if carac == "9":
            qleds += n9

        if carac == "0":
            qleds += n0
        

    print (qleds, "leds")
    qleds = 0        