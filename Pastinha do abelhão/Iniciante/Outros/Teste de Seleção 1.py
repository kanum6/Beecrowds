ask = input()
a, b, c, d = ask.split(" ")

if int(c) > 0 and int(b) > 0 and int(b) > int(c) and int(d) > int(a) and int(c) + int(d) > int(a) + int(b) and int(a) % 2 == 0:
    print ("Valores aceitos")
    exit()

else:
    print ("Valores nao aceitos")