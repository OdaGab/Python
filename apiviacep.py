import requests
import json

## Usar o caminho abaixo para rodar o script no terminal
## /Users/usuario/Desktop/Python/.venv/bin/python apiviacep.py

def buscar_endereco_por_cep(cep):
    """
    Busca informações de endereço usando a API ViaCEP
    
    Args:
        cep (str): O CEP a ser consultado (com ou sem hífen)
    
    Returns:
        dict: Dicionário com os dados do endereço
    """
    
    # Remove caracteres especiais do CEP
    cep_limpo = cep.replace("-", "").replace(" ", "")
    
    # Valida se o CEP tem 8 dígitos
    if len(cep_limpo) != 8 or not cep_limpo.isdigit():
        print(f"Erro: CEP inválido! Use o formato: 12345-678")
        return None
    
    try:
        # URL da API ViaCEP
        url = f"https://viacep.com.br/ws/{cep_limpo}/json/"
        
        # Faz a requisição
        resposta = requests.get(url)
        resposta.raise_for_status()  # Levanta exceção se houver erro HTTP
        
        # Converte para dicionário
        dados = resposta.json()
        
        # Verifica se o CEP foi encontrado
        if "erro" in dados:
            print(f"Erro: CEP {cep_limpo} não encontrado!")
            return None
        
        return dados
    
    except requests.exceptions.RequestException as e:
        print(f"Erro ao conectar com a API: {e}")
        return None


def exibir_endereco(dados):
    """
    Exibe os dados do endereço de forma formatada
    
    Args:
        dados (dict): Dicionário com os dados do endereço
    """
    if dados:
        print("\n" + "="*50)
        print(f"CEP: {dados['cep']}")
        print(f"Endereço: {dados['logradouro']}")
        print(f"Complemento: {dados['complemento']}")
        print(f"Bairro: {dados['bairro']}")
        print(f"Cidade: {dados['localidade']}")
        print(f"Estado: {dados['uf']}")
        print(f"IBGE: {dados['ibge']}")
        print(f"GIA: {dados['gia']}")
        print(f"DDD: {dados['ddd']}")
        print(f"SIAFI: {dados['siafi']}")
        print("="*50 + "\n")


# Exemplo de uso
if __name__ == "__main__":
    # Teste com um CEP
    cep_busca = input("Digite o CEP (ex: 01310-100): ")
    
    resultado = buscar_endereco_por_cep(cep_busca)
    exibir_endereco(resultado)
