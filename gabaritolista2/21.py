"""21. Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e 
depois informar quantas notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
- Exemplo 1: Para sacar a quantia de 256 reais, 
o programa fornece duas notas de 100, uma nota de 50, 
uma nota de 5 e uma nota de 1;
- Exemplo 2: Para sacar a quantia de 399 reais,
o programa fornece três notas de 100, uma nota de 50,
quatro notas de 10, uma nota de 5 e quatro notas de 1.

"""
try:
    print('Saque mínimo R$ 10,00 - Saque maximo R$ 600,00')
    print('Notas Disponíveis R$ 1.00\n R$ 5.00\n R$ 10.00\n R$ 50.00 \n R$ 100 reais')
    valor = int(input('Digite o valor que deseja sacar: '))
    if valor < 10 or valor > 600:
        print('Saque минimo R$ 10,00 - Saque.maxcdn R$ 600,00')
        exit    
    else:
    
   
        print(f'1Notas: {valor // 100} notas de R$ 100.00') # pega o cociente inteiro
        valor = valor % 100     # joga o resto para valor de maneira a atualizar 
        if valor != 0: # se o resto for diferente de zero ele imprime
            print(f'2Notas: {valor // 50} notas de R$ 50.00')  #valor atualiza divide por 50 imprime o inteiro
            valor = valor % 50
        if valor !=0:
            print(f'3Notas: {valor // 10} notas de R$ 10.00')
            valor = valor % 10
        if valor != 0:
            print(f'4Notas: {valor // 5} notas de R$ 5.00')
            valor = valor % 5
        if valor != 0:
            print(f'5Notas: {valor // 1} notas de R$ 1.00')
    
    
except:
    print('Digite um número inteiro')
    exit