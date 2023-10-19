n = str(input("insira seu nome: "))
i = int(input("insira sua idade: "))
h = float(input("informe sua altura em (m): "))
p = float(input("insira seu peso: "))

imc = p/(h*h)

print("olá {} sua idade é de {}, com a altura de {}m e peso de {}kg. Seu imc é de aproximadamente{}" .format(n, i, h, p, imc))