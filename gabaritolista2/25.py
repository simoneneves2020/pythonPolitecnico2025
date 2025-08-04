"""
25. Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
- "Telefonou para a vítima?"
- "Esteve no local do crime?"
- "Mora perto da vítima?"
- "Devia para a vítima?"
- "Já trabalhou com a vítima?"
- 
O programa deve no final emitir uma classificação sobre a participação da pessoa 
no crime. Se a pessoa responder positivamente
a 2 questões ela deve ser classificada como 
"Suspeita", entre 3 e 4 como "Cúmplice" e 5 como 
"Assassino". Caso contrário, ele será classificado como "Inocente".

"""
op1 = int(input('telefonou para a vitima [sim - 1/ nao - 0]'))
op2 = int(input('esteve no local do crime [sim - 1/ nao - 0]'))
op3 = int(input('mora perto da vitima [sim - 1/ nao - 0]'))
op4 = int(input('devia para a vitima [sim - 1/ nao - 0]'))  
op5 = int(input('ja trabalhou com a vitima [sim - 1/ nao - 0]'))    

#resultado =sum([op1,op2,op3,op4,op5]) # função para somar
soma = op1+op2+op3+op4+op5  

if soma == 2:
    print(f'voce e  suspeito')
elif soma == 3 or soma == 4:
    print(f'voce e  cumplice')
elif soma == 5:
    print(f'voce e  assassino')
else:
    print(f'voce e  inocente')              


