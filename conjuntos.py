# Teoria dos Conjuntos em Python

print("="*70)
print("TEORIA DOS CONJUNTOS EM PYTHON")
print("="*70 + "\n")

# Explicação básica
print("CONCEITOS BÁSICOS DA TEORIA DOS CONJUNTOS\n")
print("""
Um CONJUNTO é uma coleção de elementos únicos, sem ordem.

OPERAÇÕES FUNDAMENTAIS:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. UNIÃO (A ∪ B)
   Todos os elementos de A ou B (ou em ambos)
   
2. INTERSECÇÃO (A ∩ B)
   Elementos que estão em A e em B simultaneamente
   
3. DIFERENÇA (A - B)
   Elementos que estão em A mas não em B
   
4. DIFERENÇA SIMÉTRICA (A △ B)
   Elementos que estão em A ou B, mas não em ambos
   
5. COMPLEMENTO (A')
   Elementos que não estão em A
   
6. SUBCONJUNTO (A ⊆ B)
   Todos os elementos de A estão em B
   
7. SUPERCONJUNTO (A ⊇ B)
   A contém todos os elementos de B
""")

print("="*70 + "\n")

# 1. União (Union)
print("1. UNIÃO (A ∪ B) - TODOS OS ELEMENTOS:\n")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}\n")

uniao = A | B
print(f"A ∪ B = {A} ∪ {B}")
print(f"Resultado: {uniao}\n")

print("Interpretação: Todos os elementos de A e B (sem repetição)")
print("Método: A.union(B) ou A | B\n")

print("="*70 + "\n")

# 2. Intersecção (Intersection)
print("2. INTERSECÇÃO (A ∩ B) - ELEMENTOS EM COMUM:\n")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}\n")

intersecao = A & B
print(f"A ∩ B = {A} ∩ {B}")
print(f"Resultado: {intersecao}\n")

print("Interpretação: Apenas elementos que estão em A E B")
print("Método: A.intersection(B) ou A & B\n")

print("="*70 + "\n")

# 3. Diferença (Difference)
print("3. DIFERENÇA (A - B) - ELEMENTOS APENAS EM A:\n")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}\n")

diferenca_ab = A - B
diferenca_ba = B - A

print(f"A - B = {A} - {B}")
print(f"Resultado: {diferenca_ab}")
print(f"(Elementos em A mas não em B)\n")

print(f"B - A = {B} - {A}")
print(f"Resultado: {diferenca_ba}")
print(f"(Elementos em B mas não em A)\n")

print("Interpretação: Elementos exclusivos de cada conjunto")
print("Método: A.difference(B) ou A - B\n")

print("="*70 + "\n")

# 4. Diferença Simétrica (Symmetric Difference)
print("4. DIFERENÇA SIMÉTRICA (A △ B) - ELEMENTOS ÚNICOS:\n")

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print(f"A = {A}")
print(f"B = {B}\n")

dif_simetrica = A ^ B
print(f"A △ B = {A} △ {B}")
print(f"Resultado: {dif_simetrica}\n")

print("Interpretação: Elementos em A ou B, mas NÃO em ambos")
print("Método: A.symmetric_difference(B) ou A ^ B\n")

print("="*70 + "\n")

# 5. Complemento (Complement)
print("5. COMPLEMENTO (A') - ELEMENTOS FORA DO CONJUNTO:\n")

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}  # Universo
A = {1, 2, 3, 4}

print(f"Universo U = {U}")
print(f"A = {A}\n")

complemento = U - A
print(f"A' (complemento de A) = U - A")
print(f"Resultado: {complemento}\n")

print("Interpretação: Elementos que estão em U mas não em A")
print("Método: U - A\n")

print("="*70 + "\n")

# 6. Subconjunto (Subset)
print("6. SUBCONJUNTO (A ⊆ B) - A ESTÁ CONTIDO EM B:\n")

A = {1, 2}
B = {1, 2, 3, 4}
C = {2, 3}

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}\n")

print(f"A ⊆ B? {A <= B} (verdadeiro - todos elementos de A estão em B)")
print(f"A ⊂ B? {A < B} (verdadeiro - subconjunto próprio)")
print(f"B ⊆ A? {B <= A} (falso - B tem elementos não em A)")
print(f"C ⊆ B? {C <= B} (verdadeiro)\n")

print("Métodos: A.issubset(B) ou A <= B\n")

print("="*70 + "\n")

# 7. Superconjunto (Superset)
print("7. SUPERCONJUNTO (A ⊇ B) - A CONTÉM B:\n")

A = {1, 2, 3, 4}
B = {1, 2}

print(f"A = {A}")
print(f"B = {B}\n")

print(f"A ⊇ B? {A >= B} (verdadeiro - A contém todos elementos de B)")
print(f"A ⊃ B? {A > B} (verdadeiro - superconjunto próprio)")
print(f"B ⊇ A? {B >= A} (falso)\n")

print("Métodos: A.issuperset(B) ou A >= B\n")

print("="*70 + "\n")

# 8. Disjuntos (Disjoint)
print("8. CONJUNTOS DISJUNTOS (SEM ELEMENTOS EM COMUM):\n")

A = {1, 2, 3}
B = {4, 5, 6}
C = {3, 4, 5}

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}\n")

print(f"A ∩ B = {A & B} (vazio - disjuntos)")
print(f"A.isdisjoint(B)? {A.isdisjoint(B)} (verdadeiro)\n")

print(f"A ∩ C = {A & C} (tem elementos em comum)")
print(f"A.isdisjoint(C)? {A.isdisjoint(C)} (falso)\n")

print("Interpretação: Conjuntos disjuntos não compartilham elementos")
print("Método: A.isdisjoint(B)\n")

print("="*70 + "\n")

# 9. Visualização com diagrama de Venn
print("9. VISUALIZAÇÃO COM DIAGRAMA DE VENN:\n")

print("""
UNIÃO (A ∪ B):           INTERSECÇÃO (A ∩ B):
    A       B                A       B
  ┌─────────────┐         ┌─────────────┐
  │░░░  │ X  │ ░░│         │      │ X │      │
  │░░░  │ X  │ ░░│         │      │ X │      │
  │░░░░░│ X  │░░░│         │      │ X │      │
  └─────────────┘         └─────────────┘
  (tudo preenchido)      (só o meio)


DIFERENÇA (A - B):       DIFERENÇA SIMÉTRICA (A △ B):
    A       B                A       B
  ┌─────────────┐         ┌─────────────┐
  │░░░  │   │      │        │░░░  │   │ ░░│
  │░░░  │   │      │        │░░░  │   │ ░░│
  │░░░░░│   │      │        │░░░░░│   │░░░│
  └─────────────┘         └─────────────┘
  (só à esquerda)        (esquerda e direita)
""")

print("="*70 + "\n")

# 10. Exemplo prático: Alunos em cursos
print("10. EXEMPLO PRÁTICO: ALUNOS EM CURSOS:\n")

python = {"Ana", "Bruno", "Carlos", "Diana", "Eduardo"}
java = {"Carlos", "Diana", "Fernanda", "Gustavo"}
web = {"Ana", "Fernanda", "Helena", "Igor"}

print(f"Python: {python}")
print(f"Java: {java}")
print(f"Web: {web}\n")

# União
todos = python | java | web
print(f"Alunos em ALGUM curso: {sorted(todos)}")
print(f"Total: {len(todos)} alunos\n")

# Intersecção
python_java = python & java
print(f"Alunos em Python E Java: {python_java}")

python_java_web = python & java & web
print(f"Alunos em Python E Java E Web: {python_java_web}\n")

# Diferença
apenas_python = python - java - web
print(f"Alunos APENAS em Python: {apenas_python}")

apenas_java = java - python - web
print(f"Alunos APENAS em Java: {apenas_java}\n")

# Subconjunto
if python_java <= python:
    print(f"✓ Alunos em (Python ∩ Java) ⊆ Python\n")

print("="*70 + "\n")

# 11. Exemplo prático: Produtos em estoque
print("11. EXEMPLO PRÁTICO: PRODUTOS EM ESTOQUE:\n")

loja_sp = {"notebook", "mouse", "teclado", "monitor", "webcam"}
loja_rj = {"mouse", "teclado", "fone", "webcam", "impressora"}
loja_mg = {"notebook", "monitor", "fone", "impressora", "scanner"}

print(f"Loja SP: {loja_sp}")
print(f"Loja RJ: {loja_rj}")
print(f"Loja MG: {loja_mg}\n")

# Produtos em todas as lojas
em_tudo = loja_sp & loja_rj & loja_mg
print(f"Produtos em TODAS as lojas: {em_tudo}")

# Produtos em alguma loja
em_alguma = loja_sp | loja_rj | loja_mg
print(f"Produtos em ALGUMA loja: {sorted(em_alguma)}\n")

# Produtos exclusivos de SP
exclusivo_sp = loja_sp - loja_rj - loja_mg
print(f"Produtos exclusivos de SP: {exclusivo_sp}")

# Produtos não em SP
fora_sp = (loja_rj | loja_mg) - loja_sp
print(f"Produtos não em SP: {fora_sp}\n")

print("="*70 + "\n")

# 12. Lei De Morgan
print("12. LEIS DE MORGAN:\n")

print("""
Lei 1: (A ∪ B)' = A' ∩ B'
       Complemento da união = Intersecção dos complementos

Lei 2: (A ∩ B)' = A' ∪ B'
       Complemento da intersecção = União dos complementos

Vamos verificar:
""")

U = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A_comp = U - A
B_comp = U - B

# Lei 1
uniao = A | B
uniao_comp = U - uniao
intersecao_comp = A_comp & B_comp

print(f"\nLei De Morgan 1: (A ∪ B)' = A' ∩ B'")
print(f"A = {A}")
print(f"B = {B}")
print(f"(A ∪ B)' = {uniao_comp}")
print(f"A' ∩ B' = {intersecao_comp}")
print(f"Iguais? {uniao_comp == intersecao_comp} ✓\n")

# Lei 2
intersecao = A & B
intersecao_comp2 = U - intersecao
uniao_comp2 = A_comp | B_comp

print(f"Lei De Morgan 2: (A ∩ B)' = A' ∪ B'")
print(f"(A ∩ B)' = {intersecao_comp2}")
print(f"A' ∪ B' = {uniao_comp2}")
print(f"Iguais? {intersecao_comp2 == uniao_comp2} ✓\n")

print("="*70 + "\n")

# 13. Propriedades dos conjuntos
print("13. PROPRIEDADES DOS CONJUNTOS:\n")

A = {1, 2, 3}
B = {2, 3, 4}
C = {3, 4, 5}

print("""
COMUTATIVIDADE:
✓ A ∪ B = B ∪ A (ordem não importa na união)
✓ A ∩ B = B ∩ A (ordem não importa na intersecção)
""")

print(f"A ∪ B = {A | B}")
print(f"B ∪ A = {B | A}")
print(f"Iguais? {(A | B) == (B | A)} ✓\n")

print("""
ASSOCIATIVIDADE:
✓ (A ∪ B) ∪ C = A ∪ (B ∪ C)
✓ (A ∩ B) ∩ C = A ∩ (B ∩ C)
""")

uniao1 = (A | B) | C
uniao2 = A | (B | C)
print(f"(A ∪ B) ∪ C = {uniao1}")
print(f"A ∪ (B ∪ C) = {uniao2}")
print(f"Iguais? {uniao1 == uniao2} ✓\n")

print("""
IDENTIDADE:
✓ A ∪ ∅ = A (união com vazio = A)
✓ A ∩ ∅ = ∅ (intersecção com vazio = vazio)
""")

vazio = set()
print(f"A = {A}")
print(f"A ∪ ∅ = {A | vazio}")
print(f"A ∩ ∅ = {A & vazio}\n")

print("="*70 + "\n")

# 14. Método pairs: todos os métodos
print("14. RESUMO DE MÉTODOS:\n")

A = {1, 2, 3}
B = {2, 3, 4}

print(f"A = {A}")
print(f"B = {B}\n")

print(f"A | B              ou A.union(B)              = {A | B}")
print(f"A & B              ou A.intersection(B)       = {A & B}")
print(f"A - B              ou A.difference(B)         = {A - B}")
print(f"A ^ B              ou A.symmetric_difference  = {A ^ B}")
print(f"A <= B             ou A.issubset(B)           = {A <= B}")
print(f"A >= B             ou A.issuperset(B)         = {A >= B}")
print(f"A < B              (subconjunto próprio)      = {A < B}")
print(f"A > B              (superconjunto próprio)    = {A > B}")
print(f"A == B             (igualdade)                = {A == B}")
print(f"A.isdisjoint(B)    (sem elemento em comum)    = {A.isdisjoint(B)}\n")

print("="*70 + "\n")

# 15. Exemplo: Classificação
print("15. EXEMPLO: CLASSIFICAÇÃO DE PESSOAS:\n")

programadores = {"Ana", "Bruno", "Carlos", "Diana"}
designers = {"Ana", "Eduardo", "Fernanda"}
gestores = {"Gustavo", "Helena", "Igor"}

print(f"Programadores: {programadores}")
print(f"Designers: {designers}")
print(f"Gestores: {gestores}\n")

# Múltiplas competências
prog_design = programadores & designers
print(f"Prog E Designer: {prog_design}")

prog_ou_design = programadores | designers
print(f"Prog OU Designer: {prog_ou_design}")

# Exclusivamente
so_prog = programadores - designers - gestores
print(f"SÓ Programadores: {so_prog}")

# Nenhuma categoria
nenhuma = (programadores | designers | gestores)
todos = programadores | designers | gestores
print(f"Pessoas em alguma categoria: {todos}\n")

print("="*70 + "\n")

# 16. Resumo final
print("16. RESUMO FINAL:\n")

print("""
╔═══════════════════════════════════════════════════════════════╗
║ OPERAÇÕES FUNDAMENTAIS DA TEORIA DOS CONJUNTOS              ║
╚═══════════════════════════════════════════════════════════════╝

┌─────────────────────────────────────────────────────────────┐
│ OPERAÇÃO        │ SÍMBOLO │ PYTHON │ SIGNIFICADO            │
├─────────────────────────────────────────────────────────────┤
│ União           │    ∪    │   |    │ Tudo de A e B          │
│ Intersecção     │    ∩    │   &    │ Comum de A e B         │
│ Diferença       │    −    │   -    │ Em A mas não em B      │
│ Dif. Simétrica  │    △    │   ^    │ Em A ou B, não ambos   │
│ Complemento     │    '    │   -    │ Fora de A (em U)       │
│ Subconjunto     │    ⊆    │   <=   │ A contido em B         │
│ Superconjunto   │    ⊇    │   >=   │ A contém B             │
│ Disjuntos       │         │ < , >  │ A e B não relacionados │
└─────────────────────────────────────────────────────────────┘

PROPRIEDADES:
✓ Comutativa: A ∪ B = B ∪ A
✓ Associativa: (A ∪ B) ∪ C = A ∪ (B ∪ C)
✓ Identidade: A ∪ ∅ = A
✓ Distributiva: A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
✓ Lei De Morgan: (A ∪ B)' = A' ∩ B'

CASOS DE USO:
• Encontrar elementos únicos
• Eliminar duplicatas
• Agrupar e comparar coleções
• Análise de dados
• Filtros e permissões
• Recomendações
""")

print("="*70)
