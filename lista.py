# -*- coding: utf-8 -*-
# Listas em Python

# Criando uma lista de frutas
frutas = ["maçã", "banana", "laranja", "uva"]
print(f"Lista de frutas: {frutas}")

# Acessando elementos
primeira_fruta = frutas[0]
print(f"Primeira fruta: {primeira_fruta}")

# Modificando elementos
frutas[1] = "morango"
print(f"Lista com banana trocada por morango: {frutas}")

# Adicionando elementos
frutas.append("abacaxi")
print(f"Adicionando abacaxi no final da lista: {frutas}")

# Fatiando (slicing) a lista de frutas
primeiras_duas = frutas[0:2]
print(f"As duas primeiras frutas da lista: {primeiras_duas}")

# Obtendo o tamanho da lista de frutas
tamanho_frutas = len(frutas)
print(f"Tamanho da lista de frutas: {tamanho_frutas}")

# Iterando sobre a lista de frutas
print("\nIterando sobre a lista de frutas:")
for fruta in frutas:
    print(fruta)

# --- Lista Numérica ---

# Criando uma lista numérica
Z = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(f"\nLista numérica Z: {Z}")

# Acessando um elemento da lista Z
terceiro_elemento_Z = Z[2]
print(f"Terceiro elemento da lista Z: {terceiro_elemento_Z}")

# Fatiando a lista Z
primeiros_cinco_Z = Z[0:5]
print(f"Os cinco primeiros elementos de Z: {primeiros_cinco_Z}")

# Funções em lista numérica
soma_Z = sum(Z)
menor_valor_Z = min(Z)
maior_valor_Z = max(Z)

# Imprimindo resultados
print("\nResultados das funções em lista numérica:")

print(f"Soma de todos os elementos de Z: {soma_Z}")
print(f"Menor valor em Z: {menor_valor_Z}")
print(f"Maior valor em Z: {maior_valor_Z}")
print(f"Tamanho da lista Z: {len(Z)}")
print(f"Média dos valores em Z: {soma_Z / len(Z)}")
print(f"Valores únicos em Z: {set(Z)}")
print(f"Lista Z ordenada: {sorted(Z)}")
print(f"Lista Z em ordem reversa: {list(reversed(Z))}")
print(f"Lista Z convertida para tupla: {tuple(Z)}")
print(f"Lista Z convertida para string: {str(Z)}")
print(f"Lista Z convertida para conjunto: {set(Z)}")
print(f"Lista Z convertida para dicionário: {dict(enumerate(Z))}")


# Lista usando list comprehension
quadrados = [x**2 for x in Z]
print(f"\nLista de quadrados dos elementos de Z: {quadrados}")  
# Filtrando elementos pares usando list comprehension
pares = [x for x in Z if x % 2 == 0]
print(f"Lista de números pares em Z: {pares}")  
# Mapeando elementos para dobrar seus valores
dobrados = [x * 2 for x in Z]
print(f"Lista de elementos de Z dobrados: {dobrados}")  
# Criando uma lista de tuplas (número, seu quadrado)
tuplas_quadrados = [(x, x**2) for x in Z]
print(f"Lista de tuplas (número, seu quadrado): {tuplas_quadrados}")  

# While loop para iterar sobre a lista Z
print("\nIterando sobre a lista Z usando while loop:")
i = 0
while i < len(Z):
    print(Z[i])
    i += 1  
# Usando enumerate para obter índice e valor
print("\nIterando sobre a lista Z usando enumerate:")
for index, value in enumerate(Z):
    print(f"Índice: {index}, Valor: {value}")  

# Usando zip para combinar duas listas
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
combinado = list(zip(Z, letras))
print(f"\nLista combinada de Z e letras: {combinado}")  

# Usando map para aplicar uma função a todos os elementos   
def cubo(x):
    return x**3
cubos = list(map(cubo, Z))
print(f"Lista de cubos dos elementos de Z: {cubos}")  

# Usando filter para filtrar elementos maiores que 5
maiores_que_cinco = list(filter(lambda x: x > 5, Z))
print(f"Lista de elementos de Z maiores que 5: {maiores_que_cinco}")        
# Usando reduce para somar todos os elementos
from functools import reduce
soma_total = reduce(lambda x, y: x + y, Z)
print(f"Soma total dos elementos de Z usando reduce: {soma_total}") 
