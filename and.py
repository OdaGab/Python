# O operador lógico 'and' é usado para combinar duas ou mais expressões condicionais.
# A expressão inteira será verdadeira somente se todas as expressões individuais forem verdadeiras.
# Se pelo menos uma das expressões for falsa, a expressão inteira será falsa.

# Exemplo 1: Ambas as condições são verdadeiras
idade = 25
tem_carteira_de_motorista = True

if idade >= 18 and tem_carteira_de_motorista:
    print("Você pode dirigir.") # Esta mensagem será impressa
else:
    print("Você não pode dirigir.")

# Exemplo 2: Uma das condições é falsa
idade = 17
tem_carteira_de_motorista = True

if idade >= 18 and tem_carteira_de_motorista:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.") # Esta mensagem será impressa

# Exemplo 3: Ambas as condições são falsas
idade = 16
tem_carteira_de_motorista = False

if idade >= 18 and tem_carteira_de_motorista:
    print("Você pode dirigir.")
else:
    print("Você não pode dirigir.") # Esta mensagem será impressa