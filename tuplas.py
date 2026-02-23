# Tuplas em Python

print("="*60)
print("TUPLAS EM PYTHON")
print("="*60 + "\n")

# Explicação
print("O QUE É UMA TUPLA?\n")
print("""
Uma tupla é uma sequência de elementos imutável (não pode ser modificada).

Características:
✓ Imutável (não pode ser modificada)
✓ Ordenada (mantém ordem)
✓ Acessa por índice (como listas)
✓ Pode conter diferentes tipos
✓ Usa parênteses: ()

Sintaxe: tupla = (elemento1, elemento2, elemento3)
""")

print("="*60 + "\n")

# 1. Criando tuplas
print("1. CRIANDO TUPLAS:\n")

# Tupla vazia
tupla_vazia = ()
print(f"Tupla vazia: {tupla_vazia}")

# Tupla com um elemento (precisa de vírgula!)
tupla_um = (42,)
print(f"Tupla com um elemento: {tupla_um}")

# Tupla com vários elementos
tupla_numeros = (1, 2, 3, 4, 5)
print(f"Tupla de números: {tupla_numeros}")

# Tupla com strings
tupla_palavras = ("Python", "é", "incrível")
print(f"Tupla de strings: {tupla_palavras}")

# Tupla mista
tupla_mista = ("João", 25, 8.5, True)
print(f"Tupla mista: {tupla_mista}")

# Sem parênteses (ainda é tupla!)
tupla_implícita = 5, 10, 15
print(f"Tupla sem parênteses: {tupla_implícita}\n")

print("="*60 + "\n")

# 2. Acessando elementos
print("2. ACESSANDO ELEMENTOS:\n")

tupla = ("a", "b", "c", "d", "e")
print(f"Tupla: {tupla}\n")

print(f"Primeiro elemento: {tupla[0]}")
print(f"Último elemento: {tupla[-1]}")
print(f"Índice 2: {tupla[2]}")
print(f"Índice -2: {tupla[-2]}\n")

print("="*60 + "\n")

# 3. Tuplas são imutáveis
print("3. TUPLAS SÃO IMUTÁVEIS:\n")

tupla = (1, 2, 3)
print(f"Tupla original: {tupla}\n")

print("Tentando modificar:")
try:
    tupla[0] = 99
except TypeError as e:
    print(f"❌ Erro: {e}\n")

print("Tentando adicionar:")
try:
    tupla.append(4)
except AttributeError as e:
    print(f"❌ Erro: Tuplas não têm append\n")

print("✓ Tuplas são imutáveis (proteção de dados)")
print("✓ Listas podem ser modificadas\n")

print("="*60 + "\n")

# 4. Fatiamento de tuplas
print("4. FATIAMENTO DE TUPLAS:\n")

tupla = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"Tupla: {tupla}\n")

print(f"tupla[2:5]: {tupla[2:5]}")
print(f"tupla[:3]: {tupla[:3]}")
print(f"tupla[6:]: {tupla[6:]}")
print(f"tupla[::2]: {tupla[::2]}")
print(f"tupla[::-1]: {tupla[::-1]}\n")

print("="*60 + "\n")

# 5. Iterando sobre tuplas
print("5. ITERANDO SOBRE TUPLAS:\n")

cores = ("vermelho", "verde", "azul")
print("Com for simples:")
for cor in cores:
    print(f"  - {cor}")

print("\nCom enumerate:")
for i, cor in enumerate(cores):
    print(f"  {i}: {cor}")

print()

print("="*60 + "\n")

# 6. Métodos de tuplas
print("6. MÉTODOS DE TUPLAS:\n")

tupla = (1, 2, 3, 2, 4, 2, 5)
print(f"Tupla: {tupla}\n")

# count() - contar ocorrências
print(f"Quantas vezes 2 aparece: {tupla.count(2)}")
print(f"Quantas vezes 1 aparece: {tupla.count(1)}\n")

# index() - encontrar índice
print(f"Índice do 3: {tupla.index(3)}")
print(f"Índice do 4: {tupla.index(4)}\n")

# len() - tamanho
print(f"Tamanho: {len(tupla)}\n")

# in - verificar se existe
print(f"2 está na tupla? {2 in tupla}")
print(f"10 está na tupla? {10 in tupla}\n")

print("="*60 + "\n")

# 7. Empacotamento e desempacotamento
print("7. EMPACOTAMENTO E DESEMPACOTAMENTO:\n")

# Empacotamento
a = 1
b = 2
c = 3
tupla = (a, b, c)
print(f"Empacotamento: {tupla}\n")

# Desempacotamento
x, y, z = (10, 20, 30)
print(f"Desempacotamento: x={x}, y={y}, z={z}\n")

# Desempacotamento com _
nome, _, idade = ("João", 25, "São Paulo")
print(f"Ignorando segundo valor: nome={nome}, idade={idade}\n")

# Desempacotamento com *
primeiro, *meio, ultimo = (1, 2, 3, 4, 5)
print(f"primeiro={primeiro}, meio={meio}, ultimo={ultimo}\n")

print("="*60 + "\n")

# 8. Tuplas como chaves de dicionário
print("8. TUPLAS COMO CHAVES DE DICIONÁRIO:\n")

# Tuplas são hashable (imutáveis) - podem ser chaves
coordenadas = {
    (0, 0): "origem",
    (1, 2): "ponto A",
    (3, 4): "ponto B"
}

print("Coordenadas:")
for coord, nome in coordenadas.items():
    print(f"  {coord}: {nome}")

print(f"\nValor em (1, 2): {coordenadas[(1, 2)]}\n")

print("❌ Não pode usar lista como chave (mutável)")
print("✓ Pode usar tupla como chave (imutável)\n")

print("="*60 + "\n")

# 9. Tuplas aninhadas
print("9. TUPLAS ANINHADAS:\n")

matriz = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 9)
)

print("Matriz como tupla de tuplas:")
for linha in matriz:
    print(f"  {linha}")

print(f"\nElemento [1][2]: {matriz[1][2]}")
print(f"Primeira linha: {matriz[0]}\n")

print("="*60 + "\n")

# 10. Tuplas vs Listas
print("10. COMPARAÇÃO: TUPLAS vs LISTAS:\n")

print("""
┌─────────────────────────────────────────────────────┐
│ TUPLAS (Imutáveis)                                  │
└─────────────────────────────────────────────────────┘
✓ Não pode modificar
✓ Mais rápidas
✓ Pode usar como chave de dicionário
✓ Proteção de dados
  tupla = (1, 2, 3)

┌─────────────────────────────────────────────────────┐
│ LISTAS (Mutáveis)                                   │
└─────────────────────────────────────────────────────┘
✓ Pode modificar
✓ Mais funcionalidades
✓ Não pode usar como chave
✓ Mais flexível
  lista = [1, 2, 3]
""")

print("="*60 + "\n")

# 11. Exemplo prático: Coordenadas GPS
print("11. EXEMPLO: COORDENADAS GPS:\n")

locais = {
    (-23.5505, -46.6333): "São Paulo",
    (-22.9068, -43.1729): "Rio de Janeiro",
    (-30.0346, -51.2177): "Porto Alegre"
}

print("Coordenadas de cidades:\n")
for (lat, lon), cidade in locais.items():
    print(f"{cidade:20} {lat:10.4f}, {lon:10.4f}")

print()

print("="*60 + "\n")

# 12. Exemplo prático: Dados de pessoa
print("12. EXEMPLO: DADOS DE PESSOA:\n")

pessoa = ("João Silva", 25, "São Paulo", "joao@email.com")

nome, idade, cidade, email = pessoa

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Cidade: {cidade}")
print(f"Email: {email}\n")

print("="*60 + "\n")

# 13. Exemplo prático: Retorno de função
print("13. EXEMPLO: FUNÇÃO RETORNANDO TUPLA:\n")

def obter_info_usuario():
    """Retorna tupla com dados do usuário"""
    return ("Maria", 30, "maria@email.com")

nome, idade, email = obter_info_usuario()
print(f"Usuário: {nome}, {idade} anos")
print(f"Email: {email}\n")

# Função retornando múltiplos valores
def calcular(a, b):
    """Retorna soma e produto"""
    return (a + b, a * b)

soma, produto = calcular(5, 3)
print(f"5 + 3 = {soma}")
print(f"5 × 3 = {produto}\n")

print("="*60 + "\n")

# 14. Tuplas com valores únicos
print("14. TUPLAS PARA DADOS IMUTÁVEIS:\n")

# Constantes
CORES_PRIMARIAS = ("vermelho", "azul", "amarelo")
DIAS_SEMANA = ("seg", "ter", "qua", "qui", "sex", "sab", "dom")

print(f"Cores primárias: {CORES_PRIMARIAS}")
print(f"Dias da semana: {DIAS_SEMANA}\n")

print("Vantagem: protege os dados contra modificação\n")

print("="*60 + "\n")

# 15. Convertendo entre tipos
print("15. CONVERTENDO ENTRE TIPOS:\n")

# Lista para tupla
lista = [1, 2, 3, 4, 5]
tupla = tuple(lista)
print(f"Lista {lista} → Tupla {tupla}")

# Tupla para lista
tupla = (10, 20, 30)
lista = list(tupla)
print(f"Tupla {tupla} → Lista {lista}")

# String para tupla
string = "Python"
tupla = tuple(string)
print(f"String '{string}' → Tupla {tupla}\n")

print("="*60 + "\n")

# 16. Operações com tuplas
print("16. OPERAÇÕES COM TUPLAS:\n")

t1 = (1, 2, 3)
t2 = (4, 5, 6)

# Concatenação
t3 = t1 + t2
print(f"{t1} + {t2} = {t3}")

# Repetição
t4 = (1, 2) * 3
print(f"(1, 2) * 3 = {t4}")

# Tamanho
print(f"len({t1}) = {len(t1)}")

# Mínimo e máximo
numeros = (5, 2, 8, 1, 9)
print(f"min({numeros}) = {min(numeros)}")
print(f"max({numeros}) = {max(numeros)}")

# Soma
print(f"sum({numeros}) = {sum(numeros)}\n")

print("="*60 + "\n")

# 17. Quando usar tuplas
print("17. QUANDO USAR TUPLAS:\n")

print("""
USE TUPLAS QUANDO:
✓ Dados não devem ser modificados
✓ Usar como chave de dicionário
✓ Retornar múltiplos valores de função
✓ Performance é importante (tuplas são mais rápidas)
✓ Proteger dados de modificação acidental
✓ Usar em sets (apenas tuplas, não listas)

EXEMPLOS:
• Coordenadas (x, y)
• Datas (dia, mês, ano)
• RGB de cores (r, g, b)
• Dados de configuração
• Resultados de função
""")

print("="*60 + "\n")

# 18. Resumo
print("18. RESUMO:\n")

print(f"""
CRIAÇÃO:
  tupla = ()                    # Vazia
  tupla = (1,)                  # Um elemento
  tupla = (1, 2, 3)             # Múltiplos

ACESSO:
  tupla[0]                      # Primeiro
  tupla[-1]                     # Último
  tupla[1:3]                    # Fatia

ITERAÇÃO:
  for item in tupla:
      print(item)

DESEMPACOTAMENTO:
  a, b, c = (1, 2, 3)

OPERAÇÕES:
  len(tupla)                    # Tamanho
  item in tupla                 # Pertence
  tupla.count(item)             # Contar
  tupla.index(item)             # Índice

CONCATENAÇÃO:
  tupla1 + tupla2               # Junta

CARACTERÍSTICAS:
  ✓ Imutável (não modifica)
  ✓ Mais rápida que lista
  ✓ Pode ser chave de dict
  ✓ Hashable (única, constante)
""")

print("="*60)
