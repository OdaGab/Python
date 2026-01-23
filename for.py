# O loop 'for' é utilizado para iterar sobre uma sequência de elementos,
# como uma lista, uma tupla, um dicionário, uma string ou um range de números.

# Exemplo 1: Iterando sobre uma lista
print("--- Iterando sobre uma lista de frutas ---")
frutas = ["maçã", "banana", "laranja", "morango"]
for fruta in frutas:
    print(f"A fruta da vez é: {fruta}")

# Exemplo 2: Iterando sobre uma string
print("\n--- Iterando sobre uma string ---")
palavra = "Python"
for letra in palavra:
    print(f"Letra: {letra}")

# Exemplo 3: Utilizando a função range() para gerar números
# range(5) gera números de 0 a 4
print("\n--- Utilizando range(5) ---")
for numero in range(5):
    print(f"Número: {numero}")

# range(1, 6) gera números de 1 a 5
print("\n--- Utilizando range(1, 6) ---")
for numero in range(1, 6):
    print(f"Número: {numero}")

# Exemplo 4: Iterando sobre um dicionário
print("\n--- Iterando sobre um dicionário de contatos ---")
contatos = {
    "João": "joao@example.com",
    "Maria": "maria@example.com",
    "Pedro": "pedro@example.com"
}

# Iterando sobre as chaves
print("\nNomes (chaves) no dicionário:")
for nome in contatos:
    print(nome)

# Iterando sobre os valores
print("\nE-mails (valores) no dicionário:")
for email in contatos.values():
    print(email)

# Iterando sobre os itens (pares chave-valor)
print("\nContatos completos (chave e valor):")
for nome, email in contatos.items():
    print(f"O e-mail de {nome} é {email}")

# Exemplo 5: Usando enumerate para obter o índice e o valor
print("\n--- Usando enumerate para listar o ranking de filmes ---")
filmes_ranking = ["O Poderoso Chefão", "Um Sonho de Liberdade", "Batman: O Cavaleiro das Trevas"]
for i, filme in enumerate(filmes_ranking):
    print(f"#{i + 1}: {filme}")
