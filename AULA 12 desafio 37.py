n = int(input('ESCREVA UM NUMERO INTEIRO'))
print('''ESCOLHA SUA BASE DE CONVERÇÃO!
 [1] CONVERTER PARA BINARIO
 [2] CONVERTER PARA OCTAL
 [3] CONVERTER PARA HEXADECIMAL''')
o = int(input('SUA OPÇAO'))

if o == 1:
    print('O NUMERO {} EM BINARIO VIRA {}'.format(n, bin(n)[2:]))
elif o == 2:
    print('O NUMERO {} EM OCTAL VIRA {}'.format(n, oct(n)[2:]))
elif o == 3:
    print('O NUMERO {} EM HEXADECIMAL VIRA {}'.format(n,hex(n)[2:]))
else:
    print('OPÇAO NAO EXISTENTE')
