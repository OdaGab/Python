# Função para calcular o fatorial de um número


def fatorial(n):
     
     fat = 1
     
     while n > 1:
         fat *= n
         n -= 1
     return fat
# Exemplo de uso da função
if __name__ == "__main__":
    numero = 5
    print(f"O fatorial de {numero} é {fatorial(numero)}")
    
#--- Exemplo simples ---
    print("\n--- Teste da função fatorial ---")
    for i in range(6):
        print(f"O fatorial de {i} é {fatorial(i)}")
        
#--- Exemplo com entrada do usuário ---
    print("\n--- Cálculo do fatorial com entrada do usuário ---")
    try:
        entrada = int(input("Digite um número inteiro não negativo para calcular o fatorial: "))
        if entrada < 0:
            print("Por favor, digite um número não negativo.")
        else:
            print(f"O fatorial de {entrada} é {fatorial(entrada)}")
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro válido.")
        
#--- Exemplo com chamadas de função ---
    print("\n--- Teste da função fatorial com chamadas de função ---")  
    def calcula_e_exibe_fatorial(num):
        resultado = fatorial(num)
        print(f"O fatorial de {num} é {resultado}")     
    for j in range(4, 8):
        calcula_e_exibe_fatorial(j) 
        
        