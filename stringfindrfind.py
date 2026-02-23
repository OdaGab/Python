frase = "O Python é uma linguagem de programação poderosa e versátil."

# Exemplo de uso do método find()
# Procura a primeira ocorrência da substring "é"
indice_find = frase.find("é")
print(f"A substring 'é' foi encontrada no índice: {indice_find}")

# Procura a substring "Java"
indice_nao_encontrado = frase.find("Java")
print(f"A substring 'Java' foi encontrada no índice: {indice_nao_encontrado} (não encontrada)")


# Exemplo de uso do método rfind()
# Procura a última ocorrência da substring "a"
indice_rfind = frase.rfind("a")
print(f"A última ocorrência da substring 'a' foi encontrada no índice: {indice_rfind}")

# Procura a partir de um índice específico
indice_find_a_partir_do_meio = frase.find("a", 20)
print(f"Procurando 'a' a partir do índice 20, foi encontrada no índice: {indice_find_a_partir_do_meio}")
