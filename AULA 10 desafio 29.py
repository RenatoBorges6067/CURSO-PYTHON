v = float(input('QUAL ERA A SUA VELOCIDADE?'))
max = 80
multa = (v - 80) * 7
if v <= max:
    print('VOCE ESTA DIRIGINDO Á {}KM, VELOCIDADE PERMITIDA!!'.format(v))
else:
    print('VOCE ESTA DIRIGINDO Á {}KM,ACIMA DO PERMITIDO! VOCÊ FOI MULTADO EM R${}.'.format(v,multa))
    
