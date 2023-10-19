t = 50
tv = 5
tv1 = 3

m = int(input("Informe o número de tanques: "))

r = float(input("Informe o tamanho a base do tanque(m): "))

r = r / 2 

a = float(input("Informe o tamanho da altura do tanque(m): "))

i = (2 * 3.14 * r * (r + a)) * m

f = (i / tv)

p = f * t

f = round(f)

print("O total de latas é de {}" .format(f)) 

print("O valor total deu {}" .format(p))
