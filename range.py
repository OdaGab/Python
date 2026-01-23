# A função range() gera uma sequência imutável de números.
# É uma forma muito eficiente de criar sequências numéricas para usar em loops,
# pois não armazena todos os números na memória de uma vez.

# --- Sintaxe ---
# range(stop): Gera números de 0 até stop - 1.
# range(start, stop): Gera números de start até stop - 1.
# range(start, stop, step): Gera números de start até stop - 1, pulando de 'step' em 'step'.

# Exemplo 1: Usando apenas o 'stop'
# Gera uma sequência de 0 a 4 (o 5 não é incluído).
print("--- range(5) ---")
for numero in range(5):
    print(f"Número: {numero}")

# Exemplo 2: Usando 'start' e 'stop'
# Gera uma sequência de 2 a 7 (o 7 não é incluído).
print("\n--- range(2, 7) ---")
for numero in range(2, 7):
    print(f"Número: {numero}")

# Exemplo 3: Usando 'start', 'stop' e 'step'
# Gera uma sequência de números pares de 0 a 10.
print("\n--- range(0, 11, 2) ---")
for numero in range(0, 11, 2):
    print(f"Número par: {numero}")

# Exemplo 4: Criando uma contagem regressiva
# O 'step' negativo inverte a ordem.
print("\n--- range(5, 0, -1) ---")
for numero in range(5, 0, -1):
    print(f"Contagem regressiva: {numero}")
print("Fogo!")

# O que é um objeto range?
# A função range() cria um objeto especial do tipo 'range', não uma lista.
meu_range = range(10)
print(f"\nO tipo do objeto criado é: {type(meu_range)}")
print(f"O objeto em si: {meu_range}")

# Para visualizar todos os números de uma vez, podemos converter o range para uma lista.
lista_de_numeros = list(meu_range)
print(f"O objeto range convertido para lista: {lista_de_numeros}")
