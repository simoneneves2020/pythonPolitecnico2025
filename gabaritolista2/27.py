"""27. Uma fruteira está vendendo frutas com a seguinte tabela de preços:

Até 5 Kg:
- Morango R$ 2,50 por Kg 
- Maçã R$ 1,80 por Kg

Acima de 5 Kg:
- Morango R$ 2,20 por Kg

- Maçã R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou 
o valor total da compra ultrapassar R$ 25,00, receberá 
ainda um desconto de 10% sobre este total. 
Escreva um algoritmo para ler a quantidade (em Kg) de morangos e
a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.
"""
vl_morango = 2.50
vl_maca = 1.80

kg_morango = float(input('Quantidade de morangos: '))
kg_maca = float(input('Quantidade de maçã: '))

vl_total = (kg_morango * vl_morango) + (kg_maca * vl_maca)  
print(f'Valor total: R${vl_total:.2f}') 

if (kg_morango + kg_maca) > 8 or vl_total > 25:
    vl_total = vl_total * 0.9
    print(f'Valor total com desconto: R${vl_total:.2f}')