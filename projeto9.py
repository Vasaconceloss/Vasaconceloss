c = 0
c2 = 0
for n in range(1, 6):
    t = float(input("informe o {}° valor: " .format(n)))
    if t > 0:
        print("o valor {} é positivo" .format(t))
        c = c + 1
    else:
        print("o valor {} é negativo" .format(t))
        c2 = c2 + 1
print(" {} dos valores são positivos e {} dos valores são negativos" .format(c, c2))
