
# .split()
# Divide uma string em uma lista de substrings com base em um delimitador.
# Se nenhum delimitador for especificado, ele divide por espaços em branco.

texto = "Esta é uma string de exemplo"
palavras = texto.split()
print(f"String original: '{texto}'")
print(f"Lista de palavras: {palavras}")

data = "27/01/2026"
elementos_data = data.split('/')
print(f"Data original: '{data}'")
print(f"Elementos da data: {elementos_data}")


# .splitlines()
# Divide a string em uma lista de linhas, quebrando nas quebras de linha (\n).

texto_multilinha = "Primeira linha\nSegunda linha\nTerceira linha"
linhas = texto_multilinha.splitlines()
print("\nString multilinha:")
print(texto_multilinha)
print(f"Lista de linhas: {linhas}")

# Mantendo as quebras de linha
linhas_com_quebra = texto_multilinha.splitlines(keepends=True)
print(f"Lista de linhas (mantendo a quebra): {linhas_com_quebra}")
