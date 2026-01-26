frase = "O Python é uma linguagem de programação poderosa e versátil."

# Exemplo de uso do método index()
# Procura a primeira ocorrência da substring "linguagem"
try:
    indice = frase.index("linguagem")
    print(f"A substring 'linguagem' foi encontrada no índice: {indice}")
except ValueError:
    print("A substring 'linguagem' não foi encontrada.")

# Tentando encontrar uma substring que não existe
try:
    indice_nao_encontrado = frase.index("Java")
    print(f"A substring 'Java' foi encontrada no índice: {indice_nao_encontrado}")
except ValueError:
    print("A substring 'Java' não foi encontrada, e um ValueError foi lançado.")


# Exemplo de uso do método rindex()
# Procura a última ocorrência da substring "a"
try:
    indice_rindex = frase.rindex("a")
    print(f"A última ocorrência da substring 'a' foi encontrada no índice: {indice_rindex}")
except ValueError:
    print("A substring 'a' não foi encontrada.")

# Tentando encontrar uma substring que não existe com rindex
try:
    indice_rindex_nao_encontrado = frase.rindex("Z")
    print(f"A substring 'Z' foi encontrada no índice: {indice_rindex_nao_encontrado}")
except ValueError:
    print("A substring 'Z' não foi encontrada com rindex, e um ValueError foi lançado.")
