""" 10. Faça um Programa que peça a temperatura em graus Celsius, 
transforme e mostre em graus Farenheit."""

celsius = float(input('Informe e temperatura em graus Celsius: '))
fahrenheit = float((celsius * 1.8) + 32)

print(f'{celsius} Cº = {fahrenheit:.1f} Fº')    