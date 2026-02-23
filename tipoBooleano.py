# O tipo booleano em Python é usado para representar um de dois valores:
# True (verdadeiro) ou False (falso).

# Atribuindo valores booleanos a variáveis
verdadeiro = True
falso = False

print(f"O valor da variável 'verdadeiro' é: {verdadeiro}")
print(f"O valor da variável 'falso' é: {falso}")
print(f"O tipo da variável 'verdadeiro' é: {type(verdadeiro)}")
print("-" * 30)

# Expressões que resultam em valores booleanos
# Comparações:
# == (igual a)
# != (diferente de)
# > (maior que)
# < (menor que)
# >= (maior ou igual a)
# <= (menor ou igual a)

x = 10
y = 5

print(f"x > y? {x > y}")    # Verdadeiro
print(f"x < y? {x < y}")    # Falso
print(f"x == 10? {x == 10}") # Verdadeiro
print(f"x != y? {x != y}")  # Verdadeiro
print(f"y <= 5? {y <= 5}")  # Verdadeiro
print("-" * 30)

# Operadores lógicos: and, or, not

# 'and' (E): Retorna True se AMBAS as condições forem verdadeiras.
print(f"10 > 5 and 5 < 8? {10 > 5 and 5 < 8}") # True and True -> True
print(f"10 > 5 and 5 > 8? {10 > 5 and 5 > 8}") # True and False -> False

# 'or' (OU): Retorna True se PELO MENOS UMA das condições for verdadeira.
print(f"10 < 5 or 5 < 8? {10 < 5 or 5 < 8}") # False or True -> True
print(f"10 < 5 or 5 > 8? {10 < 5 or 5 > 8}") # False or False -> False

# 'not' (NÃO): Inverte o valor booleano.
esta_chovendo = False
print(f"Está chovendo? {esta_chovendo}")
print(f"Não está chovendo? {not esta_chovendo}") # not False -> True
print("-" * 30)

# O valor booleano de outros tipos
# Em Python, vários valores são avaliados como False em um contexto booleano:
# - O número 0 (inteiro ou ponto flutuante)
# - Strings vazias ("")
# - Listas, tuplas ou dicionários vazios
# - O valor None

print(f"O booleano de 0 é: {bool(0)}")
print(f"O booleano de 1 é: {bool(1)}")
print(f"O booleano de uma string vazia '' é: {bool('')}")
print(f"O booleano da string 'Olá' é: {bool('Olá')}")
print(f"O booleano de uma lista vazia [] é: {bool([])}")
print(f"O booleano de None é: {bool(None)}")
