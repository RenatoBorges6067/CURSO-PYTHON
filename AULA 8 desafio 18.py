import math
an = float(input('digire o angulo que voce desejas:'))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('O SENO DO ANGULO {:.0f} É {:.2f}'.format(an, seno))
print('O COSSENO DO ANGULO {:.0f} É {:.2f}'.format(an,cosseno))
print('O TANGENTE DO ANGULO {:.0f} É {:.2f}'.format(an,tangente))
