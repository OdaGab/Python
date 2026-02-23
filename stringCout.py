# Exemplo de count() - Contagem de Substrings

"""
OBSERVAÇÃO SOBRE count():

count(): Conta quantas vezes uma substring aparece em uma string
Sintaxe: string.count(substring, início, fim)

Parâmetros:
- substring: o texto que será procurado e contado
- início (opcional): posição inicial da busca
- fim (opcional): posição final da busca

Retorna: Um inteiro com o número de ocorrências
"""

# Texto de exemplo
texto = "Odair Gabriel é um programador Python. Python é incrível!"

print("=" * 50)
print("CONTAGEM DE SUBSTRINGS")
print("=" * 50)

print(f"\nTexto: '{texto}'\n")

# Contando a palavra "Python"
contagem_python = texto.count("Python")
print(f"A palavra 'Python' aparece {contagem_python} vezes")

# Contando a letra "a"
contagem_a = texto.count("a")
print(f"A letra 'a' aparece {contagem_a} vezes")

# Contando a letra "i"
contagem_i = texto.count("i")
print(f"A letra 'i' aparece {contagem_i} vezes")

# Contando espaços
contagem_espacos = texto.count(" ")
print(f"Existem {contagem_espacos} espaços no texto")

print("\n" + "=" * 50)
print("EXEMPLOS PRÁTICOS")
print("=" * 50 + "\n")

# Exemplo 1: Contando vogais
print("Exemplo 1: Contando vogais\n")

vogais = "aeiou"
for vogal in vogais:
    contagem = texto.lower().count(vogal)
    print(f"Vogal '{vogal}': {contagem} vezes")

print()

# Exemplo 2: Analisando frequência de palavras
print("Exemplo 2: Frequência de palavras\n")

frase = "gato gato cachorro gato passaro cachorro"
palavras = ["gato", "cachorro", "passaro", "cobra"]

for palavra in palavras:
    freq = frase.count(palavra)
    if freq > 0:
        print(f"'{palavra}': aparece {freq} vezes")
    else:
        print(f"'{palavra}': não aparece no texto")

print()

# Exemplo 3: Contando com intervalo
print("Exemplo 3: Contando em partes do texto\n")

texto_completo = "AAABBBCCCDDDEEE"

# Contando 'A' no texto todo
total_a = texto_completo.count("A")
print(f"Total de 'A': {total_a}")

# Contando 'A' apenas na primeira metade
primeira_metade = len(texto_completo) // 2
a_primeira = texto_completo.count("A", 0, primeira_metade)
print(f"'A' na primeira metade (0 a {primeira_metade}): {a_primeira}")

# Contando 'A' apenas na segunda metade
a_segunda = texto_completo.count("A", primeira_metade)
print(f"'A' na segunda metade ({primeira_metade} em diante): {a_segunda}")

print()

# Exemplo 4: Validando entrada
print("Exemplo 4: Validando entrada de usuário\n")

emails = ["odair@gmail.com", "gabriel@@hotmail.com", "usuario@example.com"]

for email in emails:
    contagem_arroba = email.count("@")
    if contagem_arroba == 1:
        print(f"✓ {email} - Email válido")
    else:
        print(f"✗ {email} - Email inválido (@ aparece {contagem_arroba} vezes)")

print()

# Exemplo 5: Análise de texto
print("Exemplo 5: Análise de texto\n")

texto_analise = "Python Python Python Java JavaScript JavaScript C++"

linguagens = ["Python", "Java", "JavaScript", "C++"]

print("Ranking de linguagens mencionadas:")
for linguagem in linguagens:
    freq = texto_analise.count(linguagem)
    print(f"{linguagem}: {freq} menções")
