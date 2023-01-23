numero = int(input("ESCREVA UM NUMERO ATÉ 9999"))
u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
m = numero // 1000 % 10
print('unidade:{}'.format(u))
print('DEZENA:{}'.format(d))
print('CENTENA:{}'.format(c))
print('MILHAR:{}'.format(m))
