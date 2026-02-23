# Problema: "O triplo de um número menos 5 é igual ao dobro do mesmo número mais 1."
# Equação: 3x - 5 = 2x + 1

# Resolvendo a equação:
# 3x - 2x = 1 + 5
# x = 6

numero = 6

# Calculando cada lado da equação para verificação
lado_esquerdo = (3 * numero) - 5
lado_direito = (2 * numero) + 1

print(f"O número que atende à regra é {numero}.")
print(f"Verificação:")
print(f"O triplo de {numero} menos 5 é: {lado_esquerdo}")
print(f"O dobro de {numero} mais 1 é: {lado_direito}")
print(f"Ambos os resultados são iguais: {lado_esquerdo == lado_direito}")
