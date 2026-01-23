# --- Recapitulação das Estruturas de Repetição em Python ---

print("### 01 - Loop for ###")
# O loop 'for' é usado para iterar sobre uma sequência (como uma lista ou string).

lista_de_tarefas = ["Lavar a louça", "Passear com o cachorro", "Estudar Python"]
print("Suas tarefas para hoje são:")
for tarefa in lista_de_tarefas:
    print(f"- {tarefa}")


print("\n### 02 - Entendendo a função range() ###")
# A função range() gera uma sequência de números, muito usada com o loop 'for'.

# Contagem de 1 a 5
print("\nContagem simples de 1 a 5:")
for numero in range(1, 6):  # Gera números de 1 até (6-1)=5
    print(f"Número: {numero}")

# Tabuada do 5 usando for e range
print("\nTabuada do 5:")
for i in range(1, 11): # Gera números de 1 a 10
    resultado = 5 * i
    print(f"5 x {i} = {resultado}")


print("\n### 03 - Loop while ###")
# O loop 'while' executa um bloco de código enquanto uma condição for verdadeira.

# Exemplo de uma contagem regressiva para um lançamento
print("\nContagem regressiva:")
contador = 5
while contador > 0:
    print(f"{contador}...")
    contador -= 1  # Decrementa o contador para evitar um loop infinito
print("Lançar!")


print("\n### 04 - Loop while com Break ###")
# O comando 'break' é usado para sair de um loop imediatamente.

# Exemplo de um menu simples que espera o comando 'sair'
print("\nBem-vindo ao menu. Digite 'sair' para terminar.")
while True:  # Este loop continuaria para sempre sem um 'break'
    comando = input("Digite seu comando: ")
    if comando.lower() == 'sair':
        print("Encerrando o programa...")
        break  # Interrompe o loop
    else:
        print(f"Comando '{comando}' não reconhecido. Tente novamente.")

print("\n--- Fim da recapitulação ---")
