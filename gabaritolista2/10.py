"""10. Faça um Programa que pergunte em que turno você estuda.
Peça para digitar M-matutino
ou V-Vespertino ou N- Noturno. Imprima a mensagem 
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso."""

turno = input('Informe o turno que você estuda [M/V/N]: ')
turno = turno.upper() # inicio de trabalho com função , sem necessidad e importação de 
# biblioteca

if turno == 'M':    
    print('Bom dia!')
elif turno == 'V':
    print('Boa tarde!')
elif turno == 'N':
    print('Boa noite!')
else:
    print('Valor inválido!')
    