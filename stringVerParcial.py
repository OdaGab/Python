# Verificação Parcial de String - startswith() e endswith()

"""
OBSERVAÇÃO SOBRE startswith() e endswith():

startswith(): Verifica se uma string COMEÇA com um prefixo especificado
Sintaxe: string.startswith(prefixo, início, fim)

endswith(): Verifica se uma string TERMINA com um sufixo especificado
Sintaxe: string.endswith(sufixo, início, fim)

Ambas retornam True ou False
"""

nome_completo = "Odair Gabriel"

print("=" * 50)
print("EXEMPLOS COM O NOME: Odair Gabriel")
print("=" * 50)

print("\n--- Usando startswith() ---\n")

# Verificando se começa com "Odair"
if nome_completo.startswith("Odair"):
    print(f"✓ '{nome_completo}' começa com 'Odair'")
else:
    print(f"✗ '{nome_completo}' não começa com 'Odair'")

# Verificando se começa com "Gabriel"
if nome_completo.startswith("Gabriel"):
    print(f"✓ '{nome_completo}' começa com 'Gabriel'")
else:
    print(f"✗ '{nome_completo}' não começa com 'Gabriel'")

# Verificando se começa com "O"
if nome_completo.startswith("O"):
    print(f"✓ '{nome_completo}' começa com 'O'")
else:
    print(f"✗ '{nome_completo}' não começa com 'O'")

print("\n--- Usando endswith() ---\n")

# Verificando se termina com "Gabriel"
if nome_completo.endswith("Gabriel"):
    print(f"✓ '{nome_completo}' termina com 'Gabriel'")
else:
    print(f"✗ '{nome_completo}' não termina com 'Gabriel'")

# Verificando se termina com "Odair"
if nome_completo.endswith("Odair"):
    print(f"✓ '{nome_completo}' termina com 'Odair'")
else:
    print(f"✗ '{nome_completo}' não termina com 'Odair'")

# Verificando se termina com "l"
if nome_completo.endswith("l"):
    print(f"✓ '{nome_completo}' termina com 'l'")
else:
    print(f"✗ '{nome_completo}' não termina com 'l'")

print("\n--- Verificações com múltiplas opções ---\n")

# Verificando se começa com múltiplos prefixos (usando tupla)
prefixos = ("Odair", "Gabriel", "João")
if nome_completo.startswith(prefixos):
    print(f"✓ '{nome_completo}' começa com um dos prefixos: {prefixos}")
else:
    print(f"✗ '{nome_completo}' não começa com nenhum desses prefixos")

# Verificando se termina com múltiplos sufixos (usando tupla)
sufixos = ("Gabriel", "Silva", "Costa")
if nome_completo.endswith(sufixos):
    print(f"✓ '{nome_completo}' termina com um dos sufixos: {sufixos}")
else:
    print(f"✗ '{nome_completo}' não termina com nenhum desses sufixos")

print("\n" + "=" * 50)
print("APLICAÇÕES PRÁTICAS")
print("=" * 50 + "\n")

# Exemplo 1: Validando emails
emails = ["odair@gmail.com", "gabriel@hotmail.com", "usuario@example"]

print("Validando extensões de email:\n")
for email in emails:
    if email.endswith(".com"):
        print(f"✓ {email} - Email válido")
    else:
        print(f"✗ {email} - Email inválido")

print("\n")

# Exemplo 2: Verificando tipos de arquivo
arquivos = ["documento.pdf", "imagem.jpg", "video.mp4", "musica.mp3"]

print("Verificando arquivos de imagem (jpg, png):\n")
for arquivo in arquivos:
    if arquivo.endswith((".jpg", ".png")):
        print(f"✓ {arquivo} - É uma imagem")
    else:
        print(f"✗ {arquivo} - Não é uma imagem")
