b1 = float(input("informe a nota do 1° bimestre: "))
b2 = float(input("informe a nota do 2° bimestre: "))
b3 = float(input("informe a nota do 3° bimestre: "))
b4 = float(input("informe a nota do 4° bimestre: "))

m = (b1 + b2 + b3 + b4) / 40

if (m >= 6 and m <= 7):
    print("O seu conceito é B. Parabéns, você foi aprovado")
elif (m < 6):
    print("O seu conceito é C. Estude mais, você reprovou ;-;")
else:
    print("O seu conceito é A. Parabéns, você foi aprovado")


