# Módulo Collections - defaultdict
# O defaultdict é uma subclasse de dicionário que chama uma função "fábrica"
# para fornecer um valor para uma chave que ainda não existe.

from collections import defaultdict

# --- O Problema com Dicionários Comuns ---
print("--- Problema com Dicionário Comum ---")
dicionario_comum = {}
# A linha abaixo causaria um erro (KeyError), pois a chave 'fruta' não existe.
# print(dicionario_comum['fruta']) 
print("Tentar acessar uma chave inexistente em um dict comum causa um KeyError.")
print("-" * 40)


# --- Solução com defaultdict ---

# --- Exemplo 1: Usando `int` como padrão ---
# Isso é muito útil para contadores. Se a chave não existir, 
# a função `int()` é chamada, que retorna 0.

print("--- Exemplo 1: defaultdict(int) ---")
contador = defaultdict(int)
lista_de_frutas = ["maçã", "banana", "laranja", "maçã", "uva", "banana", "maçã"]

for fruta in lista_de_frutas:
    contador[fruta] += 1 # Se a fruta não estiver no contador, seu valor começa em 0.

print(f"Contagem de frutas: {contador}")
print(f"Contagem de 'maçã': {contador['maçã']}")
print(f"Contagem de 'abacate' (nunca vista): {contador['abacate']}") # Acessar não dá erro, retorna 0.
print(f"O dicionário agora contém a chave 'abacate': {contador}")
print("-" * 40)


# --- Exemplo 2: Usando `list` como padrão ---
# Útil para agrupar itens. Se a chave não existir, a função `list()` é chamada,
# que retorna uma lista vazia [].

print("--- Exemplo 2: defaultdict(list) ---")
agrupador = defaultdict(list)
lista_de_nomes = ["Ana", "Bruno", "Beatriz", "Carlos", "Carla", "Daniel"]

for nome in lista_de_nomes:
    primeira_letra = nome[0]
    agrupador[primeira_letra].append(nome) # Se a letra não for chave, uma lista vazia é criada primeiro.

print(f"Nomes agrupados pela primeira letra:")
print(agrupador)
print(f"Nomes com a letra 'B': {agrupador['B']}")
print(f"Nomes com a letra 'Z': {agrupador['Z']}") # Retorna []
print("-" * 40)


# --- Exemplo 3: Usando `lambda` para um padrão customizado ---
# Você pode usar uma função lambda para retornar qualquer valor padrão que desejar.

print("--- Exemplo 3: defaultdict com lambda ---")
dicionario_custom = defaultdict(lambda: "Valor Padrão")
dicionario_custom['chave1'] = 'valor existente'

print(f"Acessando chave existente: {dicionario_custom['chave1']}")
print(f"Acessando chave inexistente: {dicionario_custom['chave_nova']}")
print(f"Dicionário final: {dicionario_custom}")
print("-" * 40)
