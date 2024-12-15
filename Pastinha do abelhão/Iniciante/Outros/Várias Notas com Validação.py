while True:
    while True:
        nota1 = float(input())
        if nota1 >= 0 and nota1 <= 10:
            break
            
        else:
            print("nota invalida")

    while True:
        nota2 = float(input())
        if nota2 >= 0 and nota2 <= 10:
            break
            
        else:
            print("nota invalida")

    media = (nota1 + nota2) / 2
    print(f"media = {media:.2f}")
    while True:
        print ("novo calculo (1-sim 2-nao)")
        rep = int(input())
        if rep == 1:
            break

        elif rep == 2:
            exit ()

        else:
            continue