"""8. Faça um programa que pergunte o preço de três produtos e 
informe qual produto você deve comprar,
sabendo que a decisão é sempre pelo mais barato."""

preco1 = float(input('Digite o preco do primeiro produto: '))
preco2 = float(input('Digite o preco do segundo produto: '))
preco3 = float(input('Digite o preco do terceiro produto: '))

if preco1 < preco2 and preco1 < preco3:
    print(f'{preco1} é o preco mais barato.')
elif preco2 < preco1 and preco2 < preco3:
    print(f'{preco2} é o preco mais barato.')
else:
    print(f'{preco3} é o preco mais barato.')
    

