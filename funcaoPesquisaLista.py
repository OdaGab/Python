def pesquisar_elemento(lista, elemento_procurado):
    """
    Pesquisa por um elemento em uma lista e retorna seu índice se encontrado.
    
    Args:
        lista (list): A lista na qual a pesquisa será feita.
        elemento_procurado: O item a ser procurado na lista.
        
    Returns:
        int: O índice do elemento se ele for encontrado.
        None: Se o elemento não for encontrado na lista.
    """
    try:
        # O método index() já faz a pesquisa e retorna o índice.
        # Se o elemento não estiver na lista, ele levanta uma exceção ValueError.
        indice = lista.index(elemento_procurado)
        return indice
    except ValueError:
        # Capturamos a exceção para significar que o item não foi encontrado.
        return None

def interagir_com_usuario():
    """
    Função principal que gerencia a interação com o usuário.
    """
    # Lista de exemplo para a pesquisa
    frutas = ["maçã", "banana", "uva", "morango", "laranja", "abacaxi"]
    
    print("--- Pesquisa em Lista ---")
    print("Vamos pesquisar na seguinte lista de frutas:")
    print(frutas)
    print("-" * 25)

    while True:
        item_desejado = input("Qual fruta você quer pesquisar? (ou 'sair' para terminar): ").lower()

        if item_desejado == 'sair':
            print("Até a próxima!")
            break
            
        # Chamamos nossa função de pesquisa
        resultado = pesquisar_elemento(frutas, item_desejado)

        if resultado is not None:
            # Se o resultado não for None, o item foi encontrado
            print(f"Ótimo! A fruta '{item_desejado}' foi encontrada na posição {resultado}.")
        else:
            # Se o resultado for None, o item não foi encontrado
            print(f"Que pena! A fruta '{item_desejado}' não está na lista.")
        
        print() # Adiciona uma linha em branco para melhor legibilidade

# Ponto de entrada do script
if __name__ == "__main__":
    interagir_com_usuario()