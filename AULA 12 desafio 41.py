print('DESCUBRA QUAL CATEGORIA VOCÊ PERTENCE...')
a = int(input('ESCREVA SEU ANO DE NASCIMENTO::'))
atual = 2023
i = atual - a
print('<>' *20)
print('VOCÊ TEM {} ANOS'.format(i))
if i <=9:
    print('VOCÊ É UM JOGADOR MIRIM')
elif i <=14:
    print('VOCÊ É UM JOGADOR INFANTIL')
elif i <=19:
    print('VOCÊ É UM JOGADOR JUNIOR')
elif i == 25:
    print('VOCÊ É UM JOGADORE SÊNIOR')
else:
    print('VOCÊ É UM JOGADOR MASTER')
