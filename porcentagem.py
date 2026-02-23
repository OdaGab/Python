
print("=== Operações de Porcentagem ===")
print("Aumento de salário") 

salario = 1500
aumento_percentual = 5

aumento = salario * (aumento_percentual / 100)
novo_salario = salario + aumento    
print(f"Salário original: R$ {salario}")
print(f"Aumento: R$ {aumento} ({aumento_percentual}%)")
print(f"Novo salário: R$ {novo_salario}")




print("--- Calculo de porcentagem exemplos ---")
def calcular_porcentagem(valor, porcentagem):
    return (valor * porcentagem) / 100  
valor = 200
porcentagem = 15
resultado = calcular_porcentagem(valor, porcentagem)
print(f"{porcentagem}% de {valor} é {resultado}")
print("-" * 20)

print("--- Calculo de desconto ---")
def calcular_desconto(valor, desconto):
    return valor - (valor * desconto / 100)
valor = 100
desconto = 10
resultado = calcular_desconto(valor, desconto)
print(f"O valor de {valor} com {desconto}% de desconto é {resultado}")
print("-" * 20)

print("--- Calculo de juros ---")   
def calcular_juros(valor, taxa_juros, periodo):
    return valor * (1 + taxa_juros / 100) ** periodo
valor = 1000
taxa_juros = 5
periodo = 2
resultado = calcular_juros(valor, taxa_juros, periodo)
print(f"O valor de {valor} com {taxa_juros}% de juros durante {periodo} anos é {resultado}")
print("-" * 20)

print("--- Calculo de imposto ---") 
def calcular_imposto(valor, taxa_imposto):
    return valor * (1 - taxa_imposto / 100)
valor = 1000
taxa_imposto = 10
resultado = calcular_imposto(valor, taxa_imposto)
print(f"O valor de {valor} após aplicar {taxa_imposto}% de imposto é {resultado}")
print("-" * 20)

print("--- Calculo de multa ---")   
def calcular_multa(valor, taxa_multa):
    return valor * (1 + taxa_multa / 100)
valor = 1000
taxa_multa = 5
resultado = calcular_multa(valor, taxa_multa)
print(f"O valor de {valor} com {taxa_multa}% de multa é {resultado}")
print("-" * 20)

print("--- Calculo de desconto ---")    
def calcular_valor_com_desconto(valor, desconto):
    return valor - (valor * desconto / 100)
valor = 500
desconto = 20
resultado = calcular_valor_com_desconto(valor, desconto)
print(f"O valor de {valor} com {desconto}% de desconto é {resultado}")
print("-" * 20)