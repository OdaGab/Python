
# Formatação de Strings com o método .format()

# O método .format() é uma maneira poderosa e flexível de formatar strings,
# substituindo placeholders (marcados por {}) por valores.

# --- Exemplos Básicos ---

# 1. Por ordem posicional
ordem_posicional = "Olá, meu nome é {} e eu tenho {} anos.".format("Alice", 30)
print(f"Posicional: {ordem_posicional}")

# 2. Por índice
por_indice = "Eu gosto de {0} e {1}, mas {0} é minha favorita.".format("maçã", "banana")
print(f"Por Índice: {por_indice}")

# 3. Por nome (argumentos nomeados)
por_nome = "O carro é um {modelo} {ano} da cor {cor}.".format(modelo="Fusca", ano=1970, cor="azul")
print(f"Por Nome:   {por_nome}")


# --- Formatação Avançada com .format() ---

# Podemos controlar o alinhamento, preenchimento e tipo de dado.
# Sintaxe: {nome_ou_indice:preenchimento alinhamento largura .precisão tipo}

numero = 123.4567

# Alinhamento
print("\n--- Alinhamento ---")
print("'{: >20}'".format("direita"))  # Alinha à direita em 20 espaços
print("'{: <20}'".format("esquerda")) # Alinha à esquerda
print("'{: ^20}'".format("centro"))   # Centraliza

# Preenchimento e Alinhamento
print("\n--- Preenchimento ---")
print("'{:*^20}'".format("centro")) # Centraliza com '*' como preenchimento

# Controle de Casas Decimais (Precisão)
print("\n--- Precisão Numérica ---")
print("Número original: {}".format(numero))
print("Com 2 casas decimais: {:.2f}".format(numero)) # 'f' para float

# Formatação como porcentagem
print("\n--- Porcentagem ---")
print("Como porcentagem: {:.1%}".format(0.758)) # 75.8%

# Formatação como moeda
print("\n--- Moeda ---")
valor = 1234.56
print("Valor em moeda: R$ {:,.2f}".format(valor)) # R$ 1,234.56 

# formatação de Numeros Inteiros com separador de milhares
print("\n--- Inteiros com Separador de Milhares ---")
grande_numero = 10000000
print("Número com separador de milhares: {:,}".format(grande_numero)) # Saída: 10,000,000

# Exemplo de iteração e validação (assumindo que 'nome' está definido em algum lugar antes)
# emails = ["exemplo@email.com", "email_invalido", "spam@email.com", "outro@email.com"]
# print("Validando emails:\n")
# for email in emails:
#     if "@" in email:
#         print(f"✓ '{email}' é um email válido.")
#     else:
#         print(f"✗ '{email}' não é um email válido.")
#     if "spam" in email:
#         print(f"✗ '{email}' contém termo proibido 'spam'.")
#     else:
#         print(f"✓ '{email}' não contém termo proibido 'spam'.")   
#     # A linha abaixo parece estar fora de contexto ou incompleta, pois 'nome' não é definido aqui.
#     # Se 'nome' for uma variável que deveria ser usada, ela precisa ser definida.
#     # Exemplo: Se 'nome' fosse o email atual, seria:
#     # if "@" in email and "spam" not in email:
#     #     print(f"✓ '{email}' é um email válido e não contém spam.")
#     # else:
#     #     print(f"✗ '{email}' é inválido ou contém spam.")
#     # print(f"✓ '{nome}' contém ambos os nomes") 
# else:
#     print(f"✗ '{nome}' não contém ambos os nomes")

print("Número formatado: {:,}".format(grande_numero))  # Saída: 10,000,000
