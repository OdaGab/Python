# Problema: "O quádruplo de um número mais 10 é igual ao triplo do mesmo número mais 22."
#
# Equação:
# 4x + 10 = 3x + 22
#
# Resolvendo:
# 4x - 3x = 22 - 10
# x = 12

numero = 12

# Calculando cada lado da equação para verificação
lado_esquerdo = (4 * numero) + 10
lado_direito = (3 * numero) + 22

print(f"O número da caça é {numero}.")
print(f"Verificação:")
print(f"Lado esquerdo (4 * {numero} + 10) = {lado_esquerdo}")
print(f"Lado direito (3 * {numero} + 22) = {lado_direito}")
print(f"Os dois lados são iguais: {lado_esquerdo == lado_direito}")
