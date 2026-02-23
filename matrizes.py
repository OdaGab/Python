# Soma de Matrizes 3x3

print("="*60)
print("SOMA DE MATRIZES 3x3")
print("="*60 + "\n")

# 1. Exemplo básico: Soma de duas matrizes 3x3
print("1. SOMA BÁSICA DE DUAS MATRIZES 3x3:\n")

matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matriz 1:")
for linha in matriz1:
    print(linha)

print("\nMatriz 2:")
for linha in matriz2:
    print(linha)

# Soma manualmente
resultado = [
    [matriz1[0][0] + matriz2[0][0], matriz1[0][1] + matriz2[0][1], matriz1[0][2] + matriz2[0][2]],
    [matriz1[1][0] + matriz2[1][0], matriz1[1][1] + matriz2[1][1], matriz1[1][2] + matriz2[1][2]],
    [matriz1[2][0] + matriz2[2][0], matriz1[2][1] + matriz2[2][1], matriz1[2][2] + matriz2[2][2]]
]

print("\nMatriz 1 + Matriz 2:")
for linha in resultado:
    print(linha)

print("\n" + "="*60 + "\n")

# 2. Usando função para somar matrizes
print("2. USANDO FUNÇÃO PARA SOMAR MATRIZES:\n")

def somar_matrizes(mat1, mat2):
    """
    Soma duas matrizes de qualquer tamanho.
    
    Args:
        mat1: primeira matriz
        mat2: segunda matriz
    
    Returns:
        Uma nova matriz com o resultado da soma
    """
    # Verifica se as matrizes têm o mesmo tamanho
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        print("❌ Erro: As matrizes devem ter o mesmo tamanho!")
        return None
    
    # Cria a matriz resultado
    linhas = len(mat1)
    colunas = len(mat1[0])
    resultado = [[0 for _ in range(colunas)] for _ in range(linhas)]
    
    # Soma cada elemento
    for i in range(linhas):
        for j in range(colunas):
            resultado[i][j] = mat1[i][j] + mat2[i][j]
    
    return resultado

def exibir_matriz(matriz, nome="Matriz"):
    """Exibe uma matriz de forma formatada"""
    print(f"{nome}:")
    for linha in matriz:
        for elemento in linha:
            print(f"{elemento:6}", end=" ")
        print()
    print()

# Exemplo com números diferentes
mat_a = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat_b = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

exibir_matriz(mat_a, "Matriz A")
exibir_matriz(mat_b, "Matriz B")

resultado = somar_matrizes(mat_a, mat_b)
exibir_matriz(resultado, "A + B")

print("="*60 + "\n")

# 3. Usando list comprehension
print("3. SOMA USANDO LIST COMPREHENSION:\n")

def somar_matrizes_comprehension(mat1, mat2):
    """Soma matrizes usando list comprehension"""
    return [[mat1[i][j] + mat2[i][j] for j in range(len(mat1[0]))] for i in range(len(mat1))]

mat_x = [
    [5, 10, 15],
    [20, 25, 30],
    [35, 40, 45]
]

mat_y = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

exibir_matriz(mat_x, "Matriz X")
exibir_matriz(mat_y, "Matriz Y")

resultado = somar_matrizes_comprehension(mat_x, mat_y)
exibir_matriz(resultado, "X + Y (com comprehension)")

print("="*60 + "\n")

# 4. Exemplo prático: Soma com números negativos
print("4. SOMA COM NÚMEROS NEGATIVOS:\n")

mat_negativa1 = [
    [5, -3, 2],
    [-1, 4, -6],
    [3, -2, 7]
]

mat_negativa2 = [
    [-5, 3, -2],
    [1, -4, 6],
    [-3, 2, -7]
]

exibir_matriz(mat_negativa1, "Matriz com negativos 1")
exibir_matriz(mat_negativa2, "Matriz com negativos 2")

resultado = somar_matrizes(mat_negativa1, mat_negativa2)
exibir_matriz(resultado, "Soma (resultado esperado: matriz de zeros)")

print("="*60 + "\n")

# 5. Soma com números decimais
print("5. SOMA COM NÚMEROS DECIMAIS:\n")

mat_decimal1 = [
    [1.5, 2.3, 3.7],
    [4.2, 5.8, 6.1],
    [7.4, 8.9, 9.6]
]

mat_decimal2 = [
    [0.5, 0.7, 0.3],
    [0.8, 0.2, 0.9],
    [0.6, 0.1, 0.4]
]

exibir_matriz(mat_decimal1, "Matriz com decimais 1")
exibir_matriz(mat_decimal2, "Matriz com decimais 2")

resultado = somar_matrizes(mat_decimal1, mat_decimal2)
exibir_matriz(resultado, "Soma dos decimais")

print("="*60 + "\n")

# 6. Verificando tamanho das matrizes
print("6. VERIFICANDO COMPATIBILIDADE DE MATRIZES:\n")

mat_valida1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat_invalida = [
    [1, 2],
    [3, 4]
]

print("Tentando somar matrizes com tamanhos diferentes:")
resultado = somar_matrizes(mat_valida1, mat_invalida)

print("\nTentando somar matrizes com tamanhos iguais:")
mat_valida2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]
resultado = somar_matrizes(mat_valida1, mat_valida2)
exibir_matriz(resultado, "Soma bem-sucedida")

print("="*60 + "\n")

# 7. Informações sobre as matrizes
print("7. INFORMAÇÕES SOBRE AS MATRIZES:\n")

def info_matriz(matriz, nome="Matriz"):
    """Exibe informações sobre uma matriz"""
    linhas = len(matriz)
    colunas = len(matriz[0])
    total_elementos = linhas * colunas
    
    # Calcula soma de todos os elementos
    soma_total = sum(sum(linha) for linha in matriz)
    
    # Calcula média
    media = soma_total / total_elementos if total_elementos > 0 else 0
    
    # Encontra máximo e mínimo
    flat = [elemento for linha in matriz for elemento in linha]
    maximo = max(flat)
    minimo = min(flat)
    
    print(f"{nome}:")
    print(f"  Dimensões: {linhas}x{colunas}")
    print(f"  Total de elementos: {total_elementos}")
    print(f"  Soma de todos os elementos: {soma_total}")
    print(f"  Média: {media:.2f}")
    print(f"  Valor máximo: {maximo}")
    print(f"  Valor mínimo: {minimo}\n")

mat_info1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

mat_info2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

info_matriz(mat_info1, "Matriz 1")
info_matriz(mat_info2, "Matriz 2")

resultado_info = somar_matrizes(mat_info1, mat_info2)
info_matriz(resultado_info, "Soma das Matrizes")

print("="*60 + "\n")

# 8. Soma iterativa de múltiplas matrizes
print("8. SOMANDO MÚLTIPLAS MATRIZES:\n")

def somar_multiplas_matrizes(matrizes):
    """Soma uma lista de matrizes"""
    if len(matrizes) == 0:
        return None
    
    # Começa com a primeira matriz
    resultado = [linha[:] for linha in matrizes[0]]  # Cópia
    
    # Soma as demais
    for i in range(1, len(matrizes)):
        resultado = somar_matrizes(resultado, matrizes[i])
    
    return resultado

mat1 = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]

mat2 = [
    [2, 2, 2],
    [2, 2, 2],
    [2, 2, 2]
]

mat3 = [
    [3, 3, 3],
    [3, 3, 3],
    [3, 3, 3]
]

matrizes = [mat1, mat2, mat3]

exibir_matriz(mat1, "Matriz 1")
exibir_matriz(mat2, "Matriz 2")
exibir_matriz(mat3, "Matriz 3")

resultado = somar_multiplas_matrizes(matrizes)
exibir_matriz(resultado, "Soma de todas as matrizes")

print("="*60 + "\n")

# 9. Exemplo prático: Soma de vendas por trimestre
print("9. EXEMPLO PRÁTICO: SOMA DE VENDAS POR TRIMESTRE:\n")

print("Uma loja tem 3 departamentos e 3 trimestres")
print("Cada matriz representa vendas (em milhares)\n")

# Vendas do trimestre 1
vendas_trim1 = [
    [10, 15, 20],  # Eletrônicos, Roupas, Alimentos
    [25, 30, 35],  # Loja 1, 2, 3
    [40, 45, 50]
]

# Vendas do trimestre 2
vendas_trim2 = [
    [12, 18, 22],
    [28, 33, 38],
    [43, 48, 53]
]

exibir_matriz(vendas_trim1, "Vendas Trimestre 1")
exibir_matriz(vendas_trim2, "Vendas Trimestre 2")

vendas_total = somar_matrizes(vendas_trim1, vendas_trim2)
exibir_matriz(vendas_total, "Vendas Totais (Trim1 + Trim2)")

print("="*60 + "\n")

# 10. Função interativa
print("10. PROGRAMA INTERATIVO:\n")

def programa_soma_matrizes():
    """Programa interativo para somar matrizes"""
    print("\n🔢 SOMA DE MATRIZES 3x3 INTERATIVA\n")
    
    # Criar primeira matriz
    print("Digite os 9 elementos da primeira matriz (3x3):")
    print("Separados por espaço, linha por linha\n")
    
    matriz1 = []
    for i in range(3):
        while True:
            try:
                linha = list(map(float, input(f"Linha {i+1}: ").split()))
                if len(linha) == 3:
                    matriz1.append(linha)
                    break
                else:
                    print("❌ Digite exatamente 3 números!\n")
            except ValueError:
                print("❌ Digite números válidos!\n")
    
    # Criar segunda matriz
    print("\nDigite os 9 elementos da segunda matriz (3x3):")
    matriz2 = []
    for i in range(3):
        while True:
            try:
                linha = list(map(float, input(f"Linha {i+1}: ").split()))
                if len(linha) == 3:
                    matriz2.append(linha)
                    break
                else:
                    print("❌ Digite exatamente 3 números!\n")
            except ValueError:
                print("❌ Digite números válidos!\n")
    
    # Somar
    resultado = somar_matrizes(matriz1, matriz2)
    
    print("\n" + "="*60)
    exibir_matriz(matriz1, "Matriz 1")
    exibir_matriz(matriz2, "Matriz 2")
    exibir_matriz(resultado, "Resultado (Matriz 1 + Matriz 2)")
    print("="*60)

# Menu
print("Para usar o programa interativo, descomente a linha abaixo:")
print("# programa_soma_matrizes()\n")

print("="*60)
