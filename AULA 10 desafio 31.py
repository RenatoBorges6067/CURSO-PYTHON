v = int(input('QUAL A DiSTANCIA PERCORRIDA NA SUA VIAGEM?'))
m = v * 0.50
l = v * 0.45
if v <= 200:
    print('SUA VIAGEM DE {}KM A PASSAGEM CUSTARÁ R${}'.format(v,m))
else:
    print('SUA VIAGEM DE {}KM Á PASSAGEM CUSTARÁ R${}'.format(v,l))
