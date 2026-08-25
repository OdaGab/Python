print("Digite o valor: ")
valor = float(input())

print(f"Preço R$: {valor:.2f}")
desconto = valor * 0.10
print(f"Desconto R$: {desconto:.2f}")

precoFinal = valor - desconto
print(f"Preço final: R$ {precoFinal:.2f}")