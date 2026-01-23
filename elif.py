"""
Estruturas condicionais elif

O comando `elif` é uma abreviação de "else if" e permite verificar múltiplas condições.
Se a condição do `if` for falsa, a condição do primeiro `elif` é verificada.
Se essa também for falsa, os próximos `elif`s (se existirem) são verificados em ordem.
Se todas as condições do `if` e `elif`s forem falsas, o bloco de código do `else` é executado.
"""

# Pede ao usuário para digitar um número e o converte para inteiro
numero = int(input("Digite um número: "))

# Verifica se o número é maior que zero
if numero > 0:
    print("O número é positivo.")
# Se a primeira condição for falsa, verifica se o número é menor que zero
elif numero < 0:
    print("O número é negativo.")
# Se nenhuma das condições acima for verdadeira, executa este bloco
else:
    print("O número é zero.")

print("Fim do programa.")

# Outro exemplo com múltiplas condições usando elif
# Pede ao usuário para digitar a nota de um aluno
nota = float(input("Digite a nota do aluno (0-10): "))  
# Verifica a faixa da nota e imprime a situação correspondente
if nota >= 9:
    print("Aprovado com louvor!")
elif nota >= 7:
    print("Aprovado!")
elif nota >= 5:
    print("Recuperação.")
else:
    print("Reprovado.")

print("Fim do programa.")
# Exemplo de uso do elif em um loop for
# Iterando sobre uma lista de números e classificando-os
numeros = [10, -5, 0, 23, -1]
for numero in numeros:  
    if numero > 0:
        print(f"{numero} é positivo.")
    elif numero < 0:
        print(f"{numero} é negativo.")
    else:
        print(f"{numero} é zero.")  

print("Fim do programa.")