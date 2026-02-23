# .strip(), .lstrip(), .rstrip()
# Removem espaços em branco (ou outros caracteres especificados) do início,
# do fim ou de ambos os lados de uma string.

texto = "   Olá, Mundo!   "
print(f"Original:        '{texto}'")

# .strip() -> remove de ambos os lados
texto_strip = texto.strip()
print(f"Com .strip():    '{texto_strip}'")

# .lstrip() -> remove do lado esquerdo (left)
texto_lstrip = texto.lstrip()
print(f"Com .lstrip():   '{texto_lstrip}'")

# .rstrip() -> remove do lado direito (right)
texto_rstrip = texto.rstrip()
print(f"Com .rstrip():   '{texto_rstrip}'")


# Removendo caracteres específicos
# Podemos passar um argumento para especificar quais caracteres remover.

texto_com_chars = ".,.Olá, Mundo!.,."
print(f"\nOriginal com chars: '{texto_com_chars}'")

# Removendo '.' e ',' dos lados
texto_strip_chars = texto_com_chars.strip('.,')
print(f"Com .strip('.,'):  '{texto_strip_chars}'")
