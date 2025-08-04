"""8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês."""

valor_hora = float(input('Informe o valor da hora trabalhada: '))
quantidade_horas = int(input('Informe a quantidade de horas trabalhadas por dia: '))
salario = valor_hora * quantidade_horas
print(f'Seu salario mensal eh de R${salario:.2f}')