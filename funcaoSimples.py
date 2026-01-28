# Em Python, a palavra-chave 'def' é usada para definir ou criar uma função.
# Uma função é um bloco de código que só é executado quando é chamado.

# Definindo funções simples para verificar se um número é par ou ímpar.


def eh_par(numero):
    """
    Verifica se um número é par.
    Retorna True se for par, False caso contrário.
    """
    return numero % 2 == 0

def eh_impar(numero):
    """
    Verifica se um número é ímpar.
    Retorna True se for ímpar, False caso contrário.
    """
    return numero % 2 != 0

def interagir_com_usuario():
    """
    Função principal que interage com o usuário.
    """
    print("--- Verificador de Números Pares e Ímpares ---")

    while True:
        try:
            entrada = input("Digite um número inteiro (ou 'sair' para terminar): ")
            
            if entrada.lower() == 'sair':
                print("Até logo!")
                break

            numero = int(entrada)

            if eh_par(numero):
                print(f"O número {numero} é PAR.")
                # Exemplo de retorno de chamada de função
                resultado_par = eh_par(numero)
                print(f"A função eh_par({numero}) retornou: {resultado_par}\n")

            if eh_impar(numero):
                print(f"O número {numero} é ÍMPAR.")
                # Exemplo de retorno de chamada de função
                resultado_impar = eh_impar(numero)
                print(f"A função eh_impar({numero}) retornou: {resultado_impar}\n")

        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.\n")
        except Exception as e:
            print(f"Ocorreu um erro: {e}\n")


# Ponto de entrada do script
if __name__ == "__main__":
    interagir_com_usuario()
    
    
        # --- Exemplo simples ---
    print("\n--- Teste da segunda função de pesquisa ('pesquisa') ---")
    
    def pesquisa(lista, valor):
        """
        Pesquisa um valor em uma lista e retorna seu índice ou -1 se não encontrado.
        """
        for x, e in enumerate(lista):
            if e == valor:
                return x
        return -1
    
    L = [10, 20, 30, 40, 50]
    
    print(f"Pesquisando na lista: {L}")
    print(f"Resultado da pesquisa por 30: {pesquisa(L, 30)}")
    print(f"Resultado da pesquisa por 60: {pesquisa(L, 60)}")
