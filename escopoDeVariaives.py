
# O escopo de uma variável em Python se refere à região do código onde essa variável é acessível.
# Em outras palavras, ele define onde você pode usar uma variável. Python tem principalmente dois tipos de escopo:
# - Escopo Local: A variável é criada dentro de uma função e só pode ser usada dentro dessa função.
# - Escopo Global: A variável é criada fora de qualquer função e pode ser acessada em qualquer lugar do seu código.

# Variável Global: Definida fora de qualquer função, acessível em todo o programa.

nome = "Mundo"

def saudacao():
    # Variável Local: Definida dentro de uma função, acessível apenas nela.
    saudacao_local = "Olá"
    print(f"{saudacao_local}, {nome}!") # Acessa a variável global 'nome'

def saudacao_com_parametro(nome_parametro):
    # O parâmetro da função também atua como uma variável local.
    print(f"Bem-vindo, {nome_parametro}!")

print("--- Chamando a primeira função ---")
saudacao()

print("\n--- Chamando a segunda função ---")
saudacao_com_parametro("Alice")

# Tentando acessar uma variável local fora de seu escopo (isso vai gerar um erro)
try:
    print(saudacao_local)
except NameError as e:
    print(f"\n--- Tentativa de acessar variável local ---")
    print(f"Erro esperado: {e}")

print(f"\n--- Acessando a variável global diretamente ---")
print(f"O nome global é: {nome}")
