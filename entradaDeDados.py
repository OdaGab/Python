import locale

# Configura a localização para o padrão brasileiro para formatação de moeda
try:
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
except locale.Error:
    print("Localização 'pt_BR.UTF-8' não suportada. Usando a localização padrão.")
    locale.setlocale(locale.LC_ALL, '')


# --- Entrada de Dados ---
print("Por favor, forneça seus dados abaixo.")
nome = input("Digite seu nome completo: ")
email = input("Digite seu e-mail: ")
idade = input("Digite sua idade: ")


# --- Tratamento de Erro para o Salário ---
while True:
    salario_str = input("Digite seu salário (ex: 3500.50 ou 3500,50): ")
    try:
        # Tenta converter para float, substituindo vírgula por ponto se necessário
        salario_float = float(salario_str.replace(',', '.'))
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Erro: Valor do salário inválido. Por favor, digite apenas números.")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


# --- Formatação e Saída dos Dados ---
# Formata o salário para o padrão de moeda brasileiro
salario_formatado = locale.currency(salario_float, grouping=True, symbol=True)

print("\n--- Dados Coletados ---")
# O 'f' antes da string (f-string) permite embutir variáveis diretamente no texto.
# O que estiver entre chaves {} será substituído pelo valor da variável.
print(f"Nome: {nome}")
print(f"E-mail: {email}")
print(f"Idade: {idade}")
print(f"Salário: {salario_formatado}")
print("------------------------")
