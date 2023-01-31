peso = float(input('QUAL O SEU PESO ?'))
altura = float(input('QUAL Á SUA ALTURA ?'))

imc = peso /(altura ** 2)
print('SEU IMC É {:.2f}'.format(imc))

if imc <= 18.5:
    print('ABAIXO DO PESO')
elif imc <=25:
    print('PESO IDEAL')
elif imc <= 30:
    print('SOBREPESO')
elif imc <= 40:
    print('OBESIDADE')
else:
    print('OBESIDADE MORBIDA')
