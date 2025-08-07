"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

n1 = input("Digite um numero inteiro: ")

try:
    int_n1 =int(n1)
    if(int_n1%2 == 0):
        print("O numero é Par")
    else:
        print("O numero é Impar")
except:
    print("Não é um numero")


