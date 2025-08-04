"""16. Faça um programa para uma loja de tintas. O programa deverá pedir
o tamanho em metros quadrados da área a ser pintada. 
Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
quadrados e que a tinta é
vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a 
quantidades de latas de tinta a serem compradas e o preço total."""

metros = float(input('Informe o tamanho em metros quadrados da area a ser pintada: '))
# estou dividindo a quantide de metros por 3 para saber quantos litros de tinta irei usar
litros = metros / 3.0
# ja sei quantos litros de tinta irei usar, agora eu quero saber 
# quantas latas de tinta irei usar
#latas = round((litros / 18.0)) ## inicio de função no python, sem a função round ele 
latas = litros / 18.0
#iria  trazer valor com dizima periódica e fazendo arredondamento para baixo.
custo = latas * 80.00  
# no custo estou multiplicando o valor das latas pela quantidade de latas 
print(f'Quantidade a ser usada: {latas:} lata(s) R$ {custo:.2f}')    
