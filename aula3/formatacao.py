# imc - índice massa corporea
# imc = peso / altura ** 2
# imc = peso / (altura * altura)
# ENTRADA
nome = 'lucas'
altura = 1.71
peso = 80
# PROCESSAMENTO
imc = peso / altura**2

print(nome,'tem',altura,'de altura','pesa',peso,' seu imc é =',imc)
#f-strings
print(f'{nome} tem{altura} de altura\n pesa{peso} e seu imc é = {imc:.2f}')