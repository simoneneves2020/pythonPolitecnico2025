"""24. Faça um Programa que leia 2 números e em seguida 
pergunte ao usuário qual operação ele deseja realizar. O resultado da 
operação deve ser acompanhado de uma frase que diga se o número é:
- par ou ímpar;
- positivo ou negativo;
- inteiro ou decimal.
"""
try:
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))
    op = input('Qual operação desejada?\n a - par ou ímpar;\n b - positivo ou negativo;\n c - inteiro ou decimal   ')
    op = op.lower() # transformando a opção em minuscula
    if op == 'a':                       
        if (numero1 % 2) == 0:  
            print(f'{numero1} é par')
        else:
            print(f'{numero1} é impar')
        if (numero2 % 2) == 0:
            print(f'{numero2} é par')
        else:
            print(f'{numero2} é impar')
    elif op == 'b':
        if numero1 > 0:
            print(f'{numero1} é positivo')
        else:
            print(f'{numero1} é negativo')
        if numero2 > 0:
            print(f'{numero2} é positivo')
        else:
            print(f'{numero2} é negativo')
    elif op == 'c':
        if (numero1 % 1) == 0:
            print(f'{numero1} é inteiro')
        else:
            print(f'{numero1} é decimal')
        if (numero2 % 1) == 0:
            print(f'{numero2} é inteiro')
        else:
            print(f'{numero2} é decimal')
        



except:
    print('Digite um número inteiro ou decimal')
    exit