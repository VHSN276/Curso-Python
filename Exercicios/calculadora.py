while True:
    n1 = input("Digite um número: ")
    n2 = input("Digite outro número: ")
    operador = input("Digite um operador (+-/*)")
    n1_int = 0
    n2_int = 0
    numeros_validos = None

    try:
        n1_int = float(n1)
        n2_int = float(n2)
        numeros_validos = True
    except:
        numeros_validos = None

    operadores_permitidos = '+-/*'
    if operador not in operadores_permitidos:
        print("Operador Inválido")
        continue
    if len(operador) > 1:
        print("Digite apenas um operador")
        continue
    if numeros_validos is None:
        print("Numero Inválido")
        continue
    print("Realizando sua operação: ")
    if(operador == '+'):
        print(n1_int + n2_int)
    elif (operador == '-'):
        print(n1_int - n2_int)
    elif (operador == '/'):
        print(n1_int / n2_int)
    elif (operador == '*'):
        print(n1_int * n2_int)
    sair = input("Quer sair? [s]sim: ").lower().startswith('s')
    if sair:
        break
