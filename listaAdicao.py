# Adição de Elementos em Listas

# 1. Usando append() - adiciona um elemento no final da lista
frutas = ['maçã', 'banana', 'laranja']
print("Lista original:", frutas)

frutas.append('morango')
print("Após append('morango'):", frutas)

frutas.append('uva')
print("Após append('uva'):", frutas)

print("\n" + "="*50 + "\n")

# 2. Usando extend() - adiciona múltiplos elementos no final
numeros = [1, 2, 3]
print("Lista original:", numeros)

numeros.extend([4, 5, 6])
print("Após extend([4, 5, 6]):", numeros)

numeros.extend([7, 8])
print("Após extend([7, 8]):", numeros)

print("\n" + "="*50 + "\n")

# 3. Usando insert() - adiciona elemento em uma posição específica
cores = ['vermelho', 'azul', 'verde']
print("Lista original:", cores)

cores.insert(1, 'amarelo')
print("Após insert(1, 'amarelo'):", cores)

cores.insert(0, 'roxo')
print("Após insert(0, 'roxo'):", cores)

cores.insert(len(cores), 'preto')
print("Após insert(len(cores), 'preto'):", cores)

print("\n" + "="*50 + "\n")

# 4. Usando + (concatenação) - cria uma nova lista
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
print("Lista1:", lista1)
print("Lista2:", lista2)

lista3 = lista1 + lista2
print("Lista1 + Lista2:", lista3)
print("Lista1 ainda é:", lista1)  # A lista original não foi modificada

print("\n" + "="*50 + "\n")

# 5. Comparação entre os métodos
print("RESUMO DOS MÉTODOS:")
print("\nappend(): adiciona UM elemento no final")
print("extend(): adiciona MÚLTIPLOS elementos no final")
print("insert(): adiciona um elemento em uma POSIÇÃO específica")
print("+: concatena duas listas (cria uma nova lista)")
