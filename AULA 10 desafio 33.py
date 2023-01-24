print("ESCREVA 3 NUMEROS!")
n1 = int(input('1°:'))
n2 = int(input('2°:'))
n3 = int(input('3°:'))

if n1==n2 and n1==n3:
    print('TODOS OS NUMEROS SAO IGUAIS')
if n1==n2 and n1>n3:
    print('OS NUMEROS DAS COLUNAS 1°:[{}] E 2°:[{}] SAO MAIORES QUE O NUMERO DA COLUNA 3°:{}'.format(n1,n2,n3))
if n1==n3 and n1>n2:
    print('OS NUMEROS DAS COLUNAS 1°:[{}] E 3°:[{}] SAO MAIORES QUE O NUMERO DA COLUNA 2°:{}'.format(n1,n3,n2))
if n2==n3 and n2>n1:
    print('OS NUMEROS DAS COLUNAS 2°[{}] e 3°:[{}] SAO MAIORES QUE O NUMERO DA COLUNA 1°:{}'.format(n2,n3,n1))
if n1>n2 and n1>n3:
    print('O NUMERO DA COLUNA 1°:[{}] É O MAIOR NUMERO!'.format(n1))
if n2>n1 and n2>n3:
    print('O NUMERO DA COLUNA 2°:[{}] É O MAIOR NUMERO!'.format(n2))
if n3>n1 and n3>n2:
    print('O NUMERO DA COLUNA 3°:[{}] É O MAIOR NUMERO!'.format(n3))
if n1==n2 and n1<n3:
    print('OS NUMEROS DAS COLUNAS 1°:[{}] E 2°:{} SAO MENORES QUE O NUMERO DA COLUNA 3°:{}'.format(n1,n2,n3))
if n1==n3 and n1<n2:
    print('OS NUMEROS DAS COLUNAS 1°:[{}] E 3°:{} SAO MENORES QUE O NUMERO DA COLUNA 2°:{}'.format(n1,n3,n2))
if n2==n3 and n2<n1:
    print('OS NUMEROS DAS COLUNAS 2°:[{}] e 3°:[{}] SAO MENORES QUE O NUMERO DA COLUNA 1°:{}'.format(n2,n3,n1))
if n1<n2 and n1<n3:
    print('O NUMERO DA COLUNA 1°:[{}] É O MENOR NUMERO!'.format(n1))
if n2<n1 and n2<n3:
    print('O NUMERO DA COLUNA 2°:[{}] É O MENOR NUMERO!'.format(n2))
if n3<n1 and n3<n2:
    print('O NUMERO DA COLUNA 3°:[{}] É O MENOR NUMERO!'.format(n3))
