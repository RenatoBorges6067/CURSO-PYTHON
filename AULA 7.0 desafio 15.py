dias = int(input('QUANTOS DIAS VOCE RODOU COM O CARRO?'))
KM = float(input('QUANTOS KM VOCE RODOU COM O CARRO?'))
d = dias * 60
k = KM * 0.15
print('TOTAL A PAGAR É R${:.2f}'.format(d + k))
