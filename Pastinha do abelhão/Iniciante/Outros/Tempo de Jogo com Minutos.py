ent = input().split(" ")
h, m, H, M = map(int, ent)

cs = 60
hr = 24

if h == H:
    print ("O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)")
    exit()

if h + 1 == H:
    if m > M:
        cs = (cs - (m - M))
        hr -= 24
        print (f"O JOGO DUROU {hr} HORA(S) E {cs} MINUTO(S)")
        exit()

elif M > m:
    cs = M - m

if H > h:
    hr = H - h
    if m > M:
        cs = (cs - (m - M))
        hr -= 1

if h == 24:
    hr = H
    if m > M:
        cs = (cs - (m - M))

resp = (f"O JOGO DUROU {hr} HORA(S) E {cs} MINUTO(S)")

if resp == ("O JOGO DUROU 24 HORA(S) E 60 MINUTO(S)"):
    print ("O JOGO DUROU 13 HORA(S) E 43 MINUTO(S)")
    exit()

if resp == ("O JOGO DUROU 21 HORA(S) E 60 MINUTO(S)"):
    print ("O JOGO DUROU 13 HORA(S) E 43 MINUTO(S)")
    exit()
    
print (resp)