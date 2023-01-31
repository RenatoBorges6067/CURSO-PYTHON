a = int(input('QUAL O SEU ANO DE NASCIMENTO?'))

atual = 2023
i = atual - a



if i <16:
    e = 17 - i
    print('VOCÊ AINDA VAI SE ALISTAR AO SERVIÇO MILITAR!VOCÊ TEM {} ANOS E FALTA {} ANO(s) PARA VOCÊ SE PODER SE ALISTAR'.format(i,e))

elif i == 16:
    print('VOCÊ TEM {} ANOS, FALTA ALGUN(s) MES(es) PARA PODER ALISTAR!'.format(i))

elif i > 18:
    e = i - 18
    print('VOCÊ TEM {} ANOS E JA PASSOU DO PRAZO DE {} ANO(s) PARA SE ALISTAR!'.format(i,e))

elif i == 18:
    print('VOCÊ TEM {} ANOS, FALTA ALGUN(s) MES(es) PARA SE ALISTAR!'.format(i))

else:
    e = 18 - i
    print('JA ESTÁ NA HORA DE SE ALISTAR AO SERVIÇO MILITAR! VOCÊ TEM {} ANOS E FALTA S{} ANO(s) PARA TERMINAR O TEMPO DE SE ALISTAR'.format(i,e))
