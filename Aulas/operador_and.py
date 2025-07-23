entrada = input("Escolha uma opção:\n[E]Entrar\n[S]Sair\n")
if entrada == 'E':
    senha_permitida = "123456"
    senha = input("Senha: ")
    if senha == senha_permitida:
        print("Senha correta.\nEntrando no sistema...")
    else:
        print("Senha incorreta")
elif entrada == 'S':
    print("Saindo do Sistema...")
else:
    print("Opção Incorreta. Saindo do Sistema...")
print("Obrigado! Volte sempre!")