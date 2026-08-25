print("Salário Atural: ")
valorS = float(input())

salarioAumento = valorS * 0.15
print(f"Aumento R$: {salarioAumento:.2f}")

salarioAtual = valorS + salarioAumento
print(f"Novo Salário: R$ {salarioAtual:.2f}")