"""
28. O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. 

Confira:

Até 5 Kg:
- File Duplo R$ 4,90 por Kg
- Alcatra R$ 5,90 por Kg
- Picanha R$ 6,90 por Kg

Acima de 5 Kg:
- File Duplo R$ 5,80 por Kg
- Alcatra R$ 6,80 por Kg
- Picanha R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos 
de carne da promoção, porém não há limites para a quantidade de carne por cliente. 
Se compra for 
feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o
total da compra.
Escreva um programa que peça o tipo e a quantidade de carne comprada pelo 
usuário e gere um
cupom fiscal, contendo as informações da compra: tipo e quantidade de carne,
preço total,
tipo de pagamento, valor do desconto e valor a pagar."""

print('Até 5 Kg:\n- File Duplo R$ 4,90 por Kg\n- Alcatra R$ 5,90 por Kg\n- Picanha R$ 6,90 por Kg\n')
print('Acima de 5 Kg:\n- File Duplo R$ 5,80 por Kg\n- Alcatra R$ 6,80 por Kg\n- Picanha R$ 7,80 por Kg\n')

tipo_carne = input('Digite o tipo de carne: ').upper()
kg_carne = float(input('Digite a quantidade de carne: '))   
pagamento = input('Digite o tipo de pagamento: [cartão tabajara -c / outro - o ]').upper()   

if kg_carne > 5:
    if tipo_carne == 'FILE DUPLO':
        vl_carne = 5.80
    elif tipo_carne == 'ALCATRA':
        vl_carne = 6.80
    elif tipo_carne == 'PICANHA':
        vl_carne = 7.80
else:
    if tipo_carne == 'FILE DUPLO':
        vl_carne = 4.90
    elif tipo_carne == 'ALCATRA':
        vl_carne = 5.90
    elif tipo_carne == 'PICANHA':
        vl_carne = 6.90

vl_total = vl_carne * kg_carne

if pagamento == 'C':
    vl_total = vl_total * 0.95

print(f'Tipo de carne: {tipo_carne}')
print(f'Quantidade de carne: {kg_carne}')
print(f'Valor total: R${vl_total:.2f}')
print(f'Tipo de pagamento: {pagamento}')
print(f'Valor do desconto: R${vl_total * 0.05:.2f}')
print(f'Valor a pagar: R${vl_total * 0.95:.2f}')