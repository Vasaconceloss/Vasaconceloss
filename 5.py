print("informe se você deseja converter km/h para mph ou mph em km: km/h_1    mph_2")
e = int(input(""))

if e == 2:
    km = float(input("Informe a velocidade em(km/h): "))

    km = km * 0.621371

    print("O valor da velocidade é de {} mph" .format(km))
elif e == 1:
    km = float(input("Informe a velocidade em(mph): "))

    km = km / 0.621371

    print("O valor da velocidade é de {} km/h" .format(km))
elif e < 1 and e > 2:
    print(EOFError)