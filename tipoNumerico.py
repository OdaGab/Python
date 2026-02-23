
# --- Tipos Numéricos em Python ---

# Python tem três tipos numéricos principais:
# 1. int - Inteiros
# 2. float - Ponto Flutuante (decimais)
# 3. complex - Números Complexos

# -------------------------
# 1. int (Inteiro)
# -------------------------
print("--- Tipo int (Inteiro) ---")

# São números inteiros, positivos ou negativos, sem parte decimal.
# O tamanho de um int é limitado apenas pela memória disponível.

numero_inteiro = 10
numero_negativo = -200
numero_grande = 9876543210987654321

print(f"Valor: {numero_inteiro}, Tipo: {type(numero_inteiro)}")
print(f"Valor: {numero_negativo}, Tipo: {type(numero_negativo)}")
print(f"Valor de um número grande: {numero_grande}, Tipo: {type(numero_grande)}")
print("-" * 20)


# -------------------------
# 2. float (Ponto Flutuante)
# -------------------------
print("--- Tipo float (Ponto Flutuante) ---")

# São números com uma parte decimal. São usados para representar números reais.
# Use o ponto (.) como separador decimal.

preco_produto = 19.99
pi = 3.14159
valor_negativo_float = -0.0075

print(f"Valor: {preco_produto}, Tipo: {type(preco_produto)}")
print(f"Valor: {pi}, Tipo: {type(pi)}")
print(f"Valor: {valor_negativo_float}, Tipo: {type(valor_negativo_float)}")

# Floats também podem ser escritos em notação científica (e).
massa_da_terra = 5.972e24 # 5.972 * 10^24
print(f"Massa da Terra (notação científica): {massa_da_terra}, Tipo: {type(massa_da_terra)}")
print("-" * 20)


# -------------------------
# 3. complex (Complexo)
# -------------------------
print("--- Tipo complex (Complexo) ---")

# São números com uma parte real e uma parte imaginária.
# A parte imaginária é indicada por um 'j' ou 'J'.
# São menos comuns no dia a dia, mas importantes em certas áreas da engenharia e matemática.

numero_complexo = 3 + 5j
outro_complexo = -2j

print(f"Valor: {numero_complexo}, Tipo: {type(numero_complexo)}")

# Podemos acessar as partes real e imaginária separadamente.
print(f"Parte Real: {numero_complexo.real}")
print(f"Parte Imaginária: {numero_complexo.imag}")
print("-" * 20)


# -------------------------
# Conversão entre Tipos (Type Casting)
# -------------------------
print("--- Conversão de Tipos ---")

valor_float = 9.81
valor_int = 15

# Convertendo float para int (a parte decimal é truncada/removida)
int_convertido = int(valor_float)
print(f"O float {valor_float} convertido para int é: {int_convertido}, Tipo: {type(int_convertido)}")

# Convertendo int para float
float_convertido = float(valor_int)
print(f"O int {valor_int} convertido para float é: {float_convertido}, Tipo: {type(float_convertido)}")
print("-" * 20)
