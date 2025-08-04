"""15. Faça um Programa que pergunte 
quanto você ganha por hora e o 
número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são 
descontados 11% para o Imposto de Renda,
8% para o INSS e 
5% para o sindicato, faça um programa que nos dê:
- salário bruto.
- quanto pagou ao INSS.
- quanto pagou ao sindicato.
- o salário líquido.
- calcule os descontos e o salário líquido, conforme a tabela abaixo:

Salário Bruto : R$
IR (11%) : R$
INSS (8%) : R$
Sindicato ( 5%) : R$
Salário Liquido : R$
Obs.: Salário Bruto - Descontos = Salário Líquido."""

hora_trabalhada = float(input('Informe o valor da hora trabalhada: '))
valor_hora = float(input('Informe o valor da hora trabalhada: '))   

salario_bruto = hora_trabalhada * valor_hora
ir = salario_bruto * 0.11
inss = salario_bruto * 0.08
sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - ir - inss - sindicato

print(f'Salário bruto: R$ {salario_bruto:.2f}\n'
    f'IR: R$ {ir:.2f}\n'
    f'INSS: R$ {inss:.2f}\n'    
    f'Sindicato: R$ {sindicato:.2f}\n'
    f'Salário Líquido: R$ {salario_liquido:.2f}')       
 