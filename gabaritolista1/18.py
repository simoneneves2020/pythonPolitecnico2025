"""18. Faça um programa que peça o tamanho
de um arquivo para download (em MB) e a velocidade 
de um link de Internet (em Mbps), 
calcule e informe o tempo aproximado de 
download do arquivo usando este link (em minutos)."""

arquivo = int(input("Digite o tamanho do arquivo (em MB): "))
velocidade = int(input("Digite a velocidade da internet (em Mbps): "))

tempo = float(arquivo / velocidade)
print(f"O tempo aproximado de download do arquivo usando este link (em minutos): {tempo}")  


"""

* **MB (megabyte)**: unidade usada para medir o tamanho do arquivo
* **Mbps (megabit por segundo)**: unidade usada para medir a velocidade da internet
* ⚠️ **1 byte = 8 bits**, portanto:
  👉 **1 MB = 8 megabits**



#### Passos:

1. **Converter o tamanho do arquivo de MB para megabits:**

   Tamanho em Megabits = Tamanho em MB * 8

2. **Calcular o tempo em segundos:**

   Tempo em segundos = Tamanho em megabits / Velocidade da internet

3. **Converter segundos para minutos:**

   Tempo em minutos = tempo em segundos / 60

---

### ✅ **Exemplo**

Suponha:

* Arquivo: 100 MB
* Velocidade da internet: 10 Mbps

**Cálculo:**

1. `100 MB × 8 = 800 megabits`
2. `800 / 10 = 80 segundos`
3. `80 / 60 = 1,33 minutos (aprox.)`

**Resultado:** O tempo aproximado de download será **1,33 minutos**, ou cerca de **1 minuto e 20 segundos**.



```python
# Entrada do usuário
tamanho_arquivo_mb = float(input("Digite o tamanho do arquivo (em MB): "))
velocidade_mbps = float(input("Digite a velocidade do link (em Mbps): "))

# Cálculo do tempo
tamanho_megabits = tamanho_arquivo_mb * 8
tempo_segundos = tamanho_megabits / velocidade_mbps
tempo_minutos = tempo_segundos / 60

# Resultado
print(f"\nTempo aproximado de download: {tempo_minutos:.2f} minutos")
```


"""