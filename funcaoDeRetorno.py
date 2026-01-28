# Uma função que retorna um valor
# Definimos uma função chamada 'quadrado' que recebe um argumento 'numero'
# Ela retorna o quadrado do número fornecido

def quadrado(numero):
  """Esta função retorna o quadrado de um número."""
  return numero ** 2

# Exemplo de uso
# Chamamos a função com o argumento 4
resultado = quadrado(4)

# Imprimimos o valor retornado pela função
print(f"O quadrado de 4 é: {resultado}")

# Podemos também chamar a função diretamente dentro de um print
print(f"O quadrado de 5 é: {quadrado(5)}")

# Outro exemplo
numero_do_usuario = 10
resultado_usuario = quadrado(numero_do_usuario)
print(f"O quadrado de {numero_do_usuario} é: {resultado_usuario}")
