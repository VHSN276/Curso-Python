# if / elif / else
# se / se não se / se não
escolha = input('Você quer "Entrar" ou "Sair"? \n')
if escolha == 'Entrar':
    print("Você entrou do sistema")
elif escolha == 'Sair':
    print("Você saiu do sistema")
else:
    print('Você não digitou nem "Entrar" e nem "Sair"')
print("Fora dos blocos")