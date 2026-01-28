# Módulo collections - Deque
# https://docs.python.org/3/library/collections.html#collections.deque

# O deque é uma lista de alta performance.

from collections import deque

# Criando um deque
deq = deque('geek')
print(f'Criando um deque: {deq}') # saíde -> deque(['g', 'e', 'e', 'k'])

# Adicionando elementos no deque
deq.append('y') # Adiciona no final
print(f'Adicionando elementos no deque: {deq}') # saída -> deque(['g', 'e', 'e', 'k', 'y'])

deq.appendleft('x') # Adiciona no começo
print(f'Adicionando elementos no começo do deque: {deq}') # saída -> deque(['x', 'g', 'e', 'e', 'k', 'y'])

# Removendo elementos
print(f'Removendo o ultimo elemento: {deq.pop()}') # saída -> y
print(f'Deque: {deq}') # saída -> deque(['x', 'g', 'e', 'e', 'k'])

print(f'Removendo o primeiro elemento: {deq.popleft()}') # saída -> x
print(f'Deque: {deq}') # saída -> deque(['g', 'e', 'e', 'k'])
