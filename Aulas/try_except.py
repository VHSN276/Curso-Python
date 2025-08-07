"""
Try -> tentar executar o code
Except -> ocorreu algum erro ao tentar executar
"""

numero_str = input("Digite um numero: ")
try:
    print(f"String: {numero_str}")
    numero_float = float(numero_str)
    print(f'Numero float: {numero_float}')
    print(f"o dobro de {numero_float} é {numero_float*2}")
except:
    print("Isso não é um numero")