s = float(input('QUAL É O SEU SALÁRIO?'))
a = (s * 10) / 100
am = (s * 15) / 100
if s<= 1250:
    print('O NOVO SALARIO É {}'.format(am + s))
else:
    print('O SEU NOVO SALARIO É {}'.format(a + s))
