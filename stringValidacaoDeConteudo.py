
# Métodos de Validação de Conteúdo de Strings

# .isalnum()
# Retorna True se todos os caracteres na string forem alfanuméricos (letras ou números)
# e houver pelo menos um caractere. Retorna False caso contrário.
print("--- .isalnum() ---")
print(f"'Python123'.isalnum() -> { 'Python123'.isalnum() }") # True
print(f"'Python 123'.isalnum() -> { 'Python 123'.isalnum() }") # False, contém espaço
print(f"'Python-123'.isalnum() -> { 'Python-123'.isalnum() }") # False, contém hífen
print(f"'123'.isalnum() -> { '123'.isalnum() }")               # True
print(f"''.isalnum() -> { ''.isalnum() }")                     # False, string vazia

# .isalpha()
# Retorna True se todos os caracteres na string forem alfabéticos (letras)
# e houver pelo menos um caractere. Retorna False caso contrário.
print("\n--- .isalpha() ---")
print(f"'Python'.isalpha() -> { 'Python'.isalpha() }")     # True
print(f"'PythonBR'.isalpha() -> { 'PythonBR'.isalpha() }") # True
print(f"'Python 1'.isalpha() -> { 'Python 1'.isalpha() }") # False, contém espaço e número
print(f"'Python-'.isalpha() -> { 'Python-'.isalpha() }")   # False, contém hífen
print(f"''.isalpha() -> { ''.isalpha() }")                 # False, string vazia

# .isdigit()
# Retorna True se todos os caracteres na string forem dígitos (0-9).
print("\n--- .isdigit() ---")
print(f"'123'.isdigit() -> { '123'.isdigit() }")   # True
print(f"'123.4'.isdigit() -> { '123.4'.isdigit() }") # False, contém ponto
print(f"'-123'.isdigit() -> { '-123'.isdigit() }") # False, contém sinal

# .isnumeric()
# Similar a isdigit(), mas aceita uma gama maior de caracteres numéricos (ex: frações).
print("\n--- .isnumeric() ---")
print(f"'123'.isnumeric() -> { '123'.isnumeric() }")      # True
print(f"'¹²³'.isnumeric() -> { '¹²³'.isnumeric() }")      # True (dígitos de expoente)
print(f"'½'.isnumeric() -> { '½'.isnumeric() }")        # True (fração)

# .isupper()
# Retorna True se todos os caracteres com caixa (letras) na string forem maiúsculos.
print("\n--- .isupper() ---")
print(f"'PYTHON'.isupper() -> { 'PYTHON'.isupper() }")     # True
print(f"'Python'.isupper() -> { 'Python'.isupper() }")     # False
print(f"'PYTHON 123'.isupper() -> { 'PYTHON 123'.isupper() }") # True

# .islower()
# Retorna True se todos os caracteres com caixa (letras) na string forem minúsculos.
print("\n--- .islower() ---")
print(f"'python'.islower() -> { 'python'.islower() }")     # True
print(f"'Python'.islower() -> { 'Python'.islower() }")     # False
print(f"'python 123'.islower() -> { 'python 123'.islower() }") # True

# .isspace()
# Retorna True se todos os caracteres na string forem espaços em branco.
print("\n--- .isspace() ---")
print(f"' '.isspace() -> { ' '.isspace() }")             # True
print(f"'  \t \n'.isspace() -> { '  \t \n'.isspace() }") # True
print(f"' a '.isspace() -> { ' a '.isspace() }")         # False

# .isprintable()
# Retorna True se todos os caracteres na string forem imprimíveis ou se a string estiver vazia.
# Caracteres não imprimíveis são, por exemplo, quebras de linha (\n) e tabulações (\t).
print("\n--- .isprintable() ---")
print(f"'Olá, Mundo!'.isprintable() -> { 'Olá, Mundo!'.isprintable() }") # True
print(f"'Olá,\nMundo!'.isprintable() -> { 'Olá,\nMundo!'.isprintable() }") # False
print(f"'\t'.isprintable() -> { '\t'.isprintable() }")                 # False
print(f"''.isprintable() -> { ''.isprintable() }")                     # True
