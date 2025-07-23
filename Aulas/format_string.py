a = 'A'
b = 'B'
c = 2.2

#padrão
print('a={}\nb={}\nc={:.3f}'.format(a,b,c))
#usando indices
print('a={0}\nb={1}\nc={2:.3f}\nb={1}'.format(a,b,c))
#nomeando variaveis
print('a={nome1}\nb={nome2}\nc={nome3:.3f}\nb={nome2}'.format(nome1=a,nome2=b,nome3=c))