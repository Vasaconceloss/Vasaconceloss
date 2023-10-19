h = int(input("informe a tábuada que você deseja: "))
a = int(input("informe até qual núnmero você deseja fazer a tabuáda: "))
a = a + 1

for n in range (1, a):
    l = h * n
    print(h, "x", n, "=", l)