n = input("Informe o nome do funcionário: ")
s = float(input("informe o salário do usuário: "))
r = float(input("informe o valor do reajuste do salário em(%): "))

s = s + (s * (r / 100))

print("O valor do salário do(a) {} com o reajuste é de {}" .format(n, s))