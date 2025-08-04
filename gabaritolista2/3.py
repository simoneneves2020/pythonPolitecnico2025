"""3. Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido."""

sexo = input('Informe o sexo do usuário [M/F]: ')
sexo = sexo.upper()
if sexo == 'F':    
    print('F - Feminino')
elif sexo == 'M':
    print('M - Masculino')
else:
    print(f'O dígito {sexo} não é válido')  