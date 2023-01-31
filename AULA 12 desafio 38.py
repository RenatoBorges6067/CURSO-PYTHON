print ('ESCREVA DOIS NUMEROS INTEIROS:::')
n1 = int(input('PRIMEIRO NUMERO::'))
n2 = int(input('SEGUNDO NUMERO::'))

if n1 == n2:
    print ('OS DOIS NUMEROS SÃO IGUAIS>>>')
elif n1 > n2 :
    print('O PRIMEIRO NUMERO {} É MAIOR QUE O SEGUNDO NUMERO {} '.format(n1,n2))
else:
    print('O SEGUNDO NUMERO {} É MAIOR QUE O PRIMEIRO NUMERO {}'.format(n2,n1))
