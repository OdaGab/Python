# Este arquivo demonstra o uso de estruturas condicionais (if, elif, else) em Python.
# O comando `if` permite que o programa execute um bloco de código apenas se uma determinada condição for verdadeira.

print("--- Exemplo 1: Simples if ---")
idade = 20
print(f"Idade informada: {idade}")

if idade >= 18:
    print("Acesso permitido. Você é maior de idade.")


# Linha em branco para separar os exemplos

# O comando `else` pode ser usado com o `if` para fornecer um bloco de código alternativo
# que será executado se a condição do `if` for falsa.

print("--- Exemplo 2: if-else ---")
idade = 16
print(f"Idade informada: {idade}")

if idade >= 18:
    print("Acesso permitido. Você é maior de idade.")
else:
    print("Acesso negado. Você é menor de idade.")


# O comando `elif` (uma contração de "else if") permite verificar múltiplas condições em sequência.
# O programa executa o bloco de código do primeiro `if` ou `elif` cuja condição for verdadeira.
# O `else` no final é opcional e é executado se nenhuma das condições anteriores for verdadeira.

print("--- Exemplo 3: if-elif-else ---")
nota = 75
print(f"Nota do aluno: {nota}")

if nota >= 90:
    print("Conceito: A")
elif nota >= 80:
    print("Conceito: B")
elif nota >= 70:
    print("Conceito: C")
elif nota >= 60:
    print("Conceito: D")
else:
    print("Conceito: F (Reprovado)")


print("--- Exemplo 4: Condicionais com operadores lógicos (and, or, not) ---")
temperatura = 28
chovendo = False
print(f"Condições atuais -> Temperatura: {temperatura}°C, Chovendo: {chovendo}")

if temperatura > 25 and not chovendo:
    print("Sugestão: Ótimo dia para ir à praia!")
elif temperatura < 15 or chovendo:
    print("Sugestão: Que tal um filme em casa?")
else:
    print("Sugestão: O tempo está agradável.")
