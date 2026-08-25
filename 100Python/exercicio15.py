import locale
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

print("Preço unitário: ")
precoUnitario = float(input())

print("Quantidade: ")
quantidade = int(input())

print("Frete: ")
frete = float(input())

print(" ")

subTotal = precoUnitario * quantidade
print(f"Subtotal ",locale.currency(subTotal, grouping=True, international=False))

total = frete + (precoUnitario * quantidade)
print(f"Total ",locale.currency(total, grouping=True, international=False))