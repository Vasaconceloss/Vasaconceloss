n = str(input("Informe o seu nome: "))
p = float(input("Informe o seu peso: "))
a = float(input("Informe a sua altura: "))

imc = p/(a**2)

if (imc <= 18.5):
    print("{} você está abaixo do peso" .format(n))
elif (imc >= 25 and imc <= 29.99):
    print("{} você está em um peso normal" .format(n))
elif (imc >= 30 and imc <= 34.99):
    print("{} você está em obesidade grau 1" .format(n))
elif (imc >= 35 and imc <= 39.99):
    print("{} você está em obesidade grau 2" .format(n))
else:
    print("{} você está em obesidade grau 3 ;-;" .format(n))
