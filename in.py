# O operador 'in' verifica a presença de um elemento em uma sequência.
# Retorna True se o valor especificado for encontrado na sequência, e False caso contrário.

# Exemplo com uma lista de frutas
frutas = ["maçã", "banana", "laranja"]
print(f"A lista de frutas é: {frutas}")

# Verificando se 'banana' está na lista de frutas
if "banana" in frutas:
    print("'banana' está na lista de frutas.")
else:
    print("'banana' não está na lista de frutas.")

# Verificando se 'abacaxi' está na lista de frutas
if "abacaxi" in frutas:
    print("'abacaxi' está na lista de frutas.")
else:
    print("'abacaxi' não está na lista de frutas.")


# Exemplo com uma string
texto = "Olá, mundo!"
print(f"\nO texto é: '{texto}'")

# Verificando se a substring 'mundo' está no texto
if "mundo" in texto:
    print("A substring 'mundo' está no texto.")
else:
    print("A substring 'mundo' não está no texto.")


# Exemplo com um dicionário (verifica as chaves)
pessoa = {"nome": "Carlos", "idade": 30}
print(f"\nO dicionário de pessoa é: {pessoa}")

# Verificando se a chave 'nome' existe no dicionário
if "nome" in pessoa:
    print("A chave 'nome' existe no dicionário.")
else:
    print("A chave 'nome' não existe no dicionário.")

# Verificando se a chave 'profissão' existe no dicionário
if "profissão" in pessoa:
    print("A chave 'profissão' existe no dicionário.")
else:
    print("A chave 'profissão' não existe no dicionário.")

# Para verificar a existência de um valor, usamos o método values()
if 30 in pessoa.values():
    print("O valor 30 existe no dicionário.")
else:
    print("O valor 30 não existe no dicionário.")
