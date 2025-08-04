"""

explicando o split
""" 

data = input('Insira a data [dd/mm/aaaa]: ')

dt = data.split('/')
dia = dt[0]
mes = dt[1]
ano = dt[2]

if not dia.isdigit() or not mes.isdigit() or not ano.isdigit():
    print('Formato inválido. Use dd/mm/aaaa com números inteiros.')
    exit() # Força o programa a parar

dia = int(dia)
mes = int(mes)
ano = int(ano)

if dia < 1 or dia > 31:
    print('Dia inválido.')
    exit()

if mes < 1 or mes > 12:    
    print('Mês inválido.')
    exit()      

    print('Data inválida.')
else:
    print('Data válida.')   