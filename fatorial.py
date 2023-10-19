l = int
while (l < 0): 
    n = int(input("insira o número que deja o fatorial: "))
    num = 1
    f = n
    l = 0
    while num < n:
        f = f * num
        num = num + 1

    print("seu fatorial é {} " .format(f))
    print("0-não")
    print("1-sim")
    l = int(input("informe se você deseja continuar: "))
print("fim")
