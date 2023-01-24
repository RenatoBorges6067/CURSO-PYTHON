import datetime
a = int(input('ESCREVA UM ANO E DESCUBRA SE ELE É BISSEXTO?'))
if a == 0:
    a = datetime.date.today().year
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print('O ANO {}, É UM ANO BISSEXTO!'.format(a))
else:
    print('O ANO {}, NÃO É UM ANO BISSEXTO!'.format(a))
