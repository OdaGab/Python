# O operador 'is' compara a identidade de dois objetos.
# Ele retorna True se duas variáveis apontam para o mesmo objeto na memória, e False caso contrário.

# Exemplo com tipos imutáveis (inteiros)
a = 5
b = 5
print(f"a = {a}, b = {b}")
print(f"a is b: {a is b}")  # Para inteiros pequenos, o Python frequentemente reutiliza o mesmo objeto.

c = 257
d = 257
print(f"c = {c}, d = {d}")
print(f"c is d: {c is d}") # Para inteiros maiores, o Python pode criar objetos diferentes.

# Exemplo com tipos mutáveis (listas)
list_a = [1, 2, 3]
list_b = [1, 2, 3]
list_c = list_a

print("\nListas:")
print(f"list_a = {list_a}")
print(f"list_b = {list_b}")
print(f"list_c = {list_c}")

# list_a e list_b têm o mesmo conteúdo, mas são objetos diferentes.
print(f"list_a is list_b: {list_a is list_b}")
print(f"list_a == list_b: {list_a == list_b}") # '==' verifica a igualdade do conteúdo.

# list_a e list_c apontam para o mesmo objeto.
print(f"list_a is list_c: {list_a is list_c}")

# Modificar list_a também afetará list_c
list_a.append(4)
print(f"\nApós modificar list_a:")
print(f"list_a = {list_a}")
print(f"list_c = {list_c}")
print(f"list_a is list_c: {list_a is list_c}")
