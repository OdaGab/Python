# Listas dentro de Listas (Listas Aninhadas / Matrizes)

print("="*60)
print("LISTAS DENTRO DE LISTAS (LISTAS ANINHADAS)")
print("="*60 + "\n")

# 1. Exemplo básico: Criando uma lista de listas
print("1. CRIANDO LISTAS ANINHADAS:\n")

# Uma matriz simples
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
print(matriz)
print(f"Tipo: {type(matriz)}")
print(f"Quantidade de linhas: {len(matriz)}")
print(f"Quantidade de colunas (primeira linha): {len(matriz[0])}\n")

print("="*60 + "\n")

# 2. Acessando elementos em listas aninhadas
print("2. ACESSANDO ELEMENTOS:\n")

print("Acessando elementos individuais:")
print(f"matriz[0] = {matriz[0]}      (primeira linha)")
print(f"matriz[1] = {matriz[1]}      (segunda linha)")
print(f"matriz[2] = {matriz[2]}      (terceira linha)\n")

print("Acessando elementos específicos:")
print(f"matriz[0][0] = {matriz[0][0]}  (linha 0, coluna 0)")
print(f"matriz[0][1] = {matriz[0][1]}  (linha 0, coluna 1)")
print(f"matriz[1][2] = {matriz[1][2]}  (linha 1, coluna 2)")
print(f"matriz[2][2] = {matriz[2][2]}  (linha 2, coluna 2)\n")

print("="*60 + "\n")

# 3. Modificando elementos em listas aninhadas
print("3. MODIFICANDO ELEMENTOS:\n")

matriz_modificada = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for linha in matriz_modificada:
    print(linha)

print("\nModificando matriz[1][1] de 5 para 99:")
matriz_modificada[1][1] = 99

print("Matriz modificada:")
for linha in matriz_modificada:
    print(linha)

print("\nModificando matriz[2][0] de 7 para 77:")
matriz_modificada[2][0] = 77

print("Matriz modificada:")
for linha in matriz_modificada:
    print(linha)

print("\n" + "="*60 + "\n")

# 4. Iterando sobre listas aninhadas
print("4. ITERANDO SOBRE LISTAS ANINHADAS:\n")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Usando for simples:")
for linha in matriz:
    print(linha)

print("\nUsando for aninhado (acessar cada elemento):")
for i, linha in enumerate(matriz):
    for j, elemento in enumerate(linha):
        print(f"matriz[{i}][{j}] = {elemento}", end="  ")
    print()

print("\n" + "="*60 + "\n")

# 5. Adicionando linhas e colunas
print("5. ADICIONANDO LINHAS E COLUNAS:\n")

matriz = [
    [1, 2, 3],
    [4, 5, 6]
]

print("Matriz original:")
for linha in matriz:
    print(linha)

print("\nAdicionando nova linha [7, 8, 9]:")
matriz.append([7, 8, 9])

print("Matriz com nova linha:")
for linha in matriz:
    print(linha)

print("\nAdicionando elemento a uma linha específica:")
matriz[0].append(10)

print("Matriz com elemento adicionado à primeira linha:")
for linha in matriz:
    print(linha)

print("\n" + "="*60 + "\n")

# 6. Removendo elementos de listas aninhadas
print("6. REMOVENDO ELEMENTOS:\n")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matriz original:")
for linha in matriz:
    print(linha)

print("\nRemovendo última linha:")
matriz.pop()

print("Matriz após remover última linha:")
for linha in matriz:
    print(linha)

print("\nRemovendo elemento da primeira linha (índice 1):")
matriz[0].pop(1)

print("Matriz após remover elemento:")
for linha in matriz:
    print(linha)

print("\n" + "="*60 + "\n")

# 7. Tamanho de listas aninhadas
print("7. TAMANHO DE LISTAS ANINHADAS:\n")

matriz = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

print("Matriz:")
for linha in matriz:
    print(linha)

print(f"\nNúmero de linhas: {len(matriz)}")
print(f"Número de colunas (primeira linha): {len(matriz[0])}")
print(f"Total de elementos: {len(matriz) * len(matriz[0])}")

# Contar elementos
total = sum(len(linha) for linha in matriz)
print(f"Total de elementos (usando sum): {total}")

print("\n" + "="*60 + "\n")

# 8. Buscando elementos em listas aninhadas
print("8. BUSCANDO ELEMENTOS:\n")

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

def encontrar_elemento(lista, valor):
    """Encontra um elemento em uma lista aninhada"""
    for i, linha in enumerate(lista):
        if valor in linha:
            j = linha.index(valor)
            return (i, j)
    return None

print("Matriz:")
for linha in matriz:
    print(linha)

print("\nBuscando o número 5:")
resultado = encontrar_elemento(matriz, 5)
print(f"Encontrado em: matriz{resultado}")

print("\nBuscando o número 9:")
resultado = encontrar_elemento(matriz, 9)
print(f"Encontrado em: matriz{resultado}")

print("\nBuscando o número 99:")
resultado = encontrar_elemento(matriz, 99)
if resultado:
    print(f"Encontrado em: matriz{resultado}")
else:
    print("Não encontrado!")

print("\n" + "="*60 + "\n")

# 9. Exemplo prático: Notas de alunos
print("9. EXEMPLO PRÁTICO: NOTAS DE ALUNOS:\n")

# [nome, nota1, nota2, nota3, média]
notas_alunos = [
    ["João", 7.5, 8.0, 7.8],
    ["Maria", 9.0, 9.5, 9.2],
    ["Pedro", 6.5, 7.0, 6.8],
    ["Ana", 8.5, 8.8, 8.6]
]

print("Notas dos alunos:")
print(f"{'Nome':<15} {'Nota1':<8} {'Nota2':<8} {'Nota3':<8} {'Média':<8}")
print("="*50)

for aluno in notas_alunos:
    nome = aluno[0]
    nota1, nota2, nota3 = aluno[1], aluno[2], aluno[3]
    media = (nota1 + nota2 + nota3) / 3
    print(f"{nome:<15} {nota1:<8.1f} {nota2:<8.1f} {nota3:<8.1f} {media:<8.2f}")

print("\n" + "="*60 + "\n")

# 10. Exemplo prático: Tabuleiro de jogo (Jogo da Velha)
print("10. EXEMPLO PRÁTICO: TABULEIRO DE JOGO (JOGO DA VELHA):\n")

tabuleiro = [
    ['X', 'O', 'X'],
    ['O', 'X', 'O'],
    [' ', ' ', ' ']
]

def exibir_tabuleiro(tab):
    """Exibe o tabuleiro de forma legível"""
    print("\n   0   1   2")
    for i, linha in enumerate(tab):
        print(f"{i}  {linha[0]} | {linha[1]} | {linha[2]}")
        if i < len(tab) - 1:
            print("  -----------")
    print()

def fazer_jogada(tab, linha, coluna, jogador):
    """Faz uma jogada no tabuleiro"""
    if tab[linha][coluna] == ' ':
        tab[linha][coluna] = jogador
        print(f"✓ Jogador {jogador} jogou em ({linha}, {coluna})")
        return True
    else:
        print(f"❌ Posição ({linha}, {coluna}) já está ocupada!")
        return False

exibir_tabuleiro(tabuleiro)

fazer_jogada(tabuleiro, 2, 0, 'X')
exibir_tabuleiro(tabuleiro)

fazer_jogada(tabuleiro, 2, 1, 'O')
exibir_tabuleiro(tabuleiro)

fazer_jogada(tabuleiro, 2, 2, 'X')
exibir_tabuleiro(tabuleiro)

print("="*60 + "\n")

# 11. Exemplo prático: Representação de mundo 2D
print("11. EXEMPLO PRÁTICO: MAPA DO JOGO (2D):\n")

mapa = [
    ['🌲', '🌲', '🌊', '🌊', '🌊'],
    ['🌲', '🏠', '🌊', '🌊', '⛰️'],
    ['🌲', '🌲', '🌾', '🏔️', '⛰️'],
    ['🌲', '🌲', '🌾', '🌾', '⛰️'],
    ['🏰', '🌾', '🌾', '🌾', '⛰️']
]

print("Mapa do jogo (5x5):\n")
for i, linha in enumerate(mapa):
    print(f"{i}  ", end="")
    for elemento in linha:
        print(elemento, end="  ")
    print()

print("\nLegenda:")
print("🌲 = Floresta")
print("🌾 = Campo")
print("🌊 = Água")
print("⛰️ = Montanha")
print("🏰 = Castelo")
print("🏠 = Casa")

print("\n" + "="*60 + "\n")

# 12. Copiando listas aninhadas
print("12. COPIANDO LISTAS ANINHADAS:\n")

original = [
    [1, 2, 3],
    [4, 5, 6]
]

# Cópia superficial (shallow copy) - PERIGOSO!
copia_superficial = original.copy()
print("Matriz original:")
for linha in original:
    print(linha)

print("\nMatriz cópia (superficial):")
for linha in copia_superficial:
    print(linha)

print("\nModificando copia_superficial[0][0] = 999:")
copia_superficial[0][0] = 999

print("\nMatriz original (foi modificada!):")
for linha in original:
    print(linha)

print("\n" + "-"*60 + "\n")

# Cópia profunda (deep copy) - SEGURO!
from copy import deepcopy

original2 = [
    [1, 2, 3],
    [4, 5, 6]
]

copia_profunda = deepcopy(original2)
print("Matriz original:")
for linha in original2:
    print(linha)

print("\nMatriz cópia (profunda):")
for linha in copia_profunda:
    print(linha)

print("\nModificando copia_profunda[0][0] = 999:")
copia_profunda[0][0] = 999

print("\nMatriz original (não foi modificada!):")
for linha in original2:
    print(linha)

print("\nMatriz cópia:")
for linha in copia_profunda:
    print(linha)

print("\n" + "="*60 + "\n")

# 13. Operações com listas aninhadas
print("13. OPERAÇÕES COM LISTAS ANINHADAS:\n")

matriz1 = [
    [1, 2],
    [3, 4]
]

matriz2 = [
    [5, 6],
    [7, 8]
]

print("Matriz 1:")
for linha in matriz1:
    print(linha)

print("\nMatriz 2:")
for linha in matriz2:
    print(linha)

# Concatenar
matriz_concatenada = matriz1 + matriz2
print("\nMatriz1 + Matriz2:")
for linha in matriz_concatenada:
    print(linha)

# Repetir
print("\nMatriz1 * 2 (repetir):")
matriz_repetida = matriz1 * 2
for linha in matriz_repetida:
    print(linha)

print("\n" + "="*60 + "\n")

# 14. Dicas e boas práticas
print("14. DICAS E BOAS PRÁTICAS:\n")

print("""
✓ BOAS PRÁTICAS:
  1. Use deepcopy() para copiar listas aninhadas com segurança
  2. Use for aninhados para iterar sobre matrizes
  3. Use enumerate() para obter índices
  4. Seja cuidadoso com índices negativos
  5. Documente o propósito de cada dimensão

✓ CASOS DE USO COMUNS:
  - Matrizes matemáticas
  - Tabuleiros de jogos
  - Mapas 2D/3D
  - Dados tabulares (planilhas)
  - Imagens (pixels em grid)
  - Gráficos (adjacência)

✓ PERFORMANCE:
  - Para listas muito grandes, considere NumPy
  - Evite listas aninhadas irregulares quando possível
  - Use list comprehensions para operações em massa
""")

print("="*60 + "\n")

# 15. Exemplo com list comprehension
print("15. USANDO LIST COMPREHENSION:\n")

print("Criar uma matriz 3x3 com zeros:")
matriz_zeros = [[0 for _ in range(3)] for _ in range(3)]
for linha in matriz_zeros:
    print(linha)

print("\nCriar uma matriz 3x3 com números sequenciais:")
matriz_seq = [[i*3 + j for j in range(3)] for i in range(3)]
for linha in matriz_seq:
    print(linha)

print("\nCriar uma matriz 3x3 com números aleatórios:")
import random
matriz_random = [[random.randint(1, 100) for _ in range(3)] for _ in range(3)]
for linha in matriz_random:
    print(linha)

print("\nTranspor uma matriz (linhas viram colunas):")
original = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposta = [[original[j][i] for j in range(len(original))] for i in range(len(original[0]))]

print("Original:")
for linha in original:
    print(linha)

print("\nTransposta:")
for linha in transposta:
    print(linha)

print("\n" + "="*60)
