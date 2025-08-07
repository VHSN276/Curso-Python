nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")
if(nome != '' and idade != ''):

    print(f"Seu nome é {nome}\n")
    print(f"Seu nome invertido é {nome[::-1]}\n")
    if(' ' in nome):
        print("Seu nome tem espaços\n")
    else:
        print("Seu nome não tem espaços\n")
    print(f'Seu nome tem {len(nome)} letras')
    print(f'A primeira letra do seu nome é {nome[0]}')
    print(f'A ultima letra do seu nome é {nome[-1]}')
else:
    print("Desculpe, você deixou campos vazios")