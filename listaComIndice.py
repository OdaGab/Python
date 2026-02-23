# Criando uma lista de exemplo
frutas = ["maçã", "banana", "laranja", "uva", "manga"]

# Os índices em uma lista começam em 0.
# Então, o primeiro elemento tem índice 0, o segundo tem índice 1, e assim por diante.

# Acessando elementos por seu índice
primeira_fruta = frutas[0]  # Acessa o primeiro elemento: "maçã"
terceira_fruta = frutas[2]  # Acessa o terceiro elemento: "laranja"

print(f"A lista completa de frutas é: {frutas}")
print(f"A primeira fruta (índice 0) é: {primeira_fruta}")
print(f"A terceira fruta (índice 2) é: {terceira_fruta}")

# Também podemos usar índices negativos para começar do final da lista
ultima_fruta = frutas[-1]  # Acessa o último elemento: "manga"
penultima_fruta = frutas[-2] # Acessa o penúltimo elemento: "uva"

print(f"A última fruta (índice -1) é: {ultima_fruta}")
print(f"A penúltima fruta (índice -2) é: {penultima_fruta}")

# Modificando um elemento da lista usando seu índice
print(f"\nLista antes da modificação: {frutas}")
frutas[1] = "morango"  # Troca "banana" por "morango"
print(f"Lista após a modificação no índice 1: {frutas}")

# Obtendo o tamanho da lista para saber o último índice válido
tamanho_lista = len(frutas)
print(f"\nA lista tem {tamanho_lista} elementos.")
print(f"Os índices válidos vão de 0 a {tamanho_lista - 1}.")
