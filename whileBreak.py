# O comando 'break' serve para interromper a execução de um loop ('while' ou 'for')
# de forma imediata, mesmo que a condição do loop ainda seja verdadeira.
# O programa então continua a execução na primeira linha de código após o loop.

# Exemplo 1: Interrompendo um loop de contagem
print("--- Exemplo 1: Interrompendo a contagem no 5 ---")
contador = 1
while contador <= 10:
    print(f"Contador: {contador}")
    if contador == 5:
        print("Condição de parada atingida. Usando 'break' para sair.")
        break  # O loop para aqui, não chegará a 10.
    contador += 1
print("Execução após o primeiro loop.\n")


# Exemplo 2: Usando 'while True' com 'break'
# Este é um padrão comum para criar um loop que só termina com uma condição específica.
print("--- Exemplo 2: Loop 'infinito' controlado por 'break' ---")
while True:  # Cria um loop que, a princípio, rodaria para sempre.
    resposta = input("Digite 'sair' para terminar o programa: ")
    if resposta.lower() == 'sair':
        print("Comando 'sair' recebido. Encerrando o loop.")
        break  # A única forma de sair deste loop.
    else:
        print(f"Você digitou: {resposta}. O loop continua.")
print("Execução após o segundo loop.\n")


# Exemplo 3: Jogo de adivinhação
# O loop continua até o usuário acertar o número.
print("--- Exemplo 3: Jogo de adivinhação ---")
numero_secreto = 42

while True:
    try:
        palpite = int(input("Adivinhe o número secreto (entre 1 e 100): "))
        
        if palpite == numero_secreto:
            print("Parabéns! Você acertou!")
            break  # Sai do loop porque o jogador venceu.
        elif palpite < numero_secreto:
            print("O número secreto é maior. Tente de novo.")
        else:
            print("O número secreto é menor. Tente de novo.")
            
    except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

print("Fim do jogo.")
