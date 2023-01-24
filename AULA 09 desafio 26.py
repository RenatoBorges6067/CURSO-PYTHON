f = str(input('ESCREVA FRASE')).strip()
print('NA SUA FRASE APARECE {}As.'.format(f.upper().count('A')))
print('O PRIMEIRO A SE ENCONTRA NO {}'.format(f.upper().find('A')+1))
print('O ULTIMO A SE ENCONTRA NO {}'.format(f.upper().rfind('A')+1))
