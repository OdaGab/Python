# Exemplo de in e not in - Verificação de Substring

"""
OBSERVAÇÃO SOBRE in e not in:

in: Verifica se uma substring EXISTE dentro de uma string
Sintaxe: substring in string
Retorna: True ou False

not in: Verifica se uma substring NÃO EXISTE dentro de uma string
Sintaxe: substring not in string
Retorna: True ou False

São operadores lógicos muito úteis para buscas simples em textos
"""

# Texto de exemplo
texto = "Odair Gabriel é um programador Python"

print("=" * 50)
print("VERIFICAÇÃO DE SUBSTRING")
print("=" * 50)

print(f"\nTexto: '{texto}'\n")

print("--- Usando in ---\n")

# Verificando se "Odair" está no texto
if "Odair" in texto:
    print("✓ 'Odair' está no texto")
else:
    print("✗ 'Odair' não está no texto")

# Verificando se "Gabriel" está no texto
if "Gabriel" in texto:
    print("✓ 'Gabriel' está no texto")
else:
    print("✗ 'Gabriel' não está no texto")

# Verificando se "Java" está no texto
if "Java" in texto:
    print("✓ 'Java' está no texto")
else:
    print("✗ 'Java' não está no texto")

print("\n--- Usando not in ---\n")

# Verificando se "JavaScript" NÃO está no texto
if "JavaScript" not in texto:
    print("✓ 'JavaScript' não está no texto")
else:
    print("✗ 'JavaScript' está no texto")

# Verificando se "Python" NÃO está no texto
if "Python" not in texto:
    print("✓ 'Python' não está no texto")
else:
    print("✗ 'Python' está no texto")

print("\n" + "=" * 50)
print("EXEMPLOS PRÁTICOS")
print("=" * 50 + "\n")

# Exemplo 1: Validando email
print("Exemplo 1: Validando email\n")

emails = ["odair@gmail.com", "gabriel@hotmail.com", "usuario123"]

for email in emails:
    if "@" in email and "." in email:
        print(f"✓ {email} - Parece ser um email válido")
    else:
        print(f"✗ {email} - Email inválido")

print()

# Exemplo 2: Verificando palavras-chave
print("Exemplo 2: Verificando palavras-chave\n")

mensagem = "Aprendendo Python é muito importante"

palavras_chave = ["Python", "Java", "JavaScript", "C++"]

for palavra in palavras_chave:
    if palavra in mensagem:
        print(f"✓ Encontrado: '{palavra}' na mensagem")
    else:
        print(f"✗ Não encontrado: '{palavra}'")

print()

# Exemplo 3: Filtro de conteúdo
print("Exemplo 3: Verificando termos proibidos\n")

textos = [
    "Este é um ótimo conteúdo",
    "Este texto contém spam indesejado",
    "Conteúdo limpo e seguro"
]

termos_proibidos = ["spam", "publicidade", "fraude"]

for texto in textos:
    tem_termo_proibido = False
    for termo in termos_proibidos:
        if termo.lower() in texto.lower():
            print(f"✗ '{texto}' - Contém termo proibido: '{termo}'")
            tem_termo_proibido = True
            break
    
    if not tem_termo_proibido:
        print(f"✓ '{texto}' - Conteúdo aprovado")

print()

# Exemplo 4: Busca simples
print("Exemplo 4: Busca com in e not in\n")

nome = "Odair Gabriel"

if "Odair" in nome and "Gabriel" in nome:
    print(f"✓ '{nome}' contém ambos os nomes")
else:
    print(f"✗ Faltam nomes")

if "Silva" not in nome:
    print(f"✓ '{nome}' não contém 'Silva'")
else:
    print(f"✗ '{nome}' contém 'Silva'")
