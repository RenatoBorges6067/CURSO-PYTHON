import random
print('VAMOS JOGAR JOKEMPO!')
print('1 É PEDRA ')
print('2 É TESOURA')
print('3 É PAPEL')
e = int(input('JOOOO KENN POOOOÔ'))
l = (1,2,3)
r = random.choice(l)
print('VOCE ESCOLHEU:::')

if e == 1:
    print('PEDRA')
if e == 2:
    print('TESOURA')
if e == 3:
    print('PAPEL')


print('<>' *20 )

print('Á MAQUINA ESCOLHEU:::')
if r == 1:
    print('PEDRA')
if r == 2:
    print('TESOURA')
if r == 3:
    print('PAPEL')

print('<>'*20)

print('RESULTADO:::')

if e == r:
    print('EMPATAMOS')
elif e == 1 and r == 2 or e == 2 and r == 3 or e == 3 and r == 1:
    print('VOCE GANHOU DE MIM')
else:
    print('HAHAH EU GANHEI DE VOCE')
