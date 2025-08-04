"""12. Tendo como dados de entrada a altura de uma pessoa, 
construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58"""


#fórmaula fórmula: (72.7*altura) - 58

# esta fórmula conseguimos na internet, famosa CÁLCLUO DE IMC
# neste exercício ele está fixando dos valores , não deixa que o usuario digite todas
# as infomações... 

altura = float(input('Digite a altura de uma pessoa: '))
peso = (72.7 * altura) - 58
print(f'O peso ideal considerando a altura informada é: {peso:.2f}')        