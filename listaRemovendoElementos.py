# Remoção de Elementos em Listas

# 1. Usando remove() - remove a primeira ocorrência de um valor
frutas = ['maçã', 'banana', 'laranja', 'banana']
print("Lista original:", frutas)

frutas.remove('banana')
print("Após remove('banana'):", frutas)

frutas.remove('maçã')
print("Após remove('maçã'):", frutas)

print("\n" + "="*50 + "\n")

# 2. Usando pop() - remove elemento por índice e retorna o valor
numeros = [1, 2, 3, 4, 5]
print("Lista original:", numeros)

removido = numeros.pop()  # Remove o último elemento
print("pop() removeu:", removido)
print("Lista após pop():", numeros)

removido = numeros.pop(0)  # Remove o primeiro elemento
print("pop(0) removeu:", removido)
print("Lista após pop(0):", numeros)

removido = numeros.pop(1)  # Remove elemento no índice 1
print("pop(1) removeu:", removido)
print("Lista após pop(1):", numeros)

print("\n" + "="*50 + "\n")

# 3. Usando del - remove elemento por índice
cores = ['vermelho', 'azul', 'verde', 'amarelo', 'roxo']
print("Lista original:", cores)

del cores[0]
print("Após del cores[0]:", cores)

del cores[2]
print("Após del cores[2]:", cores)

print("\n" + "="*50 + "\n")

# 4. Usando del com fatias - remove múltiplos elementos
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print("Lista original:", letras)

del letras[1:3]  # Remove elementos do índice 1 ao 2
print("Após del letras[1:3]:", letras)

print("\n" + "="*50 + "\n")

# 5. Usando clear() - remove todos os elementos
animais = ['gato', 'cachorro', 'pássaro', 'peixe']
print("Lista original:", animais)

animais.clear()
print("Após clear():", animais)
print("Lista vazia?", len(animais) == 0)

print("\n" + "="*50 + "\n")

# 6. Comparação entre os métodos
print("RESUMO DOS MÉTODOS:")
print("\nremove(valor): remove a PRIMEIRA ocorrência do valor")
print("pop(): remove o ÚLTIMO elemento e retorna seu valor")
print("pop(índice): remove elemento em POSIÇÃO específica e retorna seu valor")
print("del lista[índice]: remove elemento em POSIÇÃO específica (não retorna)")
print("del lista[início:fim]: remove INTERVALO de elementos")
print("clear(): remove TODOS os elementos da lista")

print("\n" + "="*50 + "\n")

# 7. Exemplos práticos
print("EXEMPLOS PRÁTICOS:\n")

# Remover último elemento de uma fila
fila = [1, 2, 3, 4, 5]
print("Fila:", fila)
print("Removendo último:", fila.pop())
print("Fila atualizada:", fila)

print()

# Remover primeiro elemento de uma fila
fila2 = ['primeiro', 'segundo', 'terceiro']
print("Fila:", fila2)
print("Removendo primeiro:", fila2.pop(0))
print("Fila atualizada:", fila2)

print()

# Limpar uma lista completamente
temporaria = [10, 20, 30, 40]
print("Lista temporária:", temporaria)
temporaria.clear()
print("Após clear():", temporaria)
