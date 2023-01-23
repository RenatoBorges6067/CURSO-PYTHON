n = str(input('ESCREVA SEU NOME:')).strip()
nome = n.split()
print('SEU PRIMEIRO NOME É {}'.format(nome[0]))
print('E SEU ULTIMO NOME É {}'.format(nome[len(nome)-1]))
