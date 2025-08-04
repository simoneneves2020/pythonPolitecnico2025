"""
17. Faça um Programa que peça um número correspondente 
a um determinado ano e em seguida informe se este ano é ou não bissexto.

Regras para um ano ser bissexto:
O ano deve ser divisível por 4
E
ano %
Não pode ser divisível por 100, exceto se também for divisível por 400
"""
ano = int(input('Digite um ano: '))

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'{ano} é bissexto')
        else:
            print(f'{ano} não é bissexto')
    else:
        print(f'{ano} é bissexto')
else:
    print(f'{ano} não é bissexto')
    
"""ano = int(input("Informe um ano: "))

if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"{ano} é um ano bissexto.")
else:
    print(f"{ano} não é um ano bissexto.")"""