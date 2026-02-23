
# .center()
# Centraliza a string em um tamanho específico, preenchendo com espaços (ou outro caractere)
texto = "Python"
print(f"'{texto.center(20)}'")  # Centraliza em 20 caracteres
print(f"'{texto.center(20, '*')}'") # Centraliza e preenche com '*'

# .ljust()
# Justifica a string à esquerda em um tamanho específico, preenchendo com espaços
print(f"'{texto.ljust(20)}'")
print(f"'{texto.ljust(20, '-')}'")

# f-strings para posicionamento
# Usando f-strings, podemos controlar o alinhamento de forma mais flexível.
# :<  -> Alinha à esquerda
# :>  -> Alinha à direita
# :^  -> Centraliza

# Alinhado à esquerda
print(f"'{texto:<20}'")

# Alinhado à direita
print(f"'{texto:>20}'")

# Centralizado
print(f"'{texto:^20}'")

# Com preenchimento
print(f"'{texto:*^20}'")
