
# Este arquivo demonstra como realizar cálculos de porcentagem em Python.

print("--- Cálculos com Porcentagem ---")

# Cenário 1: Calcular a porcentagem de um número.
#
# Para encontrar a porcentagem de um valor, transforme a porcentagem em um
# decimal (dividindo por 100) e multiplique pelo valor.
#
# Exemplo: Quanto é 25% de 200?
valor_total = 200
percentual = 25

resultado = (percentual / 100) * valor_total

print(f"{percentual}% de {valor_total} é: {resultado}")
print("-" * 20)


# Cenário 2: Aplicar um aumento percentual a um valor.
#
# Exemplo: Um produto custa R$ 80 e terá um aumento de 15%.
preco_inicial = 80
aumento_percentual = 15

# Calcula o valor do aumento
valor_do_aumento = (aumento_percentual / 100) * preco_inicial
# Soma o aumento ao preço inicial
preco_final_aumento = preco_inicial + valor_do_aumento

print(f"Produto de R$ {preco_inicial} com {aumento_percentual}% de aumento.")
print(f"Valor do aumento: R$ {valor_do_aumento}")
print(f"Preço final: R$ {preco_final_aumento}")

# Uma forma mais direta de calcular o preço final com aumento:
# preco_final = preco_inicial * (1 + (aumento_percentual / 100))
# print(f"Preço final (cálculo direto): R$ {preco_final}")
print("-" * 20)


# Cenário 3: Aplicar um desconto percentual a um valor.
#
# Exemplo: Um produto custa R$ 120 e está com 10% de desconto.
preco_produto = 120
desconto_percentual = 10

# Calcula o valor do desconto
valor_do_desconto = (desconto_percentual / 100) * preco_produto
# Subtrai o desconto do preço original
preco_final_desconto = preco_produto - valor_do_desconto

print(f"Produto de R$ {preco_produto} com {desconto_percentual}% de desconto.")
print(f"Valor do desconto: R$ {valor_do_desconto}")
print(f"Preço final com desconto: R$ {preco_final_desconto}")

# Uma forma mais direta de calcular o preço final com desconto:
# preco_final = preco_produto * (1 - (desconto_percentual / 100))
# print(f"Preço final (cálculo direto): R$ {preco_final}")
print("-" * 20)


# Cenário 4: Descobrir a variação percentual entre dois valores
#
# Exemplo: O número de usuários foi de 500 para 600. Qual foi o aumento percentual?
valor_antigo = 500
valor_novo = 600

variacao = valor_novo - valor_antigo
variacao_percentual = (variacao / valor_antigo) * 100

print(f"A variação de {valor_antigo} para {valor_novo} é de {variacao_percentual:.2f}%.")
print("-" * 20)

