entrada = input("Escolha uma opção:\n[E]Entrar\n[S]Sair\n")
if entrada == 'E' or entrada == 'e':
    senha_permitida = "123456"
    user_permitido = "vitor"
    senha = input("Senha: ")
    user = input("User: ")
    if senha == senha_permitida and user == user_permitido:
        print("Login realizado com sucesso.\nEntrando no sistema...")
    else:
        print("Login incorreto")
elif entrada == 'S' or entrada == 's':
    print("Saindo do Sistema...")
else:
    print("Opção Incorreta. Saindo do Sistema...")
print("Obrigado! Volte sempre!")