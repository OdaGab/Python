# Módulo Collections - OrderedDict
# O OrderedDict é uma subclasse de dicionário que lembra a ordem em que as chaves foram inseridas.

# Importante: A partir do Python 3.7, os dicionários padrão (`dict`) também passaram a
# garantir a ordem de inserção. No entanto, o OrderedDict ainda possui comportamentos
# específicos, como a verificação de igualdade sensível à ordem.

from collections import OrderedDict

# --- Dicionário Comum (Python 3.7+) ---
print("--- Dicionário Comum ---")
d_comum = {}
d_comum['a'] = 1
d_comum['b'] = 2
d_comum['c'] = 3
d_comum['d'] = 4

for chave, valor in d_comum.items():
    print(f"Chave: {chave}, Valor: {valor}")
# Note que a ordem de inserção ('a', 'b', 'c', 'd') é preservada.
print("-" * 40)


# --- Usando OrderedDict ---
print("--- OrderedDict ---")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for chave, valor in od.items():
    print(f"Chave: {chave}, Valor: {valor}")
# A ordem também é preservada, como esperado.
print("-" * 40)


# --- A Principal Diferença Hoje: Teste de Igualdade ---
# Dicionários comuns ignoram a ordem ao verificar se são iguais.
# O OrderedDict considera a ordem para a igualdade.

print("--- Comparando Dicionários ---")
# Dicionários comuns com os mesmos itens, mas em ordem diferente
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 2, 'a': 1}
print(f"dict1 = {dict1}")
print(f"dict2 = {dict2}")
print(f"dict1 == dict2?  -> {dict1 == dict2}") # Resultado: True, pois o conteúdo é o mesmo.

print("\n--- Comparando OrderedDicts ---")
# OrderedDicts com os mesmos itens, mas em ordem diferente
od1 = OrderedDict({'a': 1, 'b': 2})
od2 = OrderedDict({'b': 2, 'a': 1})
print(f"od1 = {od1}")
print(f"od2 = {od2}")
print(f"od1 == od2?  -> {od1 == od2}") # Resultado: False, pois a ordem é diferente.
print("-" * 40)


# --- Métodos Específicos do OrderedDict ---
# O OrderedDict possui métodos que não existem em dicionários comuns,
# como o `move_to_end()`.

print("--- Método move_to_end() ---")
od_move = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
print(f"Original: {od_move}")

# Move a chave 'b' para o final
od_move.move_to_end('b')
print(f"Após mover 'b' para o fim: {od_move}")

# Move a chave 'a' para o começo (last=False)
od_move.move_to_end('a', last=False)
print(f"Após mover 'a' para o começo: {od_move}")
print("-" * 40)
