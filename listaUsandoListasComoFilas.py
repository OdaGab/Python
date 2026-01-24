# Usando Listas como Filas (FIFO - First In, First Out)

# Uma fila é uma estrutura de dados onde o primeiro elemento a entrar
# é o primeiro a sair (FIFO - First In, First Out)
# Em Python, podemos usar listas para implementar filas com append() e pop(0)

print("="*50)
print("FILAS COM LISTAS - FIFO (First In, First Out)")
print("="*50 + "\n")

# 1. Exemplo básico de fila
print("1. EXEMPLO BÁSICO DE FILA:\n")

fila = []
print("Fila vazia:", fila)

# Adicionando elementos (enfileirando)
fila.append("Pessoa 1")
fila.append("Pessoa 2")
fila.append("Pessoa 3")
fila.append("Pessoa 4")
print("Após adicionar 4 pessoas:", fila)

# Removendo elementos (desfileirando)
primeira = fila.pop(0)
print(f"Primeira pessoa a sair: {primeira}")
print("Fila após remover primeira pessoa:", fila)

segunda = fila.pop(0)
print(f"Segunda pessoa a sair: {segunda}")
print("Fila após remover segunda pessoa:", fila)

print("\n" + "="*50 + "\n")

# 2. Simulação de fila de supermercado
print("2. SIMULAÇÃO DE FILA DE SUPERMERCADO:\n")

fila_caixa = []

def adicionar_cliente(fila, nome):
    fila.append(nome)
    print(f"✓ {nome} entrou na fila")

def atender_cliente(fila):
    if len(fila) > 0:
        cliente = fila.pop(0)
        print(f"✗ {cliente} foi atendido e saiu da fila")
        return cliente
    else:
        print("✗ Nenhum cliente na fila para atender")
        return None

# Clientes chegando
adicionar_cliente(fila_caixa, "Ana")
adicionar_cliente(fila_caixa, "Bruno")
adicionar_cliente(fila_caixa, "Carlos")
adicionar_cliente(fila_caixa, "Diana")

print(f"\nFila atual: {fila_caixa}")
print(f"Quantidade de clientes: {len(fila_caixa)}\n")

# Atendendo clientes
atender_cliente(fila_caixa)
print(f"Fila: {fila_caixa}\n")

atender_cliente(fila_caixa)
print(f"Fila: {fila_caixa}\n")

# Novo cliente chega
adicionar_cliente(fila_caixa, "Elisa")
print(f"Fila: {fila_caixa}\n")

# Atendendo mais clientes
atender_cliente(fila_caixa)
atender_cliente(fila_caixa)
print(f"Fila: {fila_caixa}\n")

print("="*50 + "\n")

# 3. Verificando se a fila está vazia ou cheia
print("3. VERIFICANDO O ESTADO DA FILA:\n")

tarefas = []

def adicionar_tarefa(fila, tarefa):
    fila.append(tarefa)
    print(f"✓ Tarefa adicionada: '{tarefa}'")
    print(f"  Total de tarefas: {len(fila)}")

def proxima_tarefa(fila):
    if len(fila) > 0:
        tarefa = fila.pop(0)
        print(f"✓ Executando: '{tarefa}'")
        print(f"  Tarefas restantes: {len(fila)}")
        return tarefa
    else:
        print("✗ Nenhuma tarefa na fila!")
        return None

adicionar_tarefa(tarefas, "Estudar Python")
adicionar_tarefa(tarefas, "Fazer exercícios")
adicionar_tarefa(tarefas, "Revisar conceitos")

print(f"\nFila de tarefas: {tarefas}\n")

proxima_tarefa(tarefas)
print()
proxima_tarefa(tarefas)
print()
proxima_tarefa(tarefas)
print()
proxima_tarefa(tarefas)  # Tentando executar quando não há tarefas

print("\n" + "="*50 + "\n")

# 4. Usando collections.deque para filas mais eficientes
print("4. USANDO DEQUE PARA FILAS (MAIS EFICIENTE):\n")

from collections import deque

fila_deque = deque()

print("Deque vazio:", fila_deque)

# Adicionar elementos
fila_deque.append(10)
fila_deque.append(20)
fila_deque.append(30)
fila_deque.append(40)
print("Após adicionar elementos:", fila_deque)

# Remover do início (popleft é mais eficiente que pop(0) com listas)
primeiro = fila_deque.popleft()
print(f"Removido do início: {primeiro}")
print("Deque após remover:", fila_deque)

segundo = fila_deque.popleft()
print(f"Removido do início: {segundo}")
print("Deque após remover:", fila_deque)

print("\n" + "="*50 + "\n")

# 5. Comparação: Lista vs Deque
print("5. COMPARAÇÃO: LISTA vs DEQUE:\n")

print("Lista:")
print("  - pop(0) é O(n) - lento para muitas operações")
print("  - Boa para pequenas filas\n")

print("Deque (double-ended queue):")
print("  - popleft() é O(1) - muito mais rápido")
print("  - Ideal para filas que recebem muitas operações\n")

print("Quando usar cada uma:")
print("  - Lista: Filas pequenas e simples")
print("  - Deque: Filas com muitas operações")

print("\n" + "="*50 + "\n")

# 6. Exemplo prático: Sistema de processamento de pedidos
print("6. SISTEMA DE PROCESSAMENTO DE PEDIDOS:\n")

class Pedido:
    def __init__(self, numero, cliente):
        self.numero = numero
        self.cliente = cliente
    
    def __str__(self):
        return f"Pedido #{self.numero} - Cliente: {self.cliente}"

fila_pedidos = deque()

# Novos pedidos chegando
pedidos = [
    Pedido(1, "João Silva"),
    Pedido(2, "Maria Santos"),
    Pedido(3, "Pedro Costa"),
    Pedido(4, "Ana Oliveira")
]

for pedido in pedidos:
    fila_pedidos.append(pedido)
    print(f"✓ {pedido} entrou na fila")

print(f"\nTotal de pedidos: {len(fila_pedidos)}\n")

# Processando pedidos
while len(fila_pedidos) > 0:
    pedido = fila_pedidos.popleft()
    print(f"✗ Processando: {pedido}")

print("\nTodos os pedidos foram processados!")
