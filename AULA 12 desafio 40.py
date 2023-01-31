print('ESCREVA DUAS NOTAS DE UM ALUNO')
n1 = float(input('1° NOTA:'))
n2 = float(input('2° NOTA:'))

media = (n1 + n2) / 2

if media < 5:
    print('VOCÊ FOI REPROVADO!')
elif media < 7  :
    print('VOCÊ FICOU DE RECUPERAÇÃO')
else:
    print('VOCÊ FOI APROVADO')
