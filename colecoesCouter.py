# Módulo Collections - Counter
# O Counter é uma subclasse de dicionário usada para contar objetos "hashable" (que podem ser chaves de dicionário).

# 1. Importando o Counter
from collections import Counter

# --- Exemplo 1: Contando elementos em uma lista ---
print("--- Exemplo 1: Contando em uma Lista ---")
lista_de_frutas = ["maçã", "banana", "laranja", "maçã", "uva", "banana", "maçã"]

# Criando um Counter a partir da lista
contagem_frutas = Counter(lista_de_frutas)

print(f"Lista original: {lista_de_frutas}")
print(f"Contagem: {contagem_frutas}")

# O Counter se comporta como um dicionário, então você pode acessar a contagem de um item específico:
print(f"Quantas maçãs existem? {contagem_frutas['maçã']}")
print(f"Quantos abacates existem? {contagem_frutas['abacate']}") # Retorna 0 se o item não existir
print("-" * 30)


# --- Exemplo 2: Contando caracteres em uma string ---
print("--- Exemplo 2: Contando em uma String ---")
frase = "abracadabra"
contagem_letras = Counter(frase)
print(f"Frase: '{frase}'")
print(f"Contagem de letras: {contagem_letras}")
print("-" * 30)


# --- Exemplo 3: Usando o método most_common() ---
# Este método retorna uma lista de tuplas com os 'n' elementos mais comuns e suas contagens.
print("--- Exemplo 3: Usando most_common() ---")
contagem_letras_comuns = contagem_letras.most_common(3)
print(f"As 3 letras mais comuns em '{frase}' são: {contagem_letras_comuns}")
print("-" * 30)


# --- Exemplo 4: Contando palavras em um texto ---
print("--- Exemplo 4: Contando Palavras ---")
texto = "O rato roeu a roupa do rei de roma o rato é um animal"
palavras = texto.lower().split() # Converte para minúsculas e divide em palavras

contagem_palavras = Counter(palavras)
print(f"Contagem de palavras: {contagem_palavras}")

# A palavra mais comum
palavra_mais_comum = contagem_palavras.most_common(1)
print(f"A palavra mais comum é: {palavra_mais_comum[0]}")
print("-" * 30)


# O Counter também suporta operações matemáticas
c1 = Counter(a=4, b=2, c=0, d=-2)
c2 = Counter(a=1, b=2, c=3, d=4)

print(f"\nOperações com Counters:")
print(f"c1 = {c1}")
print(f"c2 = {c2}")
print(f"c1 + c2 = {c1 + c2}") # Soma as contagens
print(f"c1 - c2 = {c1 - c2}") # Subtrai (mantém apenas contagens positivas)
print(f"c1 & c2 = {c1 & c2}") # Interseção (mínimo das contagens)
print(f"c1 | c2 = {c1 | c2}") # União (máximo das contagens)
