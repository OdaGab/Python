
# .replace()
# Retorna uma cópia da string com todas as ocorrências de uma substring
# substituídas por outra.

# Sintaxe: string.replace(old, new, count)
# old - A substring a ser substituída.
# new - A nova substring que substituirá a antiga.
# count (opcional) - O número de ocorrências a serem substituídas.
# Se não for especificado, todas as ocorrências são substituídas.

texto = "O rato roeu a roupa do rei de Roma."
print(f"Original: '{texto}'")

# Substituindo todas as ocorrências de 'r' por 'l'
texto_substituido = texto.replace('r', 'l')
print(f"Substituindo 'r' por 'l': '{texto_substituido}'")

# Substituindo a palavra 'rato' por 'gato'
texto_substituido_palavra = texto.replace('rato', 'gato')
print(f"Substituindo 'rato' por 'gato': '{texto_substituido_palavra}'")

# Substituindo apenas as duas primeiras ocorrências de 'ro' por '##'
texto_contado = texto.replace('ro', '##', 2)
print(f"Substituindo as 2 primeiras 'ro': '{texto_contado}'")
