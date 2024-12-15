tempo = int(input())

tempo2 = tempo
seg = 0
minu = 0
hour = 0

if tempo >= 0 and tempo <= 60:
    seg += tempo

if tempo > 60:
    minu += 1

print (f"{hour}:{minu}:{seg}")