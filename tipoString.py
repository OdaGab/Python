"""
Exemplos de como trabalhar com strings em Python.
"""

# Criando uma string
minha_string = "Olá, Mundo!"
print(f"String original: {minha_string}")

# Concatenação de strings
outra_string = " Bem-vindo ao Python."
string_concatenada = minha_string + outra_string
print(f"String concatenada: {string_concatenada}")

# Métodos de string
print(f"Maiúsculas: {minha_string.upper()}")
print(f"Minúsculas: {minha_string.lower()}")

print(f"String original ainda é a mesma: {minha_string}")

# F-strings (formatação de strings)
nome = "Johann"
idade = 15
print(f"Olá, meu nome é {nome} e eu tenho {idade} anos.")

# Acessando caracteres individuais
primeiro_caractere = nome[0]
print(f"O primeiro caractere é: {primeiro_caractere}")

# Fatiamento (slicing) de strings
fatia = minha_string[0:5] # Pega os caracteres do índice 0 ao 4
print(f"A fatia de 0 a 5 é: {fatia}")
