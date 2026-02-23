# Criando uma lista original
lista_original = ['banana', 'maçã', 'laranja', 'morango', 'uva']
print(f"Lista Original: {lista_original}")

# --- Cópia de Listas ---

# Forma 1: Usando o método copy()
# Isso cria uma nova lista independente da original.
lista_copia = lista_original.copy()
print(f"Lista Copiada com copy(): {lista_copia}")

# Forma 2: Usando fatiamento [:]
# Esta é outra forma de criar uma cópia completa da lista.
lista_copia_fatiamento = lista_original[:]
print(f"Lista Copiada com Fatiamento [:]: {lista_copia_fatiamento}")

# Modificando a cópia para provar que a original não muda
lista_copia.append('abacaxi')
print(f"\nLista Cópia Modificada: {lista_copia}")
print(f"Lista Original (não mudou): {lista_original}")

# --- Fatiamento (Slicing) de Listas ---

# Fatiar é pegar "pedaços" da lista. A sintaxe é lista[inicio:fim:passo]

# Pegando os 3 primeiros elementos (do índice 0 até o 2)
primeiros_elementos = lista_original[0:3]
print(f"\nFatiamento - 3 primeiros elementos: {primeiros_elementos}")

# Pegando os elementos do índice 2 até o final
do_meio_para_frente = lista_original[2:]
print(f"Fatiamento - Do índice 2 até o fim: {do_meio_para_frente}")

# Pegando os 2 últimos elementos
ultimos_elementos = lista_original[-2:]
print(f"Fatiamento - 2 últimos elementos: {ultimos_elementos}")

# Pegando elementos com um "passo" (step) de 2 em 2
de_dois_em_dois = lista_original[::2]
print(f"Fatiamento - Pulando de 2 em 2: {de_dois_em_dois}")

# Invertendo a lista com fatiamento
lista_invertida = lista_original[::-1]
print(f"Fatiamento - Lista invertida: {lista_invertida}")

# --- Cuidado: Atribuição não é cópia! ---
# Se você apenas atribuir uma lista a outra variável, ambas apontarão
# para o MESMO objeto na memória.
lista_referencia = lista_original
lista_referencia.append('melancia')

print(f"\nLista por referência após adicionar 'melancia': {lista_referencia}")
print(f"Lista Original também foi modificada: {lista_original}")
