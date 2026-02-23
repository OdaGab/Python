# Dicionário com Listas

print("="*60)
print("DICIONÁRIO COM LISTAS")
print("="*60 + "\n")

# 1. Dicionário com lista como valor
print("1. EXEMPLO BÁSICO:\n")

aluno = {
    "nome": "João",
    "notas": [7.5, 8.0, 8.5, 9.0],
    "matérias": ["Português", "Matemática", "História", "Inglês"]
}

print(f"Aluno: {aluno}\n")
print(f"Nome: {aluno['nome']}")
print(f"Notas: {aluno['notas']}")
print(f"Matérias: {aluno['matérias']}\n")

print("="*60 + "\n")

# 2. Acessando elementos da lista dentro do dicionário
print("2. ACESSANDO ELEMENTOS DA LISTA:\n")

print(f"Primeira nota: {aluno['notas'][0]}")
print(f"Última nota: {aluno['notas'][-1]}")
print(f"Segunda matéria: {aluno['matérias'][1]}\n")

print("="*60 + "\n")

# 3. Modificando a lista dentro do dicionário
print("3. MODIFICANDO A LISTA:\n")

print(f"Notas antes: {aluno['notas']}")
aluno['notas'][0] = 8.5
print(f"Notas depois: {aluno['notas']}\n")

# Adicionando elemento à lista
aluno['notas'].append(9.5)
print(f"Notas após adicionar 9.5: {aluno['notas']}\n")

print("="*60 + "\n")

# 4. Iterando sobre a lista no dicionário
print("4. ITERANDO SOBRE A LISTA:\n")

print("Matérias:")
for materia in aluno['matérias']:
    print(f"  - {materia}")

print("\nNotas:")
for i, nota in enumerate(aluno['notas']):
    print(f"  Nota {i+1}: {nota}")

print()

print("="*60 + "\n")

# 5. Exemplo: Biblioteca com livros
print("5. EXEMPLO PRÁTICO: BIBLIOTECA:\n")

biblioteca = {
    "ficção científica": ["Duna", "1984", "Fundação"],
    "mistério": ["Assassinato no Expresso do Oriente", "A Menina que Roubava Livros"],
    "fantasia": ["Harry Potter", "O Senhor dos Anéis", "Crônicas de Nárnia"],
    "romance": ["O Cortiço", "Dom Casmurro"]
}

print("Biblioteca:")
for genero, livros in biblioteca.items():
    print(f"\n{genero.upper()}:")
    for livro in livros:
        print(f"  • {livro}")

print()

print("="*60 + "\n")

# 6. Exemplo: Horário de aulas
print("6. EXEMPLO: HORÁRIO DE AULAS:\n")

horario = {
    "segunda": ["Português", "Matemática", "História"],
    "terça": ["Inglês", "Educação Física", "Arte"],
    "quarta": ["Ciências", "Português", "Matemática"],
    "quinta": ["História", "Inglês", "Português"],
    "sexta": ["Matemática", "Educação Física", "Ciências"]
}

print("Horário semanal:\n")
for dia, aulas in horario.items():
    print(f"{dia.capitalize()}:")
    for i, aula in enumerate(aulas, 1):
        print(f"  {i}. {aula}")
    print()

print("="*60 + "\n")

# 7. Exemplo: Carrinho de compras
print("7. EXEMPLO: CARRINHO DE COMPRAS:\n")

carrinho = {
    "notebook": {"quantidade": 1, "preco": 3500},
    "mouse": {"quantidade": 2, "preco": 50},
    "teclado": {"quantidade": 1, "preco": 150}
}

print("Carrinho de compras:\n")
total = 0
for produto, dados in carrinho.items():
    qtd = dados["quantidade"]
    preco = dados["preco"]
    subtotal = qtd * preco
    total += subtotal
    print(f"{produto.capitalize()}: {qtd}x R${preco} = R${subtotal}")

print(f"\nTotal: R${total}\n")

print("="*60 + "\n")

# 8. Adicionando e removendo de listas no dicionário
print("8. ADICIONANDO E REMOVENDO ELEMENTOS:\n")

tarefas = {
    "hoje": ["Estudar Python", "Fazer exercícios", "Ler livro"],
    "amanhã": ["Projeto final", "Review de código"]
}

print(f"Tarefas hoje: {tarefas['hoje']}")
tarefas['hoje'].append("Assistir aula")
print(f"Após adicionar: {tarefas['hoje']}")

tarefas['hoje'].remove("Ler livro")
print(f"Após remover 'Ler livro': {tarefas['hoje']}\n")

print("="*60 + "\n")

# 9. Verificando se um elemento está na lista
print("9. VERIFICANDO SE ELEMENTO EXISTE:\n")

filme = {
    "titulo": "Matrix",
    "atores": ["Keanu Reeves", "Laurence Fishburne", "Carrie-Anne Moss"],
    "genero": ["ficção científica", "ação"]
}

print(f"Filme: {filme['titulo']}")
print(f"Atores: {filme['atores']}")

if "Keanu Reeves" in filme['atores']:
    print("✓ Keanu Reeves está no elenco")

if "Tom Hanks" in filme['atores']:
    print("✓ Tom Hanks está no elenco")
else:
    print("✗ Tom Hanks não está no elenco\n")

print("="*60 + "\n")

# 10. Tamanho das listas
print("10. TAMANHO DAS LISTAS:\n")

escola = {
    "7A": ["Ana", "Bruno", "Carlos", "Diana", "Eduarda"],
    "7B": ["Felipe", "Gabriela", "Henrique"],
    "7C": ["Iris", "João", "Karla", "Lúcio", "Marina", "Nina"]
}

print("Quantidade de alunos por turma:\n")
for turma, alunos in escola.items():
    print(f"{turma}: {len(alunos)} alunos")
    print(f"  {alunos}\n")

total_alunos = sum(len(alunos) for alunos in escola.values())
print(f"Total de alunos: {total_alunos}")

print()

print("="*60 + "\n")

# 11. Operações com listas em dicionários
print("11. OPERAÇÕES COM LISTAS:\n")

numeros = {
    "pares": [2, 4, 6, 8],
    "impares": [1, 3, 5, 7]
}

print(f"Pares: {numeros['pares']}")
print(f"Soma dos pares: {sum(numeros['pares'])}")
print(f"Máximo: {max(numeros['pares'])}")
print(f"Mínimo: {min(numeros['pares'])}\n")

print(f"Impares: {numeros['impares']}")
print(f"Soma dos impares: {sum(numeros['impares'])}\n")

print("="*60 + "\n")

# 12. Ordenando listas no dicionário
print("12. ORDENANDO LISTAS:\n")

resultado = {
    "pontuações": [95, 87, 92, 78, 88, 91],
    "nomes": ["Pedro", "Ana", "Carlos", "Maria", "João", "Laura"]
}

print(f"Pontuações: {resultado['pontuações']}")
resultado['pontuações'].sort()
print(f"Pontuações ordenadas: {resultado['pontuações']}\n")

print(f"Nomes: {resultado['nomes']}")
resultado['nomes'].sort()
print(f"Nomes ordenados: {resultado['nomes']}\n")

print("="*60 + "\n")

# 13. Adicionando nova lista ao dicionário
print("13. ADICIONANDO NOVAS LISTAS:\n")

pessoa = {
    "nome": "Alice",
    "hobbies": ["leitura", "programação", "yoga"]
}

print(f"Pessoa: {pessoa}")

pessoa["linguagens"] = ["Python", "JavaScript", "Java"]
print(f"Após adicionar linguagens: {pessoa}\n")

print("="*60 + "\n")

# 14. Resumo visual
print("14. RESUMO:\n")

print("""
ESTRUTURA:
  dicio = {
    "chave1": [valor1, valor2, valor3],
    "chave2": [valor4, valor5],
    "chave3": [valor6]
  }

ACESSAR:
  dicio["chave1"]        → [valor1, valor2, valor3]
  dicio["chave1"][0]     → valor1
  dicio["chave1"][-1]    → valor3

MODIFICAR:
  dicio["chave1"][0] = novo_valor

ADICIONAR:
  dicio["chave1"].append(novo_valor)

REMOVER:
  dicio["chave1"].remove(valor)
  dicio["chave1"].pop()

ITERAR:
  for valor in dicio["chave1"]:
      print(valor)

OPERAÇÕES:
  len(dicio["chave1"])              → quantidade de elementos
  sum(dicio["chave1"])              → soma (se números)
  max(dicio["chave1"])              → máximo
  min(dicio["chave1"])              → mínimo
  "valor" in dicio["chave1"]        → verifica se existe
""")

print("="*60)
