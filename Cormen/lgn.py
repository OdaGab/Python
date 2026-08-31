# Pede ao usuário a quantidade de dias e converte para número inteiro
dia = int(input("Digite a quantidade de dias\n"))

# Define as constantes de conversão
hora = 24
segundos = 3600

# Calcula o total de segundos em um número de dias
lgn = dia * hora * segundos

# Mostra o resultado em notação científica
print(f"f(x) = lg n = {lgn:.3e}")
print(f"f(x) = lg n ≈ {lgn / 10**12:.3f} x 10^12")

