
# Este arquivo demonstra as operações básicas em Python.

# -------------------------
# 1. Operações Aritméticas
# -------------------------
print("--- Operações Aritméticas ---")
a = 10
b = 3

soma = a + b          # Soma
subtracao = a - b     # Subtração
multiplicacao = a * b # Multiplicação
divisao = a / b       # Divisão (sempre retorna um número com ponto flutuante, ex: float)
divisao_inteira = a // b # Divisão inteira (descarta a parte decimal)
resto = a % b         # Resto da divisão (módulo)
potencia = a ** b     # Potência (a elevado a b)

print(f"{a} + {b} = {soma}")
print(f"{a} - {b} = {subtracao}")
print(f"{a} * {b} = {multiplicacao}")
print(f"{a} / {b} = {divisao}")
print(f"{a} // {b} = {divisao_inteira}")
print(f"{a} % {b} = {resto}")
print(f"{a} ** {b} = {potencia}")
print("-" * 20)


# -------------------------
# 2. Operações com Strings (Textos)
# -------------------------
print("--- Operações com Strings ---")
primeiro_nome = "João"
segundo_nome = "Silva"

# Concatenação (+)
nome_completo = primeiro_nome + " " + segundo_nome
print(f"Nome completo: {nome_completo}")

# Repetição (*)
risada = "ha" * 5
print(f"Risada: {risada}")
print("-" * 20)


# -------------------------
# 3. Operações de Comparação
# -------------------------
print("--- Operações de Comparação ---")
x = 15
y = 20

print(f"x ({x}) é igual a y ({y})? {x == y}")
print(f"x ({x}) é diferente de y ({y})? {x != y}")
print(f"x ({x}) é maior que y ({y})? {x > y}")
print(f"x ({x}) é menor que y ({y})? {x < y}")
print(f"x ({x}) é maior ou igual a y ({y})? {x >= y}")
print(f"x ({x}) é menor ou igual a y ({y})? {x <= y}")
print("-" * 20)


# -------------------------
# 4. Operações Lógicas
# -------------------------
print("--- Operações Lógicas ---")
tem_dinheiro = True
tem_tempo = False

# 'and' (E): só é verdadeiro se AMBAS as condições forem verdadeiras.
pode_viajar = tem_dinheiro and tem_tempo
print(f"Pode viajar (dinheiro E tempo)? {pode_viajar}")

# 'or' (OU): é verdadeiro se PELO MENOS UMA das condições for verdadeira.
pode_ir_ao_parque = tem_dinheiro or tem_tempo
print(f"Pode ir ao parque (dinheiro OU tempo)? {pode_ir_ao_parque}")

# 'not' (NÃO): inverte o valor booleano.
nao_tem_dinheiro = not tem_dinheiro
print(f"Não tem dinheiro? {nao_tem_dinheiro}")
print("-" * 20)

