# Exemplo de lower() e upper() - Conversão de Caso

"""
OBSERVAÇÃO SOBRE lower() e upper():

lower(): Converte todos os caracteres de uma string para MINÚSCULAS
Sintaxe: string.lower()

upper(): Converte todos os caracteres de uma string para MAIÚSCULAS
Sintaxe: string.upper()

Ambas retornam uma nova string sem modificar a original
"""

# Texto de exemplo
texto = "Odair Gabriel"

print("=" * 50)
print("CONVERSÃO DE CASO")
print("=" * 50)

print(f"\nTexto original: {texto}")

# Usando lower()
print(f"\nUsando lower(): {texto.lower()}")

# Usando upper()
print(f"Usando upper(): {texto.upper()}")

print("\n" + "=" * 50)
print("EXEMPLOS PRÁTICOS")
print("=" * 50 + "\n")

# Exemplo 1: Padronizando entrada de usuário
print("Exemplo 1: Comparação ignorando maiúsculas/minúsculas\n")

nome_usuario = "ODAIR GABRIEL"
nome_esperado = "odair gabriel"

if nome_usuario.lower() == nome_esperado:
    print(f"✓ Nome '{nome_usuario}' está correto (após conversão)")
else:
    print(f"✗ Nome não coincide")

print()

# Exemplo 2: Formatando strings
print("Exemplo 2: Formatando diferentes casos\n")

frase = "Bem-vindo ao Python"

print(f"Original:     {frase}")
print(f"Minúsculas:   {frase.lower()}")
print(f"Maiúsculas:   {frase.upper()}")
print(f"Primeira mai: {frase[0].upper() + frase[1:].lower()}")

print()

# Exemplo 3: Buscando em textos
print("Exemplo 3: Busca insensível a maiúsculas/minúsculas\n")

texto_busca = "Python é Incrível"
termo = "PYTHON"

if termo.lower() in texto_busca.lower():
    print(f"✓ Encontrado '{termo}' em '{texto_busca}'")
else:
    print(f"✗ Não encontrado")

print()

# Exemplo 4: Lista de nomes
print("Exemplo 4: Padronizando lista de nomes\n")

nomes = ["odair gabriel", "JOÃO SILVA", "Maria Santos", "CARLOS OLIVEIRA"]

print("Nomes originais:")
for nome in nomes:
    print(f"  - {nome}")

print("\nNomes em minúsculas:")
for nome in nomes:
    print(f"  - {nome.lower()}")

print("\nNomes em maiúsculas:")
for nome in nomes:
    print(f"  - {nome.upper()}")
