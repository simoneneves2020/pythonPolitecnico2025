
# Entrada: área a ser pintada
import math


area = float(input("Digite o tamanho da área a ser pintada (em m²): "))

# Acrescenta 10% de folga
area_com_folga = area * 1.1

# Quantidade de litros de tinta necessária
litros_necessarios = area_com_folga / 6

# Preços
preco_lata = 80.00
preco_galao = 25.00

# Estratégia 1: Apenas latas de 18L
qtd_latas = math.ceil(litros_necessarios / 18)
custo_latas = qtd_latas * preco_lata

# Estratégia 2: Apenas galões de 3,6L
qtd_galoes = math.ceil(litros_necessarios / 3.6)
custo_galoes = qtd_galoes * preco_galao

# Estratégia 3: Mistura
qtd_latas_mixto = int(litros_necessarios / 18)
litros_restantes = litros_necessarios - (qtd_latas_mixto * 18)
qtd_galoes_mixto = math.ceil(litros_restantes / 3.6)
custo_misto = (qtd_latas_mixto * preco_lata) + (qtd_galoes_mixto * preco_galao)

# Resultado
print("\n== Opções de Compra ==")
print(f"1) Apenas latas de 18L: {qtd_latas} lata(s) - R$ {custo_latas:.2f}")
print(f"2) Apenas galões de 3,6L: {qtd_galoes} galão(ões) - R$ {custo_galoes:.2f}")
print(f"3) Mistura: {qtd_latas_mixto} lata(s) e {qtd_galoes_mixto} galão(ões) - R$ {custo_misto:.2f}")