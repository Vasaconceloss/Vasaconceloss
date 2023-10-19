l = input("informe o 1° valor do triângulo (base): ")
l1 = input("informe o 2° valor do triângulo: ")
l2 = input("informe o 3° valor do triângulo: ")
h = input("informe a altura do triângulo:")

if l != l1 and l != l2:
    print("O triângulo é um triângulo escaleno")
elif l == l1 and l != l2:
    print("O triângulo é um triângulo isósceles")
elif l == l2 and l != l1:
    print("O triângulo é um triângulo isósceles")
elif l1 != l and l != l2:
    print("O triângulo é um triângulo escaleno")
elif l1 == l and l != l2:
    print("O triângulo é um triângulo isósceles")
elif l1 == l2 and l1 != l:
    print("O triângulo é um triângulo isósceles")
elif l1 != l and l1 != l2:
    print("O triângulo é um triângulo escaleno")
elif l2 == l and l2 != l1:
    print("O triângulo é um triângulo isósceles")
elif l2 == l1 and l2 != l:
    print("O triângulo é um triângulo isósceles")

a = l * h / 2

print("a área do triângulo é de {}" .format(a))
