resp = float(input(""))
    
if resp >= 0 and resp <= 25:
    print ("Intervalo [0,25]")

elif resp > 25 and resp <= 50:
    print ("Intervalo (25,50]")

elif resp > 50 and resp <= 75:
    print ("Intervalo (50,75]")

elif resp > 75 and resp <= 100:
    print ("Intervalo (75,100]")

else:
    print ("Fora de intervalo")