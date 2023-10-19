n = int(input("informe um número de (0 a 9): "))

if n == 0:
    print("zero")
elif n == 1:
    print("um")
elif n == 2:
    print("dois")
elif n == 3:
    print("trêis")
elif n == 4:
    print("quatro")
elif n == 5:
    print("cinco")
elif n == 6:
    print("seis")
elif n == 7:
    print("sete")
elif n == 8:
    print("oito")
elif n == 9:
    print("nove")
elif n < 0 and n > 9:
    print(EOFError)