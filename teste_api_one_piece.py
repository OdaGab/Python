# teste_api_one_piece.py
# Script para testar a API de One Piece e buscar informações de um personagem específico

# Importa a biblioteca 'requests' para fazer requisições HTTP
import requests
# Importa a biblioteca 'json' para formatar a saída
import json

# URL da API para buscar informações de um personagem específico (neste caso, o ID 1, que é o Luffy)
url = "https://api.api-onepiece.com/v2/characters/en/1"

print(f"Buscando dados em: {url}\n")

try:
    # Faz a requisição GET para a URL
    response = requests.get(url)

    # Verifica se a requisição foi bem-sucedida (código de status 200)
    if response.status_code == 200:
        # Pega os dados da resposta em formato JSON
        dados = response.json()
        
        # Imprime os dados formatados de uma maneira mais legível
        print("Dados recebidos com sucesso:")
        print(json.dumps(dados, indent=4, ensure_ascii=False))
        
    else:
        # Se a requisição falhou, informa o código do erro
        print(f"Erro ao buscar dados. Código de status: {response.status_code}")

except requests.exceptions.RequestException as e:
    # Captura possíveis erros de conexão com a internet
    print(f"Ocorreu um erro de conexão: {e}")
    print("Verifique se a biblioteca 'requests' está instalada. Você pode instalar com o comando: pip install requests")

except json.JSONDecodeError:
    # Captura erros se a resposta não for um JSON válido
    print("Erro: A resposta recebida não é um JSON válido.")
