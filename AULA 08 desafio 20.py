import random

n1 = input('NOME DO PRIMEIRO ALUNO:')
n2 = input('NOME DO SEGUNDO ALUNO:')
n3 = input('NOME DO TERCEIRO ALUNO:')
n4 = input('NOME DO QUARTO ALUNO:')

lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ORDEM DE APRESENTAÇAO VAI SER:')
print(lista)
