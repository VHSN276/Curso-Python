nome = 'Vitor'
cont = 0
novo_nome = ''
qtde_nome = len(nome)
print(nome)
print(qtde_nome)
while cont < qtde_nome:
    novo_nome += nome[cont] + '*'
    cont+=1
print(novo_nome)