# -*- coding: utf-8 -*-
# Listas com range

# Criando uma lista a partir de um range
# range(stop)
lista1 = list(range(10))
print(f"Lista criada com range(10): {lista1}")

# range(start, stop)
lista2 = list(range(5, 11))
print(f"Lista criada com range(5, 11): {lista2}")

# range(start, stop, step)
lista3 = list(range(0, 10, 2))
print(f"Lista de números pares de 0 a 8: {lista3}")

lista4 = list(range(10, 0, -1))
print(f"Lista de 10 a 1 em ordem decrescente: {lista4}")
