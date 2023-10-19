d = float(input("Informe a distância(km): "))
g = float(input("Informe o valor da gasolina: "))
c = float(input("Informe o valor do consumo: "))

t = (d / c)* g
t = round(t)

print("O total gasto será aproximadamente de {}" .format(t))
