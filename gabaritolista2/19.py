"""

19. Faça um Programa que leia um número inteiro menor que 1000 e imprima 
a quantidade de centenas, dezenas e unidades 
do mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. 
Exemplo:
- 326 = 3 centenas, 2 dezenas e 6 unidades
- 12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 
301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

"""
try:
    numero = int(input('Digite um número menor do que 1000 ==> '))
    if numero > 1000:
        print('Digite um número menor do que 1000')
        exit
    #elif numero<0:
        #print('Digite um número inteiro')
        #exit
        #numero = abs(numero)
    else:
        numero = abs(numero) # uso da função absoluto caso queira considerar numeros negativos
        centena = numero // 100
        # na centena ele está dividindo por 100 e pegando o valor inteiro(somente)
        dezena = (numero % 100) // 10
        # na dezena está pegando os dois últimos digitos do numero
        # no caso de explo 123 , ele pega o 23 ... com o numero % 100
        # apos ele pegar o 23 no exemplo ele divide com por 10 pegando somente o inteiro 2,3
        
        unidade = (numero % 100) % 10   
        # para pegar a unidade ele pega os dois numero do digito
        # depois dele ele divide por 10 pegando somente o inteiro 3
        
        if centena == 1:
            string_centena = 'centena'
        else:
            string_centena = 'centenas'
        
        if dezena == 1:
            string_dezena = 'dezena'
        else:
            string_dezena = 'dezenas'
        
        if unidade == 1:
            string_unidade = 'unidade'
        else:
            string_unidade = 'unidades'
        
        print(f'{numero} = {centena} {string_centena}, {dezena} {string_dezena} e {unidade} {string_unidade}')
    
    
    
    

    
except:
    print('Digite um número inteiro')
    exit