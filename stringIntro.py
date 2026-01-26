# Exemplo de List e Join - Alteração de String

"""
OBSERVAÇÃO SOBRE split():
A finalidade do split() é dividir uma string em uma lista de substrings com base em um delimitador (separador).

Sintaxe: string.split(separador, máximo)
- separador (opcional): o caractere ou texto que marca o ponto de divisão. Padrão é espaço em branco
- máximo (opcional): número máximo de divisões a fazer

O split() é muito útil para:
- Processar linhas de texto
- Analisar dados formatados (CSV, valores separados por delimitadores)
- Quebrar sentenças em palavras
- Extrair componentes de uma string
"""

'''
O exemplo demonstra três casos práticos:

1. Dividir string em lista e juntar com novo separador - mostra como split() cria uma lista e join() reconstrói a string com um separador diferente
2. Converter string em lista de caracteres - utiliza list() para quebrar em caracteres individuais e join() para reconstruir
3. Trabalhar com lista de números - demonstra como usar join() com map() para converter uma lista em string

'''


# Exemplo 1: Convertendo uma string em lista e depois juntando novamente
texto_original = "Python é incrível"
print(f"Texto original: {texto_original}")

# Convertendo string em lista de palavras
palavras = texto_original.split()
print(f"Lista de palavras: {palavras}")

# Juntando a lista com um separador diferente
texto_modificado = " - ".join(palavras)
print(f"Texto modificado: {texto_modificado}")

print("\n" + "="*50 + "\n")

# Exemplo 2: Usando list() para converter string em caracteres
caracteres = list("Olá")
print(f"String em lista de caracteres: {caracteres}")

# Juntando os caracteres de volta
texto_reconstruido = "".join(caracteres)
print(f"String reconstruída: {texto_reconstruido}")

print("\n" + "="*50 + "\n")

# Exemplo 3: Manipulando uma lista e juntando
numeros = [1, 2, 3, 4, 5]
print(f"Lista de números: {numeros}")

# Convertendo números em string e juntando com vírgula
numeros_string = ",".join(map(str, numeros))
print(f"Números como string: {numeros_string}")
