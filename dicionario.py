# Dicionários em Python


# Dicionários em Python
# Um dicionário é uma estrutura de dados que armazena pares chave-valor.

print("="*70)
print("DICIONÁRIOS EM PYTHON")
print("="*70 + "\n")

# Explicação
print("O QUE É UM DICIONÁRIO?\n")
print("""
Um dicionário é uma estrutura de dados que armazena pares chave-valor.

Características:
✓ Muta vel (pode ser modificado)
✓ Desordenado (Python 3.7+ mantém ordem de inserção)
✓ Sem índices numéricos (usa chaves para acessar valores)
✓ Chaves devem ser únicas
✓ Valores podem ser qualquer tipo

Sintaxe: dicionario = {chave: valor, chave: valor, ...}
""")

print("="*70 + "\n")

# 1. Criando dicionários
print("1. CRIANDO DICIONÁRIOS:\n")

# Dicionário vazio
dicio_vazio = {}
print(f"Dicionário vazio: {dicio_vazio}\n")

# Dicionário com dados
pessoa = {
    "nome": "Odair Gabriel",
    "idade": 25,
    "email": "joao@email.com",
    "cidade": "São Paulo"
}
print(f"Dicionário pessoa: {pessoa}\n")

# Usando construtor dict()
cores = dict(vermelho="FF0000", verde="00FF00", azul="0000FF")
print(f"Dicionário cores: {cores}\n")

print("="*70 + "\n")

# 2. Acessando valores
print("2. ACESSANDO VALORES:\n")

print(f"Nome: {pessoa['nome']}")
print(f"Idade: {pessoa['idade']}")
print(f"Email: {pessoa['email']}\n")

# Usando get() - mais seguro
print("Usando get():")
print(f"Telefone: {pessoa.get('telefone')}")
print(f"Telefone (com padrão): {pessoa.get('telefone', 'Não informado')}\n")

print("="*70 + "\n")

# 3. Modificando valores
print("3. MODIFICANDO VALORES:\n")

print(f"Pessoa antes: {pessoa}")

pessoa["idade"] = 26
pessoa["email"] = "joao.silva@email.com"

print(f"Pessoa depois: {pessoa}\n")

print("="*70 + "\n")

# 4. Adicionando novos pares
print("4. ADICIONANDO NOVOS PARES:\n")

print(f"Antes: {pessoa}")

pessoa["telefone"] = "(11) 98765-4321"
pessoa["profissao"] = "Desenvolvedor"

print(f"Depois: {pessoa}\n")

print("="*70 + "\n")

# 5. Removendo pares
print("5. REMOVENDO PARES:\n")

dicio = {"a": 1, "b": 2, "c": 3, "d": 4}
print(f"Dicionário original: {dicio}")

# Usar del
del dicio["b"]
print(f"Após del dicio['b']: {dicio}")

# Usar pop()
valor_removido = dicio.pop("d")
print(f"Removido com pop(): {valor_removido}")
print(f"Dicionário após pop: {dicio}\n")

print("="*70 + "\n")

# 6. Iterando sobre dicionários
print("6. ITERANDO SOBRE DICIONÁRIOS:\n")

aluno = {
    "nome": "Maria",
    "nota1": 8.5,
    "nota2": 9.0,
    "nota3": 8.8
}

print("Iterando sobre chaves:")
for chave in aluno:
    print(f"  {chave}: {aluno[chave]}")

print("\nIterando sobre chaves (explícito):")
for chave in aluno.keys():
    print(f"  {chave}")

print("\nIterando sobre valores:")
for valor in aluno.values():
    print(f"  {valor}")

print("\nIterando sobre pares (chave, valor):")
for chave, valor in aluno.items():
    print(f"  {chave}: {valor}")

print()

print("="*70 + "\n")

# 7. Métodos úteis
print("7. MÉTODOS ÚTEIS:\n")

dicio = {"x": 10, "y": 20, "z": 30}

print(f"Dicionário: {dicio}\n")

print(f"Chaves: {list(dicio.keys())}")
print(f"Valores: {list(dicio.values())}")
print(f"Pares: {list(dicio.items())}\n")

print(f"Quantidade de elementos: {len(dicio)}")
print(f"'x' está no dicionário? {'x' in dicio}")
print(f"'w' está no dicionário? {'w' in dicio}\n")

print("="*70 + "\n")

# 8. Exemplo prático: Contato
print("8. EXEMPLO PRÁTICO: AGENDA DE CONTATOS:\n")

contatos = {
    "João": {
        "telefone": "(11) 98765-4321",
        "email": "joao@email.com",
        "cidade": "São Paulo"
    },
    "Maria": {
        "telefone": "(21) 99876-5432",
        "email": "maria@email.com",
        "cidade": "Rio de Janeiro"
    },
    "Pedro": {
        "telefone": "(31) 97654-3210",
        "email": "pedro@email.com",
        "cidade": "Belo Horizonte"
    }
}

print("Agenda de contatos:")
for nome, info in contatos.items():
    print(f"\n{nome}:")
    for chave, valor in info.items():
        print(f"  {chave}: {valor}")

print("\n" + "="*70 + "\n")

# 9. Exemplo prático: Inventário de loja
print("9. EXEMPLO PRÁTICO: INVENTÁRIO DE LOJA:\n")

inventario = {
    "notebook": {"preco": 3500.00, "quantidade": 5},
    "mouse": {"preco": 50.00, "quantidade": 20},
    "teclado": {"preco": 150.00, "quantidade": 15},
    "monitor": {"preco": 800.00, "quantidade": 8}
}

print("Inventário:")
print(f"{'Produto':<15} {'Preço':<12} {'Qtd':<8} {'Total':<12}")
print("-" * 50)

for produto, dados in inventario.items():
    preco = dados["preco"]
    qtd = dados["quantidade"]
    total = preco * qtd
    print(f"{produto:<15} R${preco:<11.2f} {qtd:<8} R${total:<11.2f}")

print()

print("="*70 + "\n")

# 10. Contando frequência com dicionário
print("10. CONTANDO FREQUÊNCIA DE PALAVRAS:\n")

texto = "python python java python javascript python java"
palavras = texto.split()

frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print(f"Texto: {texto}\n")
print("Frequência de palavras:")
for palavra, freq in frequencia.items():
    print(f"  {palavra}: {freq}")

print()

print("="*70 + "\n")

# 11. Merging (unindo dicionários)
print("11. UNINDO DICIONÁRIOS:\n")

dicio1 = {"a": 1, "b": 2}
dicio2 = {"c": 3, "d": 4}

print(f"Dicionário 1: {dicio1}")
print(f"Dicionário 2: {dicio2}\n")

# Método 1: Usando update()
dicio_unido = dicio1.copy()
dicio_unido.update(dicio2)
print(f"Unido com update(): {dicio_unido}\n")

# Método 2: Usando | (Python 3.9+)
dicio_unido2 = dicio1 | dicio2
print(f"Unido com | : {dicio_unido2}\n")

print("="*70 + "\n")

# 12. Valores padrão com setdefault()
print("12. VALORES PADRÃO COM setdefault():\n")

usuario = {"nome": "Ana", "idade": 28}
print(f"Usuário: {usuario}\n")

# Se a chave não existe, cria com valor padrão
telefone = usuario.setdefault("telefone", "Não informado")
print(f"Telefone: {telefone}")
print(f"Usuário após setdefault: {usuario}\n")

print("="*70 + "\n")

# 13. Dicionário com valores padrão (defaultdict)
print("13. USANDO defaultdict:\n")

from collections import defaultdict

# Dicionário normal (erro se chave não existe)
print("Dicionário normal:")
d1 = {"a": 1}
try:
    print(d1["b"])
except KeyError:
    print("  Erro: Chave 'b' não existe!\n")

# defaultdict (valor padrão)
print("Usando defaultdict:")
d2 = defaultdict(int)
d2["a"] = 5
print(f"  d2['a']: {d2['a']}")
print(f"  d2['b'] (não existe): {d2['b']}")
print(f"  Dicionário após acessar 'b': {dict(d2)}\n")

print("="*70 + "\n")

# 14. Compreensão de dicionário
print("14. COMPREENSÃO DE DICIONÁRIO:\n")

numeros = [1, 2, 3, 4, 5]

# Criar dicionário: número -> quadrado
quadrados = {n: n**2 for n in numeros}
print(f"Números: {numeros}")
print(f"Quadrados: {quadrados}\n")

# Dicionário com condição
pares = {n: n**2 for n in numeros if n % 2 == 0}
print(f"Pares e seus quadrados: {pares}\n")

print("="*70 + "\n")

# 15. Resumo e operações comuns
print("15. RESUMO - OPERAÇÕES COMUNS:\n")

dicio = {"nome": "João", "idade": 25}

print(f"""
Criação:
  dicio = {{'nome': 'João', 'idade': 25}}

Acesso:
  dicio['nome']           → {dicio['nome']}
  dicio.get('nome')       → {dicio.get('nome')}
  dicio.get('email', '')  → {dicio.get('email', '')}

Modificação:
  dicio['idade'] = 26

Adição:
  dicio['email'] = 'joao@email.com'

Remoção:
  del dicio['email']
  dicio.pop('email')

Verificação:
  'nome' in dicio         → {'nome' in dicio}
  'email' in dicio        → {'email' in dicio}

Tamanho:
  len(dicio)              → {len(dicio)}

Iteração:
  dicio.keys()            → {list(dicio.keys())}
  dicio.values()          → {list(dicio.values())}
  dicio.items()           → {list(dicio.items())}

Limpeza:
  dicio.clear()           → remove todos os elementos
""")

print("="*70 + "\n")

# 16. Dicionários ordenados
print("16. ORDEM EM DICIONÁRIOS:\n")

print("Python 3.7+: Dicionários mantêm ordem de inserção\n")

d = {}
d["z"] = 1
d["a"] = 2
d["m"] = 3

print(f"Ordem de inserção: z → a → m")
print(f"Dicionário: {d}")
print(f"Chaves na ordem de inserção: {list(d.keys())}\n")

print("="*70 + "\n")

# 17. Casos de uso
print("17. CASOS DE USO COMUNS:\n")

print("""
✓ Dados estruturados:
  - Representar objetos/registros
  - Armazenar propriedades

✓ Mapeamento:
  - Converter um valor em outro
  - Tradução de idiomas

✓ Contagem:
  - Frequência de elementos
  - Estatísticas

✓ Cache:
  - Armazenar resultados
  - Evitar cálculos repetidos

✓ Configurações:
  - Armazenar settings
  - Parâmetros de programa

✓ Dados JSON:
  - Trabalhar com APIs
  - Ler/escrever dados
""")

print("="*70)
