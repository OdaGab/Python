# Conjuntos (Set) em Python

print("="*60)
print("CONJUNTOS (SET) EM PYTHON")
print("="*60 + "\n")

# Explicação
print("O QUE É UM SET?\n")
print("""
Um set é uma coleção desordenada de elementos únicos.

Características:
✓ Sem ordem
✓ Sem duplicatas (valores únicos)
✓ Mutável (pode ser modificado)
✓ Não acessa por índice
✓ Usa chaves: {}

Sintaxe: conjunto = {elemento1, elemento2, elemento3}

Nota: {} vazio é dicionário, use set() para set vazio
""")

print("="*60 + "\n")

# 1. Criando sets
print("1. CRIANDO SETS:\n")

# Set vazio (cuidado: {} é dicionário!)
conjunto_vazio = set()
print(f"Set vazio: {conjunto_vazio}")

# Set com elementos
numeros = {1, 2, 3, 4, 5}
print(f"Set de números: {numeros}")

# Set com strings
cores = {"vermelho", "azul", "verde"}
print(f"Set de cores: {cores}")

# Set com múltiplos tipos
misto = {1, "texto", 3.14, True}
print(f"Set misto: {misto}")

# Criando a partir de lista (remove duplicatas)
lista = [1, 2, 2, 3, 3, 3, 4]
conjunto = set(lista)
print(f"Lista {lista} → Set {conjunto}")

# Criando a partir de string
letras = set("python")
print(f"String 'python' → Set {letras}\n")

print("="*60 + "\n")

# 2. Sets removem duplicatas
print("2. REMOVENDO DUPLICATAS:\n")

numeros_duplicados = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
print(f"Lista com duplicatas: {numeros_duplicados}")

conjunto = set(numeros_duplicados)
print(f"Convertido para set: {conjunto}")
print(f"Lista novamente: {list(conjunto)}\n")

print("="*60 + "\n")

# 3. Adicionando elementos
print("3. ADICIONANDO ELEMENTOS:\n")

frutas = {"maçã", "banana"}
print(f"Set original: {frutas}")

frutas.add("laranja")
print(f"Após add('laranja'): {frutas}")

frutas.add("maçã")  # Tenta adicionar duplicata
print(f"Após add('maçã'): {frutas} (sem duplicata)\n")

print("="*60 + "\n")

# 4. Removendo elementos
print("4. REMOVENDO ELEMENTOS:\n")

numeros = {1, 2, 3, 4, 5}
print(f"Set original: {numeros}")

# remove() - erro se não existe
numeros.remove(3)
print(f"Após remove(3): {numeros}")

# discard() - não erro se não existe
numeros.discard(10)
print(f"Após discard(10): {numeros}")

# pop() - remove um elemento aleatório
removido = numeros.pop()
print(f"pop() removeu: {removido}")
print(f"Set após pop: {numeros}")

# clear() - remove tudo
numeros.clear()
print(f"Após clear(): {numeros}\n")

print("="*60 + "\n")

# 5. Operações matemáticas com sets
print("5. OPERAÇÕES MATEMÁTICAS:\n")

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}

print(f"Set A: {a}")
print(f"Set B: {b}\n")

# União (todos os elementos)
uniao = a | b
print(f"A | B (união): {uniao}")

uniao2 = a.union(b)
print(f"a.union(b): {uniao2}\n")

# Intersecção (elementos em comum)
intersecao = a & b
print(f"A & B (intersecção): {intersecao}")

intersecao2 = a.intersection(b)
print(f"a.intersection(b): {intersecao2}\n")

# Diferença (em A mas não em B)
diferenca = a - b
print(f"A - B (diferença): {diferenca}")

diferenca2 = a.difference(b)
print(f"a.difference(b): {diferenca2}\n")

# Diferença simétrica (em A ou B, mas não em ambos)
sim_diferenca = a ^ b
print(f"A ^ B (diferença simétrica): {sim_diferenca}")

sim_diferenca2 = a.symmetric_difference(b)
print(f"a.symmetric_difference(b): {sim_diferenca2}\n")

print("="*60 + "\n")

# 6. Verificando pertencimento
print("6. VERIFICANDO PERTENCIMENTO:\n")

numeros = {10, 20, 30, 40, 50}
print(f"Set: {numeros}\n")

print(f"10 in numeros: {10 in numeros}")
print(f"25 in numeros: {25 in numeros}")
print(f"50 in numeros: {50 in numeros}\n")

print("="*60 + "\n")

# 7. Iterando sobre sets
print("7. ITERANDO SOBRE SETS:\n")

cores = {"vermelho", "azul", "verde", "amarelo"}
print("Cores:")
for cor in cores:
    print(f"  - {cor}")

print("\nCom índice (enumerate):")
for i, cor in enumerate(cores):
    print(f"  {i}: {cor}")

print()

print("="*60 + "\n")

# 8. Comparando sets
print("8. COMPARANDO SETS:\n")

s1 = {1, 2, 3}
s2 = {1, 2, 3}
s3 = {1, 2, 3, 4}
s4 = {4, 5, 6}

print(f"s1 = {s1}")
print(f"s2 = {s2}")
print(f"s3 = {s3}")
print(f"s4 = {s4}\n")

print(f"s1 == s2: {s1 == s2} (iguais)")
print(f"s1 < s3: {s1 < s3} (subconjunto próprio)")
print(f"s3 > s1: {s3 > s1} (superconjunto)")
print(f"s1 <= s2: {s1 <= s2} (subconjunto ou igual)")
print(f"s1 & s4: {s1 & s4} (sem interseção)\n")

print("="*60 + "\n")

# 9. Métodos úteis
print("9. MÉTODOS ÚTEIS:\n")

conjunto = {1, 2, 3, 4, 5}
print(f"Set: {conjunto}\n")

print(f"len(): {len(conjunto)}")
print(f"min(): {min(conjunto)}")
print(f"max(): {max(conjunto)}")
print(f"sum(): {sum(conjunto)}\n")

print("="*60 + "\n")

# 10. Sets vs Listas
print("10. COMPARAÇÃO: SETS vs LISTAS:\n")

print("""
┌─────────────────────────────────────────────────────┐
│ SETS                                                │
└─────────────────────────────────────────────────────┘
✓ Sem duplicatas
✓ Sem ordem
✓ Mais rápido para buscar (hash)
✓ Operações matemáticas
✗ Não acessa por índice
✗ Não pode ter elementos mutáveis

┌─────────────────────────────────────────────────────┐
│ LISTAS                                              │
└─────────────────────────────────────────────────────┘
✓ Com ordem
✓ Acessa por índice
✓ Pode ter duplicatas
✓ Pode ter elementos mutáveis
✗ Mais lenta para buscar
✗ Sem operações matemáticas

USE SET PARA: Coleção única e desordenada
USE LISTA PARA: Sequência ordenada
""")

print("="*60 + "\n")

# 11. Exemplo prático: Encontrar elementos únicos
print("11. EXEMPLO: ELEMENTOS ÚNICOS:\n")

numeros = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
unicos = set(numeros)

print(f"Lista com repetições: {numeros}")
print(f"Elementos únicos: {sorted(unicos)}\n")

print("="*60 + "\n")

# 12. Exemplo prático: Encontrar diferença
print("12. EXEMPLO: ENCONTRAR DIFERENÇA:\n")

alunos_2024 = {"Ana", "Bruno", "Carlos", "Diana"}
alunos_2025 = {"Carlos", "Diana", "Eduardo", "Fernanda"}

novos = alunos_2025 - alunos_2024
saidos = alunos_2024 - alunos_2025
continuam = alunos_2024 & alunos_2025

print("Alunos 2024:", alunos_2024)
print("Alunos 2025:", alunos_2025)
print()
print(f"Novos alunos: {novos}")
print(f"Alunos que saíram: {saidos}")
print(f"Continuam: {continuam}\n")

print("="*60 + "\n")

# 13. Exemplo prático: Tags e categorias
print("13. EXEMPLO: TAGS DE ARTIGOS:\n")

artigo1_tags = {"python", "programação", "tutorial", "iniciante"}
artigo2_tags = {"python", "django", "web", "backend"}
artigo3_tags = {"javascript", "frontend", "web", "iniciante"}

print("Artigo 1:", artigo1_tags)
print("Artigo 2:", artigo2_tags)
print("Artigo 3:", artigo3_tags)
print()

todas_tags = artigo1_tags | artigo2_tags | artigo3_tags
print(f"Todas as tags: {sorted(todas_tags)}")

tags_python = artigo1_tags & artigo2_tags
print(f"Tags em comum (artigo 1 e 2): {tags_python}")

apenas_web = (artigo2_tags | artigo3_tags) - artigo1_tags
print(f"Tags web (2 ou 3) não em 1: {apenas_web}\n")

print("="*60 + "\n")

# 14. Frozenset (set imutável)
print("14. FROZENSET (SET IMUTÁVEL):\n")

congelado = frozenset({1, 2, 3, 4, 5})
print(f"Frozenset: {congelado}")

# Pode usar como chave de dicionário
localizacoes = {
    frozenset({"norte", "leste"}): "Nordeste",
    frozenset({"sul", "oeste"}): "Sudoeste",
    frozenset({"norte", "oeste"}): "Noroeste"
}

print("Localização:", localizacoes[frozenset({"norte", "leste"})])

print("\nTentando modificar:")
try:
    congelado.add(6)
except AttributeError as e:
    print(f"❌ Erro: Frozenset é imutável\n")

print("="*60 + "\n")

# 15. Convertendo sets
print("15. CONVERTENDO SETS:\n")

# Set para lista
conjunto = {5, 2, 8, 1}
lista = list(conjunto)
print(f"Set {conjunto} → Lista {sorted(lista)}")

# Set para tupla
tupla = tuple(conjunto)
print(f"Set {conjunto} → Tupla {tupla}")

# Set para string
caracteres = set("hello")
print(f"String 'hello' → Set {caracteres}\n")

print("="*60 + "\n")

# 16. Exemplo prático: Remover duplicatas
print("16. EXEMPLO: REMOVER DUPLICATAS:\n")

nomes_com_repeticao = ["Ana", "Bruno", "Ana", "Carlos", "Bruno", "Diana"]
nomes_unicos = list(set(nomes_com_repeticao))

print(f"Lista original: {nomes_com_repeticao}")
print(f"Sem duplicatas: {sorted(nomes_unicos)}\n")

print("="*60 + "\n")

# 17. Comprensão de sets
print("17. COMPREENSÃO DE SETS:\n")

# Números pares
pares = {n for n in range(1, 11) if n % 2 == 0}
print(f"Números pares (1-10): {pares}")

# Quadrados
quadrados = {n**2 for n in range(1, 6)}
print(f"Quadrados (1-5): {quadrados}")

# Primeiras letras
palavras = {"python", "java", "javascript", "ruby"}
primeiras = {p[0] for p in palavras}
print(f"Primeiras letras de {palavras}: {primeiras}\n")

print("="*60 + "\n")

# 18. Exemplo prático: Alunos inscritos
print("18. EXEMPLO: ALUNOS INSCRITOS:\n")

inscritos_python = {"Ana", "Bruno", "Carlos", "Diana", "Eduardo"}
inscritos_java = {"Bruno", "Diana", "Fernanda", "Gustavo"}
inscritos_web = {"Ana", "Carlos", "Fernanda", "Helena"}

# Alunos em todos os cursos
em_tudo = inscritos_python & inscritos_java & inscritos_web
print(f"Em todos os cursos: {em_tudo}")

# Alunos em pelo menos um curso
em_algum = inscritos_python | inscritos_java | inscritos_web
print(f"Em pelo menos um: {sorted(em_algum)}")

# Alunos apenas em Python
so_python = inscritos_python - inscritos_java - inscritos_web
print(f"Apenas Python: {so_python}\n")

print("="*60 + "\n")

# 19. Resumo
print("19. RESUMO:\n")

print(f"""
CRIAÇÃO:
  conjunto = {{1, 2, 3}}        # Com elementos
  vazio = set()                 # Vazio

ADICIONAR/REMOVER:
  conjunto.add(4)               # Adiciona
  conjunto.remove(1)            # Remove (erro se não existe)
  conjunto.discard(1)           # Remove (sem erro)
  conjunto.pop()                # Remove aleatório
  conjunto.clear()              # Limpa tudo

OPERAÇÕES MATEMÁTICAS:
  a | b                         # União
  a & b                         # Intersecção
  a - b                         # Diferença
  a ^ b                         # Diferença simétrica

VERIFICAÇÃO:
  item in conjunto              # Pertence
  len(conjunto)                 # Tamanho
  min(conjunto), max(conjunto)  # Mínimo/máximo

ITERAÇÃO:
  for item in conjunto:
      print(item)

CONVERSÃO:
  list(conjunto)                # Para lista
  tuple(conjunto)               # Para tupla
  set(lista)                    # Da lista

CARACTERÍSTICAS:
  ✓ Sem duplicatas
  ✓ Sem ordem
  ✓ Sem índice
  ✓ Operações rápidas
  ✓ Operações matemáticas

FROZENSET (imutável):
  congelado = frozenset({{1, 2, 3}})
  Pode ser chave de dicionário
""")

print("="*60)
