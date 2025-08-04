"""

16. Faça um programa que calcule as raízes de uma equação do segundo grau,
na forma ax2 + bx + c. O programa 
deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário 
nas seguintes situações:
- Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau 
e o programa não deve fazer
pedir os demais valores, sendo encerrado;
- Se o delta calculado for negativo, a equação não possui raizes reais. 
Informe ao usuário e encerre o programa;
- Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
- Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

1. Delta positivo (duas raízes reais):
a = 1, b = -3, c = 2
2. Delta negativo
a = 2 , b = 3 , c= 5
a = 1, b = 2, c = 5

3. Delta igual a zero
a = 1, b = -2, c = 1
a = 4, b = 4, c = 1

"""
import math


a = float(input('Informe o valor de A: '))
if a != 0:
      
    b = float(input('Informe o valor de B: '))
    c = float(input('Informe o valor de C: '))
    delta = (b**2) - (4*a*c) 
    if  delta <0:
        print('Delta negativo. A equação não possui raiz real. \n'
              'Programa encerrado.')
    elif delta == 0 :
        raiz = -b / (2 * a)
        print(f'Delta igual a 0 , a equação possui apenas uma raiz = {raiz}')   
    else:
        raiz_1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz_2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f' A equação possui duas raizes: {raiz_1} e {raiz_2}')
    
else:
    print('a equação não é do segundo grau ')
    
    