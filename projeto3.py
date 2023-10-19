c = float(input("informe o valor da gasolina: "))
c1 = float(input("informe o valor do álcool: "))

c2 = (c1 / c) * 100
c2 = round(c2)

print("o valor da gasolina é de", c, "e o do álcool é de", c1, "o valor da conta é de", c2,"%. Se o valor der menor que 75%, compensa abastecer no álcool")