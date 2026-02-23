
# Formatação de Strings com o método .format()

# O método .format() é uma maneira poderosa e flexível de formatar strings,
# substituindo placeholders (marcados por {}) por valores.

# --- Exemplos Básicos ---

# 1. Por ordem posicional
ordem_posicional = "Olá, meu nome é {} e eu tenho {} anos.".format("Alice", 30)
print(f"Posicional: {ordem_posicional}")

# 2. Por índice
por_indice = "Eu gosto de {0} e {1}, mas {0} é minha favorita.".format("maçã", "banana")
print(f"Por Índice: {por_indice}")

# 3. Por nome (argumentos nomeados)
por_nome = "O carro é um {modelo} {ano} da cor {cor}.".format(modelo="Fusca", ano=1970, cor="azul")
print(f"Por Nome:   {por_nome}")


# --- Formatação Avançada com .format() ---

# Podemos controlar o alinhamento, preenchimento e tipo de dado.
# Sintaxe: {nome_ou_indice:preenchimento alinhamento largura .precisão tipo}

numero = 123.4567

# Alinhamento
print("\n--- Alinhamento ---")
print("'{: >20}'".format("direita"))  # Alinha à direita em 20 espaços
print("'{: <20}'".format("esquerda")) # Alinha à esquerda
print("'{: ^20}'".format("centro"))   # Centraliza

# Preenchimento e Alinhamento
print("\n--- Preenchimento ---")
print("'{:*^20}'".format("centro")) # Centraliza com '*' como preenchimento

# Controle de Casas Decimais (Precisão)
print("\n--- Precisão Numérica ---")
print("Número original: {}".format(numero))
print("Com 2 casas decimais: {:.2f}".format(numero)) # 'f' para float

# Formatação como porcentagem
print("\n--- Porcentagem ---")
print("Como porcentagem: {:.1%}".format(0.758)) # 75.8%

# Formatação como moeda
print("\n--- Moeda ---")
valor = 1234.56
print("Valor em moeda: R$ {:,.2f}".format(valor)) # R$ 1,234.56 

# --- Formatação de Números Inteiros ---
inteiro = 255
print("\n--- Formatação de Inteiros (base 255) ---")
print(f"Decimal (d):     {inteiro:d}")
print(f"Caractere (c):   '{inteiro:c}' (Corresponde a Tabela ASCII)") # Requer um inteiro pequeno
print(f"Binário (b):     {inteiro:b}")
print(f"Octal (o):       {inteiro:o}")
print(f"Hexadecimal (x): {inteiro:x}")
print(f"Hexadecimal (X): {inteiro:X}")

# O 'n' é similar ao 'd', mas usa a configuração de localidade 
# para inserir separadores apropriados.
numero_grande = 1234567
print("\n--- Formato de Número (n) ---")
# Em localidades que usam ',', o resultado seria "1,234,567"
# A exibição exata depende da configuração do sistema operacional.
import locale
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    print(f"Formato 'n' (pt_BR): {numero_grande:n}") 
except locale.Error:
    print(f"Formato 'n' (padrão): {numero_grande:n} (locale 'pt_BR.UTF-8' não suportado)")


# --- Formatação de Números Decimais ---
decimal_num = 12345.6789
print("\n--- Formatação de Números Decimais (base 12345.6789) ---")
print(f"Notação Científica (e): {decimal_num:e}")
print(f"Notação Científica (E): {decimal_num:E}")
print(f"Ponto Fixo (f):         {decimal_num:f}")
print(f"Geral (g):              {decimal_num:g}") # Usa 'e' se o expoente for grande
print(f"Geral (G):              {decimal_num:G}") # Usa 'E' se o expoente for grande
print(f"Número (n):             {decimal_num:n}") # Usa configuração de localidade
print(f"Porcentagem (%):        {0.8912:.2%}")   # Multiplica por 100 e adiciona %

