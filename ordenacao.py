# Ordenação de Lista - Método Bolha (Bubble Sort)

print("="*70)
print("ORDENAÇÃO DE LISTAS - MÉTODO BOLHA (BUBBLE SORT)")
print("="*70 + "\n")

# 1. Explicação do Método Bolha
print("1. O QUE É O MÉTODO BOLHA?\n")

print("""
O Método Bolha (Bubble Sort) é um algoritmo de ordenação simples que:

1. Compara elementos adjacentes
2. Se estão fora de ordem, troca suas posições
3. Repete o processo até que a lista esteja ordenada

Por que "bolha"? Porque os maiores elementos "fluem" para o final,
como bolhas subindo em um líquido.

Exemplo visual:
[5, 2, 8, 1, 9]
Primeira passada: 2, 5, 1, 8, 9
Segunda passada: 2, 1, 5, 8, 9
Terceira passada: 1, 2, 5, 8, 9 ✓
""")

print("="*70 + "\n")

# 2. Implementação básica do Bubble Sort
print("2. IMPLEMENTAÇÃO BÁSICA:\n")

def bubble_sort_basico(lista):
    """
    Ordenação com método bolha - versão básica
    
    Args:
        lista: lista a ser ordenada
    
    Returns:
        lista ordenada
    """
    # Cria uma cópia para não modificar a original
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    # Percorre toda a lista
    for i in range(n):
        # Compara pares adjacentes
        for j in range(0, n - i - 1):
            # Se o elemento atual é maior que o próximo, troca
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia

# Exemplo
numeros = [5, 2, 8, 1, 9, 3]
print(f"Lista original: {numeros}")
ordenada = bubble_sort_basico(numeros)
print(f"Lista ordenada: {ordenada}")
print(f"Lista original (não modificada): {numeros}\n")

print("="*70 + "\n")

# 3. Visualizando passo a passo
print("3. VISUALIZANDO PASSO A PASSO:\n")

def bubble_sort_visualizado(lista):
    """
    Bubble sort com visualização de cada passo
    """
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    print(f"Lista inicial: {lista_copia}\n")
    
    total_trocas = 0
    
    for i in range(n):
        print(f"Passada {i + 1}:")
        trocas_nesta_passada = 0
        
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                # Exibe a troca
                print(f"  Comparando {lista_copia[j]} e {lista_copia[j + 1]} → Trocando", end="")
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
                trocas_nesta_passada += 1
                total_trocas += 1
                print(f" → {lista_copia}")
            else:
                print(f"  Comparando {lista_copia[j]} e {lista_copia[j + 1]} → Sem troca")
        
        print(f"  Resultado da passada: {lista_copia}")
        print(f"  Trocas nesta passada: {trocas_nesta_passada}\n")
    
    print(f"Total de trocas: {total_trocas}")
    return lista_copia

print("Exemplo com visualização:")
numeros_vis = [5, 2, 8, 1]
resultado = bubble_sort_visualizado(numeros_vis)

print("="*70 + "\n")

# 4. Otimização: Parando quando não há mais trocas
print("4. VERSÃO OTIMIZADA (com parada antecipada):\n")

def bubble_sort_otimizado(lista):
    """
    Bubble sort otimizado - para quando não há trocas
    """
    lista_copia = lista.copy()
    n = len(lista_copia)
    passadas = 0
    trocas_total = 0
    
    for i in range(n):
        passadas += 1
        houve_troca = False
        
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
                houve_troca = True
                trocas_total += 1
        
        # Se não houve troca, lista já está ordenada
        if not houve_troca:
            print(f"Lista já estava ordenada após {passadas} passada(s)")
            break
    
    return lista_copia, passadas, trocas_total

# Teste com lista já parcialmente ordenada
numeros_otim = [1, 2, 3, 5, 4]
resultado, passadas, trocas = bubble_sort_otimizado(numeros_otim)
print(f"Lista original: {numeros_otim}")
print(f"Lista ordenada: {resultado}")
print(f"Passadas realizadas: {passadas}")
print(f"Total de trocas: {trocas}\n")

print("="*70 + "\n")

# 5. Ordenação crescente e decrescente
print("5. ORDENAÇÃO CRESCENTE E DECRESCENTE:\n")

def bubble_sort_crescente(lista):
    """Ordena em ordem crescente"""
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia

def bubble_sort_decrescente(lista):
    """Ordena em ordem decrescente"""
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] < lista_copia[j + 1]:  # Inverte a comparação
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia

numeros = [5, 2, 8, 1, 9, 3]

print(f"Lista original: {numeros}")
print(f"Crescente: {bubble_sort_crescente(numeros)}")
print(f"Decrescente: {bubble_sort_decrescente(numeros)}\n")

print("="*70 + "\n")

# 6. Ordenando strings
print("6. ORDENANDO STRINGS:\n")

def bubble_sort_strings(lista):
    """Ordena lista de strings alfabeticamente"""
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia

palavras = ["zebra", "apple", "mango", "banana", "cherry"]
print(f"Lista original: {palavras}")
print(f"Lista ordenada: {bubble_sort_strings(palavras)}\n")

print("="*70 + "\n")

# 7. Análise de performance
print("7. ANÁLISE DE PERFORMANCE:\n")

import time

def medir_tempo_bubble_sort(tamanho):
    """Mede o tempo de execução do bubble sort"""
    lista = list(range(tamanho, 0, -1))  # Lista em ordem inversa
    
    inicio = time.time()
    bubble_sort_basico(lista)
    fim = time.time()
    
    return fim - inicio

print("Tempo de execução do bubble sort (em segundos):")
print(f"{'Tamanho':<15} {'Tempo':<15}")
print("-" * 30)

tamanhos = [100, 500, 1000]
for tamanho in tamanhos:
    tempo = medir_tempo_bubble_sort(tamanho)
    print(f"{tamanho:<15} {tempo:.6f}s")

print("\nNota: Bubble sort é lento para listas grandes!")
print("Complexidade: O(n²)\n")

print("="*70 + "\n")

# 8. Comparação com sorted() nativo
print("8. COMPARAÇÃO COM MÉTODO NATIVO sorted():\n")

numeros = [5, 2, 8, 1, 9, 3]

# Bubble sort
inicio_bubble = time.time()
resultado_bubble = bubble_sort_basico(numeros)
tempo_bubble = time.time() - inicio_bubble

# sorted() nativo
inicio_sorted = time.time()
resultado_sorted = sorted(numeros)
tempo_sorted = time.time() - inicio_sorted

print(f"Bubble sort: {resultado_bubble} - Tempo: {tempo_bubble:.8f}s")
print(f"sorted():    {resultado_sorted} - Tempo: {tempo_sorted:.8f}s")
print(f"\nsorted() é aproximadamente {tempo_bubble/tempo_sorted:.0f}x mais rápido\n")

print("="*70 + "\n")

# 9. Exemplo prático: Ordenar notas de alunos
print("9. EXEMPLO PRÁTICO: ORDENAR NOTAS DE ALUNOS:\n")

class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __repr__(self):
        return f"{self.nome}: {self.nota}"

alunos = [
    Aluno("João", 7.5),
    Aluno("Maria", 9.0),
    Aluno("Pedro", 6.8),
    Aluno("Ana", 8.5)
]

def bubble_sort_alunos(lista):
    """Ordena alunos por nota"""
    lista_copia = lista.copy()
    n = len(lista_copia)
    
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista_copia[j].nota > lista_copia[j + 1].nota:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
    
    return lista_copia

print("Alunos originais:")
for aluno in alunos:
    print(f"  {aluno}")

alunos_ordenados = bubble_sort_alunos(alunos)

print("\nAlunos ordenados por nota (crescente):")
for aluno in alunos_ordenados:
    print(f"  {aluno}")

print("\n" + "="*70 + "\n")

# 10. Contando trocas e comparações
print("10. CONTANDO OPERAÇÕES:\n")

def bubble_sort_com_estatisticas(lista):
    """Bubble sort que conta comparações e trocas"""
    lista_copia = lista.copy()
    n = len(lista_copia)
    comparacoes = 0
    trocas = 0
    
    for i in range(n):
        for j in range(0, n - i - 1):
            comparacoes += 1
            if lista_copia[j] > lista_copia[j + 1]:
                lista_copia[j], lista_copia[j + 1] = lista_copia[j + 1], lista_copia[j]
                trocas += 1
    
    return lista_copia, comparacoes, trocas

numeros = [5, 2, 8, 1, 9]
resultado, comp, troc = bubble_sort_com_estatisticas(numeros)

print(f"Lista original: {numeros}")
print(f"Lista ordenada: {resultado}")
print(f"Total de comparações: {comp}")
print(f"Total de trocas: {troc}")
print(f"Taxa de trocas: {(troc/comp)*100:.1f}%\n")

print("="*70 + "\n")

# 11. Casos especiais
print("11. CASOS ESPECIAIS:\n")

print("Lista vazia:")
print(f"  Resultado: {bubble_sort_basico([])}\n")

print("Um elemento:")
print(f"  Resultado: {bubble_sort_basico([42])}\n")

print("Dois elementos:")
print(f"  Resultado: {bubble_sort_basico([2, 1])}\n")

print("Elementos duplicados:")
print(f"  Resultado: {bubble_sort_basico([3, 1, 3, 1, 3])}\n")

print("Lista já ordenada:")
print(f"  Resultado: {bubble_sort_basico([1, 2, 3, 4, 5])}\n")

print("="*70 + "\n")

# 12. Resumo
print("12. RESUMO DO MÉTODO BOLHA:\n")

print("""
✓ VANTAGENS:
  - Fácil de entender
  - Fácil de implementar
  - Não requer espaço extra (in-place)
  - Estável (mantém ordem de elementos iguais)

✗ DESVANTAGENS:
  - Muito lento para listas grandes O(n²)
  - Não é eficiente na prática
  - Existem algoritmos muito melhores

📊 COMPLEXIDADE:
  - Pior caso: O(n²) - lista em ordem inversa
  - Melhor caso: O(n) - lista já ordenada (versão otimizada)
  - Caso médio: O(n²)
  - Espaço: O(1) - ordenação in-place

💡 QUANDO USAR:
  - Fins educacionais
  - Listas muito pequenas
  - Dados quase ordenados
  
❌ QUANDO NÃO USAR:
  - Dados em produção
  - Listas grandes
  - Performance é crítica

🏆 ALTERNATIVAS MELHORES:
  - sorted() - O(n log n)
  - Quick Sort - O(n log n) médio
  - Merge Sort - O(n log n)
  - Heap Sort - O(n log n)
""")

print("="*70)
