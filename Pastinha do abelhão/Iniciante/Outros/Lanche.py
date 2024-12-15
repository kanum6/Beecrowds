choise = input("")
code, quant = choise.split(" ")

quant = int(quant)
code = int(code)
dg = 4
sa = 4.5
ba = 5
to = 2
re = 1.5

if code == 1:
   print (f"Total: R$ {quant * dg:.2f}")

if code == 2:
   print (f"Total: R$ {quant * sa:.2f}")

if code == 3:
   print (f"Total: R$ {quant * ba:.2f}")

if code == 4:
    print (f"Total: R$ {quant * to:.2f}")

if code == 5:
    print (f"Total: R$ {quant * re:.2f}")

