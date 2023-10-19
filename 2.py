n = str(input("Informe o nome do vendedor: "))
s = float(input("Informe o salário do vendedor: "))
v = int(input("informe o número de vendas que o vendedor efetuou: "))

sf = s * v * 0.15 + s

print("O salário de(a) {} é de R$:{} " .format(n, sf))