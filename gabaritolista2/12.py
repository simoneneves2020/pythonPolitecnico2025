"""12. Faça um programa para o cálculo de uma folha de pagamento, sabendo 
que os descontos são do Imposto de Renda, que depende 
do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e
que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado 
(é a empresa que deposita). O Salário Líquido corresponde ao Salário 
Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua
hora e a quantidade de horas trabalhadas no mês.
- Desconto do IR:
- Salário Bruto até 900 (inclusive) - isento
- Salário Bruto até 1500 (inclusive) - desconto de 5%
- Salário Bruto até 2500 (inclusive) - desconto de 10%
- Salário Bruto acima de 2500 - desconto de 20% 
Imprima na tela as informações, 
dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a 
quantidade de hora é 220.

  Salário Bruto: (5 * 220)        : R$ 1100,00
  (-) IR (5%)                     : R$   55,00  
  (-) INSS ( 10%)                 : R$  110,00
  FGTS (11%)                      : R$  121,00
  Total de descontos              : R$  165,00
  Salário Liquido                 : R$  935,00"""
  
valor_hora = float (input('Informe o valor em reais(R$) da hora trabalhada: '))
qtd_hora = int(input('Informe a quantidade de horas trabalhadas: '))

salario_bruto = (valor_hora * qtd_hora)
print(f'Salário bruto: ({qtd_hora} horas *  R${valor_hora} valor hora trabalhada )   : {salario_bruto:.2f} reais')  
# calculo de IMPOSTO DE RENDA  
if salario_bruto <= 900:
    desconto_ir = 0
     
elif salario_bruto > 900 and salario_bruto <= 1500:    
    desconto_ir = (salario_bruto * 5)/100  
    
elif salario_bruto > 1500 and salario_bruto <= 2500:    
    desconto_ir = (salario_bruto * 10)/100
    
elif salario_bruto > 2500:    
    desconto_ir = (salario_bruto * 20)/100
print(f'(-) IR (5%):        R$: {desconto_ir:.2f}')

# calculo de INSS
inss = (salario_bruto * 10)/100
print(f'(-) INSS (10%):     R$: {inss:.2f}')

# calculo de FGTS   
fgts = (salario_bruto * 11)/100
print(f'FGTS (11%) -        Valor pago pela empresa.\n')    
print(f'(-) FGTS (11%):     R$: {fgts:.2f}')    

# calculo de sindicato  
sindicato = (salario_bruto * 3)/100
print(f'(-) SINDICATO (3%): R$: {sindicato:.2f}\n')
print(f'Total de descontos: R$ {desconto_ir + inss + sindicato:.2f}\n')
print(f'Salário Liquido:    R$ {salario_bruto - (desconto_ir + inss + sindicato):.2f}\n')   

     
    
             