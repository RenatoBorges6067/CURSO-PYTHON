import random
print('SORTEIO DE QUAL ALUNO VAI APAGAR O QUADRO:')
n1 = input('NOME DO PRIMEIRO ALUNO:')
n2 = input('NOME DO SEGUNDO ALUNO:')
n3 = input('NOME DO TERCEIRO ALUNO:')
n4 = input('NOME DO QUARTO ALUNO:')

lista = [n1, n2, n3, n4]

escolhido = random.choice(lista)

print('O ALUNO ESCOLHIDO PARA APAGAR O QUADRO FOI {}'.format(escolhido))
