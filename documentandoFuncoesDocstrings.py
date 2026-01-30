# Em Python, a forma padrão de documentar o código é através de "docstrings".
# Uma docstring é uma string que aparece como a primeira linha da definição
# de uma função, método, classe ou módulo.

def calcular_media(numeros):
  """Calcula a média de uma lista de números.

  Esta função recebe uma lista de valores numéricos, soma todos eles
  e divide pelo total de elementos para encontrar a média.

  Args:
      numeros (list of int or float): Uma lista de números para calcular a média.
          A lista não pode estar vazia.

  Returns:
      float: A média dos números na lista. Retorna 0.0 se a lista for vazia
             para evitar um erro de divisão por zero.
  
  Raises:
      TypeError: Se a lista contiver um elemento que não seja um número.
  """
  if not numeros:
    return 0.0
  
  total = sum(numeros)
  return total / len(numeros)

# --- Como acessar e usar a documentação ---

# 1. Acessando o atributo __doc__
# Isso imprime a docstring exatamente como foi escrita no código.
print("="*50)
print("Acessando a docstring diretamente com o atributo .__doc__:")
print("="*50)
print(calcular_media.__doc__)


# 2. Usando a função interna help()
# O help() formata a docstring para uma leitura mais amigável.
# Pressione 'q' para sair da visualização de ajuda no terminal interativo.
print("\n" + "="*50)
print("Usando a função help() para uma visualização formatada:")
print("="*50)
help(calcular_media)


# Exemplo de uso da função
notas = [8.5, 9.0, 7.5, 10.0]
media_final = calcular_media(notas)
print(f"\nAs notas foram: {notas}")
print(f"A média final é: {media_final}")
