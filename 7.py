c = float(input("Informe o custo de fábrica do carro: "))
c = 0.45 * c + c
c = 0.28 * c + c
c1 = float(input("Informe o custo de fábrica do carro: "))
c1 = 0.45 * c1 + c1
c1 = 0.28 * c1 + c1
c2 = float(input("Informe o custo de fábrica do carro: "))
c2 = 0.45 * c2 + c2
c2 = 0.28 * c2 + c2

if (c > c1 and c > c2):
    print("O 1° carro tem o maior valor: R${}" .format(c))
elif (c < c1 and c < c2):
    print("O 1° carro tem o menor valor: R${}" .format(c))
else:
     print("O preço é médio")
if(c1 > c and c1 > c2):
         print("O 2° carro tem o maior valor: R${}" .format(c1))
elif (c1 < c and c1 < c2):
    print("O 2° carro tem o menor valor: R${}" .format(c1))
else:
     print("O preço é médio")
if(c2 > c1 and c2 > c):
    print("O 3° carro tem o maior valor: R${}" .format(c2))
elif (c2 < c1 and c2 < c):
    print("O 3° carro tem o menor valor: R${}" .format(c2)) 
else:
    print("O preço é médio")
