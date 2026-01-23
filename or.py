
# O operador lógico 'or' (ou) retorna True se pelo menos uma das condições for verdadeira.
# Se ambas as condições forem falsas, ele retorna False.

# Exemplo 1: Uma condição é verdadeira
tem_dinheiro = True
tem_credito = False

if tem_dinheiro or tem_credito:
    print("Você pode comprar o item.")  # Este bloco será executado
else:
    print("Você não tem fundos suficientes.")

# Exemplo 2: Ambas as condições são verdadeiras
tem_sol = True
fim_de_semana = True

if tem_sol or fim_de_semana:
    print("Vamos à praia!")  # Este bloco será executado
else:
    print("Vamos ficar em casa.")

# Exemplo 3: Ambas as condições são falsas
esta_chovendo = False
esta_frio = False

if esta_chovendo or esta_frio:
    print("Leve um casaco ou um guarda-chuva.")
else:
    print("O tempo está agradável.") # Este bloco será executado

# Exemplo com entrada do usuário
try:
    idade_str = input("Digite sua idade: ")
    idade = int(idade_str)

    # Verifica se a pessoa é criança OU idosa
    if idade < 12 or idade > 65:
        print("Você tem direito a um desconto.")
    else:
        print("Você não tem direito a um desconto.")
except ValueError:
    print("Por favor, digite um número válido para a idade.")
