n1 = input("Digite um valor: ")
n2 = input("Digite outro valor: ")
valor1 = int(n1)
valor2 = int(n2)
if valor1 > valor2:
    print(f"{valor1=} é maior do que {valor2=}")
elif valor2 > valor1:
    print(f"{valor2=} é maior do que {valor1=}")
else:
    print(f"{valor1=} é igual a {valor2=}")