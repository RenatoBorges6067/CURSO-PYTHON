print('{:=^40}'.format('LOJAS RENATOVISK'))
v = float(input('QUAL O VALOR DO PRODUTO?'))
print ('QUAL Á FORMA DE PAGAMENTO ?')
p = int(input('''
1 para a vista  
2 para cartao de debito 
3 para 2x no cartao de credito 
4 para 3x OU MAIS NO cartao de credito '''))

print('<>' * 20)
if p ==1:
    d = v * 10 / 100
    vf = v - d
    print('COM DESCONTO DE 10% PAGANDO A VISTA VOCE VAI PAGAR R${:.0f}'.format(vf))
elif p == 2:
    d = v * 5 / 100
    vf = v - d
    print('COM O DESCONTO DE 5% NO CARTAO DE DEBITO VOCE VAI PAGAR R${:.0f}'.format(vf))
elif p ==3:
    print('COM A COMPRA NO CARTAO DE CREDITO DE 2x VOCE VAI PAGAR O PREÇO NORMAL R${:.0f}'.format(v))
elif p == 4:
    par = int(input('QUANTAS PARCELAS?'))

    d = v * 20 /100
    vf = v + d
    pres = vf / par
    print('SUA COMPRA DE R${} FOI PARA R${} NO CARTAO DE CREDITO, AS PARCELAS VÃO SER DE R${:.0f} '.format(v,vf,pres))
else:
    print('NAO EXISTE ESSA OPÇAO DE COMPRA>')
