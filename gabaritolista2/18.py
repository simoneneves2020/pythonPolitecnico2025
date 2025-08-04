"""
18. Faça um Programa que 
peça uma data no formato dd/mm/aaaa e 
determine se a mesma é uma data válida.

para fazer este programa não dar erro teremos que trabalhar primeiro com 
split
vetor
Claro! Vamos montar um programa completo em Python que:

* Pede a data no formato `dd/mm/aaaa`
* Verifica se é uma **data válida**, incluindo o tratamento de:

  * Dias válidos para cada mês
  * Mês válido (1 a 12)
  * Ano válido
  * Ano bissexto (caso seja fevereiro)

---

## ✅ Código completo:

```python
def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

def data_valida(dia, mes, ano):
    if mes < 1 or mes > 12:
        return False

    if dia < 1:
        return False

    # Dias máximos por mês
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return dia <= 31
    elif mes in [4, 6, 9, 11]:
        return dia <= 30
    elif mes == 2:
        if eh_bissexto(ano):
            return dia <= 29
        else:
            return dia <= 28
    return False

# Entrada do usuário
data = input('Insira a data [dd/mm/aaaa]: ')

try:
    partes = data.split('/')
    if len(partes) != 3:
        raise ValueError("Formato inválido.")

    dia = int(partes[0])
    mes = int(partes[1])
    ano = int(partes[2])

    if data_valida(dia, mes, ano):
        print(f'{data} é uma data válida.')
    else:
        print(f'{data} é uma data inválida.')

except ValueError:
    print('Formato inválido. Use dd/mm/aaaa com números inteiros.')
```

---

## 🧪 Exemplos de entrada e saída:

```
Insira a data [dd/mm/aaaa]: 29/02/2024
→ 29/02/2024 é uma data válida.

Insira a data [dd/mm/aaaa]: 31/04/2025
→ 31/04/2025 é uma data inválida.

Insira a data [dd/mm/aaaa]: 30/02/2023
→ 30/02/2023 é uma data inválida.

Insira a data [dd/mm/aaaa]: 15/13/2022
→ 15/13/2022 é uma data inválida.
```

---

Se quiser, posso adaptar para permitir entrada com hífen (`dd-mm-aaaa`) ou validar intervalo de datas. Deseja isso?





"""
data = input('Insira a data [dd/mm/aaaa]: ')
# inserção da função que conta a quantidade de caracteres de uma string
if len(data) != 10:
    print('Data inválida.')
else:
    print('Data válida.')   