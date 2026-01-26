# Em Python, os dicionários são a implementação padrão do tipo de dado abstrato "mapa"
# (também conhecido como mapa associativo ou array associativo).
# Eles armazenam pares de chave-valor.

# 1. Criando um dicionário (mapa)
# Vamos mapear o nome de uma pessoa para sua idade e cidade.
mapa_de_pessoas = {
    "João": 34,
    "Maria": 28,
    "Pedro": 45
}

print("--- Dicionário Inicial ---")
print(mapa_de_pessoas)
print("-" * 25)


# 2. Acessando um valor pela chave
# Para obter a idade de "Maria", usamos a chave "Maria"
idade_da_maria = mapa_de_pessoas["Maria"]
print(f"A idade de Maria é: {idade_da_maria}")
print("-" * 25)


# 3. Adicionando um novo par chave-valor (novo mapeamento)
# Vamos adicionar a "Ana" ao nosso mapa.
mapa_de_pessoas["Ana"] = 23
print("--- Dicionário Após Adicionar 'Ana' ---")
print(mapa_de_pessoas)
print("-" * 25)


# 4. Iterando sobre o mapa
print("--- Iterando sobre o mapa (chaves e valores) ---")
for nome, idade in mapa_de_pessoas.items():
    print(f"A pessoa '{nome}' tem {idade} anos.")
print("-" * 25)


# Exemplo um pouco mais complexo: Dicionários aninhados
# Um mapa onde a chave é o nome de um produto e o valor é outro mapa com detalhes.
mapa_de_produtos = {
    "Celular": {
        "preco": 1500.00,
        "estoque": 50
    },
    "Notebook": {
        "preco": 3500.50,
        "estoque": 20
    }
}

print("\n--- Mapa de Produtos (Dicionário Aninhado) ---")
# Acessando o preço do Notebook
preco_notebook = mapa_de_produtos["Notebook"]["preco"]
print(f"O preço do Notebook é: R$ {preco_notebook}")
print("-" * 25)
