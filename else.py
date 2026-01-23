# Exemplo de uso do else em uma estrutura condicional if-else em Python
# Definindo duas variáveis para comparação
# Comparando os valores de a e b e usando else para tratar o caso contrário 

a = 10
b = 20

if a > b:
  print("a é maior que b")
else:
  print("a não é maior que b")
  
# Outro exemplo com else em um loop for
# Iterando sobre uma lista e usando else para indicar que o loop terminou
numeros = [1, 2, 3, 4, 5] 
for numero in numeros:
  print(numero)
else:
  print("Fim da lista de números.") 
# Exemplo de uso do else em um loop while
# Contando de 1 a 5 e usando else para indicar que o loop terminou
contador = 1
while contador <= 5:
  print(contador)
  contador += 1
else:
  print("Contagem concluída.")
