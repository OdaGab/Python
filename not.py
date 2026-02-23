# O operador lógico 'not' é usado para inverter o valor de uma expressão booleana.
# Se a expressão for verdadeira, 'not' a tornará falsa.
# Se a expressão for falsa, 'not' a tornará verdadeira.

# Exemplo 1: Invertendo um valor verdadeiro
tem_sol = True
if not tem_sol:
    print("Está chovendo.")
else:
    print("Está ensolarado.") # Esta mensagem será impressa

# Exemplo 2: Invertendo um valor falso
chovendo = False
if not chovendo:
    print("Não está chovendo, vamos passear!") # Esta mensagem será impressa
else:
    print("Está chovendo, melhor ficar em casa.")

# Exemplo 3: Usando com outras condições
idade = 20
if not (idade < 18):
    print("Você é maior de idade.") # Esta mensagem será impressa
else:
    print("Você é menor de idade.")