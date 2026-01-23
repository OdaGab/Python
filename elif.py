# A estrutura de controle elif (abreviação de "else if") em Python
# permite que você verifique múltiplas condições em sequência.

# O elif é executado somente se a condição do if inicial for falsa.
# Se a condição do elif for verdadeira, o bloco de código correspondente
# é executado e o resto da estrutura (outros elifs e o else) é ignorado.
# Você pode ter vários elifs em uma única estrutura if.

# Exemplo:
idade = 25

if idade < 18:
    print("Você é menor de idade.")
elif idade >= 18 and idade < 60:
    print("Você é um adulto.")
else:
    print("Você é um idoso.")

# Outro exemplo com mais de um elif
nota = 85

if nota >= 90:
    print("Conceito A")
elif nota >= 80:
    print("Conceito B")
elif nota >= 70:
    print("Conceito C")
elif nota >= 60:
    print("Conceito D")
else:
    print("Conceito F")
