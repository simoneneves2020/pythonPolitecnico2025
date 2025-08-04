""" 17. Faça um Programa para uma loja de tintas. 
O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e 
que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em 
galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos 
preços em 3 situações:
- comprar apenas latas de 18 litros;
- comprar apenas galões de 3,6 litros;
- misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e 
sempre arredonde os valores para cima, isto é, considere latas cheias."""

import math
# esta biblioteca dará suporte a funções matemáticas

metros = int(input('Informe o tamanho em metros quadrados da area a ser pintada: '))
metros_com_folga = metros * 1.1
litros = metros_com_folga/ 6.0 # quantos litros será necessario
latas = math.ceil(litros / 18.0) # quantas latas serão necessarias        
custo = latas * 80.00 # custo das latas
galoes = math.ceil(litros / 3.6) # quantos galões serão necessarios
custo_galoes = galoes * 25.00 # custo dos galões
custo_total = custo + custo_galoes # custo total das latas e galões

print(f'Quantidade a ser usada: {latas:.2f} lata(s) R$ {custo:.2f}')
print(f'Quantidade a ser usada: {galoes:.2f} galão(oes) R$ {custo_galoes:.2f}')    


# Estratégia 3: Mistura
qtd_ = int(litros_necessarios / 18)
litros_restantes = litros_necessarios - (qtd_latas_mixto * 18)
qtd_galoes_mixto = math.ceil(litros_restantes / 3.6)
custo_misto = (qtd_latas_mixto * preco_lata) + (qtd_galoes_mixto * preco_galao)

# Resultado
print("\n== Opções de Compra ==")
print(f"1) Apenas latas de 18L: {qtd_latas} lata(s) - R$ {custo_latas:.2f}")
print(f"2) Apenas galões de 3,6L: {qtd_galoes} galão(ões) - R$ {custo_galoes:.2f}")
print(f"3) Mistura: {qtd_latas_mixto} lata(s) e {qtd_galoes_mixto} galão(ões) - R$ {custo_misto:.2f}")