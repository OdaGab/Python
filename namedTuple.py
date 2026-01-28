# Módulo Collections - namedtuple
# A função namedtuple é uma fábrica que cria subclasses de tuplas com nomes de campo.
# Você pode usá-la para criar tipos de tupla imutáveis e legíveis.

from collections import namedtuple

# --- O Problema com Tuplas Comuns ---
# Tuplas são ótimas, mas acessar seus elementos por índice pode deixar o código confuso.
print("--- Tupla Comum ---")
carta_tupla = ('10', 'Ouros')
print(f"Valor: {carta_tupla[0]}, Naipe: {carta_tupla[1]}") # Funciona, mas não é muito legível.
# O que é o índice 0? E o 1? Precisamos adivinhar ou lembrar a estrutura.
print("-" * 40)


# --- Solução com namedtuple ---
print("--- Usando namedtuple ---")

# 1. Criando a "fábrica" da nossa tupla nomeada
#    O primeiro argumento é o nome do novo tipo ('Carta').
#    O segundo argumento é uma string com os nomes dos campos, separados por espaço ou vírgula.
Carta = namedtuple('Carta', 'valor naipe')

# 2. Criando instâncias (objetos) da nossa namedtuple
as_de_espadas = Carta(valor='A', naipe='Espadas')
dez_de_ouros = Carta(valor='10', naipe='Ouros')

# 3. Acessando os dados de forma legível
print(f"Carta 1: {as_de_espadas.valor} de {as_de_espadas.naipe}")
print(f"Carta 2: {dez_de_ouros.valor} de {dez_de_ouros.naipe}")

# Você ainda pode acessar por índice, como uma tupla normal
print(f"Acessando por índice: Valor={as_de_espadas[0]}, Naipe={as_de_espadas[1]}")
print("-" * 40)


# --- Propriedades e Métodos Úteis ---
print("--- Propriedades Úteis ---")

# Tuplas nomeadas são imutáveis, assim como as tuplas comuns.
# A linha abaixo causaria um erro (AttributeError):
# as_de_espadas.valor = 'K'

# Você pode converter uma namedtuple para um dicionário (OrderedDict)
print(f"Como dicionário: {as_de_espadas._asdict()}")

# Você pode criar uma nova instância substituindo alguns valores
nova_carta = as_de_espadas._replace(valor='K')
print(f"Carta original: {as_de_espadas}")
print(f"Nova carta com _replace: {nova_carta}")

# Você pode ver os campos definidos
print(f"Campos da tupla: {as_de_espadas._fields}")
print("-" * 40)


# --- Exemplo Prático: Coordenadas ---
print("--- Exemplo Prático: Coordenadas ---")
Ponto = namedtuple('Ponto', ['x', 'y', 'z'])
ponto_a = Ponto(x=10, y=20, z=30)
print(f"Ponto A - x: {ponto_a.x}, y: {ponto_a.y}, z: {ponto_a.z}")
print(ponto_a)
print("-" * 40)
