'''
Docstring para equacao03
Três amigos somaram suas idades. 
João tem o dobro da idade de Pedro. 
Carlos tem a mesma idade de Pedro. 
A soma das idades é 60 anos. Qual é a idade de cada um?
'''

# Definição do problema:
# Idade de Pedro = P
# Idade de João = 2 * P
# Idade de Carlos = P
# A soma das idades é 60: P + 2P + P = 60

# Resolvendo a equação:
# 4P = 60
# P = 60 / 4
# P = 15

# Atribuindo as idades com base na solução
idade_pedro = 15
idade_joao = 2 * idade_pedro
idade_carlos = idade_pedro

# Verificando a soma
soma_idades = idade_joao + idade_pedro + idade_carlos

# Exibindo os resultados
print(f"A idade de Pedro é {idade_pedro} anos.")
print(f"A idade de João é {idade_joao} anos.")
print(f"A idade de Carlos é {idade_carlos} anos.")
print(f"A soma das idades é {soma_idades} anos.")
