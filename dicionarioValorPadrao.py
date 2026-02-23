# Dicionário com Valor Padrão

print("="*60)
print("DICIONÁRIO COM VALOR PADRÃO")
print("="*60 + "\n")

# 1. Usando get() com valor padrão
print("1. USANDO get() COM VALOR PADRÃO:\n")

pessoa = {"nome": "João", "idade": 25}

print(f"Dicionário: {pessoa}\n")

# get() retorna o valor se existe, senão retorna None
print(f"Nome: {pessoa.get('nome')}")
print(f"Email (não existe): {pessoa.get('email')}")

# get() com valor padrão
print(f"Email (com padrão): {pessoa.get('email', 'não informado')}")
print(f"Telefone (com padrão): {pessoa.get('telefone', 'sem dados')}\n")

print("="*60 + "\n")

# 2. Diferença entre [] e get()
print("2. DIFERENÇA ENTRE [] E get():\n")

usuario = {"nome": "Maria", "país": "Brasil"}

print("Usando []:")
print(f"Nome: {usuario['nome']}")
try:
    print(usuario['cidade'])
except KeyError:
    print("❌ Erro! Chave 'cidade' não existe\n")

print("Usando get():")
print(f"Nome: {usuario.get('nome')}")
print(f"Cidade: {usuario.get('cidade')}")
print(f"Cidade (com padrão): {usuario.get('cidade', 'não informado')}\n")

print("="*60 + "\n")

# 3. Usando setdefault()
print("3. USANDO setdefault():\n")

aluno = {"nome": "Pedro", "nota": 8.5}

print(f"Aluno: {aluno}")

# setdefault retorna o valor se existe
resultado = aluno.setdefault("nome", "Padrão")
print(f"setdefault('nome', 'Padrão'): {resultado}")
print(f"Aluno: {aluno}\n")

# setdefault cria a chave se não existe
resultado = aluno.setdefault("turma", "7A")
print(f"setdefault('turma', '7A'): {resultado}")
print(f"Aluno: {aluno}\n")

print("="*60 + "\n")

# 4. Usando defaultdict
print("4. USANDO defaultdict:\n")

from collections import defaultdict

# defaultdict com int (padrão 0)
contador = defaultdict(int)

print("contador sem chaves: {}")
print(f"contador['a']: {contador['a']}")
print(f"Dicionário agora: {dict(contador)}\n")

# Somando valores
contador['python'] += 1
contador['python'] += 1
contador['java'] += 1
contador['python'] += 1

print(f"Contagem de linguagens: {dict(contador)}\n")

print("="*60 + "\n")

# 5. defaultdict com list
print("5. defaultdict COM list:\n")

grupos = defaultdict(list)

grupos['frutas'].append('maçã')
grupos['frutas'].append('banana')
grupos['legumes'].append('cenoura')
grupos['legumes'].append('brócolis')

print("Grupos:")
for categoria, itens in grupos.items():
    print(f"  {categoria}: {itens}\n")

print("="*60 + "\n")

# 6. Exemplo prático: Contagem de palavras
print("6. EXEMPLO: CONTAGEM DE PALAVRAS:\n")

texto = "python python java python javascript java ruby"
palavras = texto.split()

# Opção 1: Usando defaultdict
contagem = defaultdict(int)
for palavra in palavras:
    contagem[palavra] += 1

print(f"Texto: {texto}\n")
print("Frequência com defaultdict:")
for palavra, freq in contagem.items():
    print(f"  {palavra}: {freq}\n")

print("="*60 + "\n")

# 7. Exemplo prático: Grupos de alunos
print("7. EXEMPLO: GRUPOS DE ALUNOS:\n")

grupos_alunos = defaultdict(list)

grupos_alunos['7A'].append('Ana')
grupos_alunos['7A'].append('Bruno')
grupos_alunos['7B'].append('Carlos')
grupos_alunos['7B'].append('Diana')
grupos_alunos['7A'].append('Eduarda')

print("Alunos por turma:\n")
for turma, alunos in sorted(grupos_alunos.items()):
    print(f"{turma}: {alunos}")

print()

print("="*60 + "\n")

# 8. Comparação: dict normal vs defaultdict vs get()
print("8. COMPARAÇÃO DE MÉTODOS:\n")

print("""
┌─────────────────────────────────────────────────────────────┐
│ MÉTODO 1: Usando [] (sem segurança)                         │
└─────────────────────────────────────────────────────────────┘

  dicio = {'a': 1}
  print(dicio['b'])  ❌ Erro: KeyError

┌─────────────────────────────────────────────────────────────┐
│ MÉTODO 2: Usando get() (seguro)                             │
└─────────────────────────────────────────────────────────────┘

  dicio = {'a': 1}
  print(dicio.get('b'))           → None
  print(dicio.get('b', 0))        → 0 (padrão)

┌─────────────────────────────────────────────────────────────┐
│ MÉTODO 3: Usando setdefault() (modifica)                    │
└─────────────────────────────────────────────────────────────┘

  dicio = {'a': 1}
  dicio.setdefault('b', 0)        → 0
  print(dicio)                    → {'a': 1, 'b': 0}

┌─────────────────────────────────────────────────────────────┐
│ MÉTODO 4: Usando defaultdict (automático)                   │
└─────────────────────────────────────────────────────────────┘

  from collections import defaultdict
  dicio = defaultdict(int)
  print(dicio['b'])               → 0 (cria automaticamente)
""")

print("="*60 + "\n")

# 9. defaultdict com diferentes tipos
print("9. defaultdict COM DIFERENTES TIPOS:\n")

# Com int (padrão 0)
d_int = defaultdict(int)
print(f"defaultdict(int): {d_int['qualquer_chave']}")

# Com list (padrão [])
d_list = defaultdict(list)
print(f"defaultdict(list): {d_list['qualquer_chave']}")

# Com str (padrão '')
d_str = defaultdict(str)
print(f"defaultdict(str): '{d_str['qualquer_chave']}'")

# Com dict (padrão {})
d_dict = defaultdict(dict)
print(f"defaultdict(dict): {d_dict['qualquer_chave']}\n")

print("="*60 + "\n")

# 10. Exemplo prático: Pontuação de jogadores
print("10. EXEMPLO: PONTUAÇÃO DE JOGADORES:\n")

from collections import defaultdict

pontuacao = defaultdict(int)

# Simulando partidas
jogadores = [
    ("Alice", 10),
    ("Bob", 8),
    ("Alice", 12),
    ("Carlos", 15),
    ("Bob", 5),
    ("Alice", 7)
]

for jogador, pontos in jogadores:
    pontuacao[jogador] += pontos

print("Pontuação total por jogador:\n")
for jogador in sorted(pontuacao.keys()):
    print(f"{jogador}: {pontuacao[jogador]} pontos")

print()

print("="*60 + "\n")

# 11. Exemplo prático: Inventário de loja
print("11. EXEMPLO: INVENTÁRIO COM PADRÃO:\n")

inventario = {}

# Função para obter quantidade (com padrão 0)
def obter_quantidade(item):
    return inventario.get(item, 0)

print("Inventário vazio:\n")
print(f"Notebooks em estoque: {obter_quantidade('notebook')}")
print(f"Mouses em estoque: {obter_quantidade('mouse')}")

# Adicionando itens
inventario['notebook'] = 5
inventario['mouse'] = 20
inventario['teclado'] = 15

print("\nInventário com itens:\n")
print(f"Notebooks em estoque: {obter_quantidade('notebook')}")
print(f"Mouses em estoque: {obter_quantidade('mouse')}")
print(f"Monitores em estoque: {obter_quantidade('monitor')}\n")

print("="*60 + "\n")

# 12. Resumo
print("12. RESUMO:\n")

print("""
MÉTODO 1: get(chave, padrão)
  - Não modifica o dicionário
  - Retorna padrão se chave não existe
  - Uso: leitura segura

MÉTODO 2: setdefault(chave, padrão)
  - Modifica o dicionário
  - Cria chave com padrão se não existe
  - Uso: criar com padrão

MÉTODO 3: defaultdict(tipo)
  - Sempre usa padrão do tipo
  - Cria automaticamente ao acessar
  - Uso: contar, agrupar dados

QUANDO USAR:
  ✓ get():         leitura simples
  ✓ setdefault():  inicializar com padrão
  ✓ defaultdict(): processar muitos dados
""")

print("="*60)
