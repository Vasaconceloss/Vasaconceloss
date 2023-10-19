n = int(input("informe o número do fatorial que você deseja: "))
f = n

for num in range(1, n):
   f = f * num
   
print("o fatorial de {} é igual a: {} " .format(n, f))