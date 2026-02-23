# Podemos definir um valor padrão para os parâmetros de uma função.
# Se um argumento para aquele parâmetro não for passado durante a chamada da função,
# o valor padrão definido será utilizado.

# 'saudacao_texto' tem o valor padrão "Olá".
# 'pontuacao' tem o valor padrão "!".
def saudacao(nome, saudacao_texto="Olá", pontuacao="!"):
  """
  Esta função imprime uma saudação.
  O texto da saudação e a pontuação podem ser customizados.
  """
  print(f"{saudacao_texto}, {nome}{pontuacao}")


# --- Exemplos de uso ---

# 1. Chamando a função apenas com o parâmetro obrigatório ('nome').
# A função usará os valores padrão para 'saudacao_texto' e 'pontuacao'.
print("Exemplo 1: Usando todos os padrões")
saudacao("Ana")


# 2. Chamando a função e especificando um novo texto para a saudação.
# O valor padrão de 'saudacao_texto' é substituído por "Bem-vindo".
print("\nExemplo 2: Modificando a saudação")
saudacao("Marcos", saudacao_texto="Bem-vindo")


# 3. Chamando a função e alterando todos os parâmetros.
# É possível passar os argumentos na ordem ou nomeando os parâmetros.
print("\nExemplo 3: Modificando todos os parâmetros")
saudacao("Júlia", saudacao_texto="Bom dia", pontuacao="...")
