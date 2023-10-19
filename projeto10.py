n = 1
c = 0
c2 = 0

while n < 6:
    m = int(input("informe {}° valor: " .format(n)))
    n = n + 1
    if m %2:
        c = c + 1
    else:
        c2 = c2 + 1
print("{} número(s) são par e {} são ímpares" .format(c2, c))  