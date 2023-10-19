h = int(input("informe a tábuada que você deseja: "))
a = int(input("informe até qual número deseja a tabuada: "))
n = 0

while n < a:
    n = n + 1
    r = h * n
    print("{} x {} = {}" .format(h, n, r))
