print ('BEM VINDO AO MINHA CASA MINHA VIDA')
print ('ME DÊ OS SEUS DADOS')
nome = str(input('QUAL O SEU NOME ?'))
casa = float(input('QUAL O VALOR DA CASA?'))
salario = float(input('QUAL O SEU SALARIO'))
anos= int(input('EM QUANTOS ANOS PRETENDE PAGAR ESSA CASA?'))


print('>-'  * 20  )
mes = anos * 12
s = (salario * 30) / 100
mensal = casa / mes




print('VALOR DA CASA R${:.2f}'.format(casa))
print('30% DO SALARIO DE R${:.2f} É R${:.2f}'.format(salario,s))
print('VALOR MENSAL DA CASA É R${:.2f}'.format(mensal))
print('TEMPO À PAGAR {} ANO(s) É IGUAL À {} MESES '.format(anos , mes))


print('>-' *20 )
if  mensal >= s :
    print('ENTÃO SENHOR(a) {}, SEU EMPRESTIMO NÃO PODE SER APROVADO, PORQUE VOCÊ EXCEDEU 30% DO SEU SALARIO QUE É R${:.2f}'.format(nome,s))
else:
    print('SENHOR(a) {}, SEU EMPRESTIMO FOI APROVADO. VOCÊ ATENDEU A TODAS EXIGÊNCIAS'.format(nome))
