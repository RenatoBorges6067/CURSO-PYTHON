import random
import time
print('A MAQUINA ESCOLHEU UM NUMERO DE 1 A 5!')
n = random.randint(0, 5)
a = int(input('TENTE ACERTAR O NUMERO QUE A MAQUINA ESCOLHEU!'))
print('PROCESSANDO..................')
time.sleep(3)
if a == n:
    print('VOCE ACERTOU... A MAQUINA TAMBEM ESCOLHEU O NUMERO {}..'.format(n))
else:
    print('VOCE ERROU... O NUMERO QUE A MAQUINA ESCOLHEU FOI O {}..'.format(n))
