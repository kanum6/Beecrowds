din = float(input(""))

not100 = 0
not50 = 0
not20 = 0
not10 = 0
not5 = 0
not2 = 0

mo1 = 0
mo05 = 0
mo025 = 0
mo010 = 0
mo005 = 0
mo001 = 0

while din >= 100:
    not100 += 1
    din -= 100

while din >= 50 and din < 100:
    not50 += 1
    din -= 50

while din >= 20 and din < 50:
    not20 += 1
    din -= 20

while din >= 10 and din < 20:
    not10 += 1
    din -= 10

while din >= 5 and din < 10:
    not5 += 1
    din -= 5

while din >= 2 and din < 5:
    not2 += 1
    din -= 2

while din >= 1 and din < 2:
    mo1 += 1
    din -= 1

while din >= 0.50 and din < 1:
    mo05 += 1
    din -= 0.50

while din >= 0.25 and din < 0.50:
    mo025 += 1
    din -= 0.25

while din >= 0.10 and din < 0.25:
    mo010 += 1
    din -= 0.10

while din >= 0.05 and din < 0.10:
    mo005 += 1
    din -= 0.05

while din > 0.001 and din < 0.05:
    mo001 += 1
    din -= 0.01

print (f"NOTAS:\n{not100} nota(s) de R$ 100.00\n{not50} nota(s) de R$ 50.00\n{not20} nota(s) de R$ 20.00\n{not10} nota(s) de R$ 10.00\n{not5} nota(s) de R$ 5.00\n{not2} nota(s) de R$ 2.00\nMOEDAS:\n{mo1} moeda(s) de R$ 1.00\n{mo05} moeda(s) de R$ 0.50\n{mo025} moeda(s) de R$ 0.25\n{mo010} moeda(s) de R$ 0.10\n{mo005} moeda(s) de R$ 0.05\n{mo001} moeda(s) de R$ 0.01")