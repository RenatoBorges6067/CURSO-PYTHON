print('ESCREVA 3 RETAS')
r1 = float(input('PRIMEIRA RETA'))
r2 = float(input('SEGUNDA RETA'))
r3 = float(input('TERCEIRA RETA'))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('AS RETAS ACIMA PODEM FORMAR UM TRIANGULO')
else:
    print('AS RETAS ACIMA NAO PODEM FORMAR UM TRIANGULO')

if r1 == r2 and r1 == r3:
    print('ESSE TRIANGULO É EQUILÁTERO')
elif r1 == r2 or r1 == r3 or r2 == r3:
    print('TRIANGULO ISÓCELES')
else:
    print('TRIANGULO ESCALENO')
