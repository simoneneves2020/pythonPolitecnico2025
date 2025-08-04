"""11. As Organizações Tabajara resolveram dar um aumento de salário aos seus 
colaboradores e lhe contraram para
desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo 
o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento."""
salario = float(input('Informe o salário: '))
if salario <= 280.00:
    aumento = (salario * 20) / 100
    salario_aumento = salario + aumento
    print(f'Salário antes do reajuste: R$ {salario:.2f}\n'
          f'Percentual de aumento: 20%\n'
          f'Valor do aumento: R$ {aumento:.2f}\n'
          f'Novo salário: R$ {salario_aumento:.2f}')
elif salario > 280.00 and salario <= 700.00:    
    aumento = (salario * 15) / 100    
    salario_aumento = salario + aumento
    print(f'Salário antes do reajuste: R$ {salario:.2f}\n'
          f'Percentual de aumento: 15%\n'
          f'Valor do aumento: R$ {aumento:.2f}\n'
          f'Novo salário: R$ {salario_aumento:.2f}')
elif salario > 700.00 and salario <= 1500.00:
    aumento = (salario * 10) / 100
    salario_aumento = salario + aumento
    print(f'Salário antes do reajuste: R$ {salario:.2f}\n'
          f'Percentual de aumento: 10%\n'
          f'Valor do aumento: R$ {aumento:.2f}\n'
          f'Novo salário: R$ {salario_aumento:.2f}')
else:
    aumento = (salario * 5) / 100
    salario_aumento = salario + aumento
    print(f'Salário antes do reajuste: R$ {salario:.2f}\n'
          f'Percentual de aumento: 5%\n'
          f'Valor do aumento: R$ {aumento:.2f}\n'
          f'Novo salário: R$ {salario_aumento:.2f}')    

