"""4. Faça um Programa que verifique se uma letra digitada é vogal ou consoante."""

letra = input('Digite uma letra: ')
letra = letra.upper()


if letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print(f'A letra {letra} é uma vogal.')

else:
    print(f'O caractere digitado é uma consuante.')