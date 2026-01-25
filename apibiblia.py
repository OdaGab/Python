"""
Programa para buscar versículos da Bíblia em português usando API

API utilizada: bible-api.com (suporta português com tradução)
Retorna versículos em português de forma confiável
"""

import requests


def buscar_versiculo(livro, capitulo, versiculo):
    """
    Busca um versículo na Bible API
    
    Args:
        livro (str): Nome do livro (ex: João, Salmos, Mateus)
        capitulo (int): Número do capítulo
        versiculo (str): Número do versículo ou range (ex: 16 ou 1-5)
    
    Returns:
        dict: Dados do versículo ou None se não encontrado
    """
    try:
        # Monta a referência no formato esperado pela API
        referencia = f"{livro}%20{capitulo}:{versiculo}"
        
        # URL da API bible-api.com
        url = f"https://bible-api.com/{referencia}?translation=almeida"
        
        print(f"\n🔍 Buscando: {livro} {capitulo}:{versiculo}...")
        print(f"📡 URL: {url}")
        
        # Faz a requisição com timeout
        resposta = requests.get(url, timeout=10)
        
        # Verifica status HTTP
        if resposta.status_code == 404:
            print(f"❌ Versículo '{livro} {capitulo}:{versiculo}' não encontrado.")
            return None
        
        resposta.raise_for_status()
        dados = resposta.json()
        
        # Verifica se há erro na resposta
        if "error" in dados:
            print(f"❌ Erro da API: {dados['error']}")
            return None
        
        # Formata o resultado
        if "text" in dados and "reference" in dados:
            return {
                "referencia": dados.get("reference", "Desconhecido"),
                "texto": dados.get("text", "Texto não disponível")
            }
        
        return dados
    
    except requests.exceptions.Timeout:
        print(f"❌ Timeout: API levou muito tempo para responder")
        return None
    except requests.exceptions.ConnectionError:
        print(f"❌ Erro de conexão: Verifique sua internet")
        return None
    except requests.exceptions.HTTPError as e:
        print(f"❌ Erro HTTP: {e.response.status_code}")
        return None
    except Exception as e:
        print(f"❌ Erro ao buscar versículo: {e}")
        return None


def exibir_versiculo(dados):
    """
    Exibe o versículo de forma formatada
    
    Args:
        dados (dict): Dados do versículo retornados
    """
    if dados:
        print("\n" + "="*70)
        print(f"📖 {dados['referencia']}")
        print("="*70)
        print(f"\n{dados['texto']}\n")
        print("="*70 + "\n")


def exibir_passagem_completa(dados):
    """
    Exibe uma passagem completa (vários versículos)
    
    Args:
        dados (dict): Dados dos versículos
    """
    if dados:
        print("\n" + "="*70)
        print(f"📖 {dados['referencia']}")
        print("="*70)
        print(f"\n{dados['texto']}\n")
        print("="*70 + "\n")


def menu_principal():
    """
    Exibe o menu principal e gerencia as operações
    """
    while True:
        print("\n" + "="*70)
        print("BUSCADOR DE VERSÍCULOS DA BÍBLIA 📖")
        print("="*70)
        print("1. Buscar um versículo")
        print("2. Buscar uma sequência de versículos")
        print("3. Exemplos de buscas")
        print("4. Sair")
        print("="*70)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            livro = input("Digite o livro (em português ou inglês, ex: João, Salmos, Matthew): ").strip()
            
            try:
                capitulo = int(input("Digite o capítulo: "))
                versiculo = input("Digite o versículo (número): ")
                
                if not livro or capitulo <= 0 or not versiculo:
                    print("Erro: Verifique os valores digitados!")
                    continue
                
                dados = buscar_versiculo(livro, capitulo, versiculo)
                exibir_versiculo(dados)
            
            except ValueError:
                print("Erro: Capítulo deve ser um número!")
        
        elif opcao == "2":
            livro = input("Digite o livro (em português ou inglês, ex: João, Genesis): ").strip()
            
            try:
                capitulo = int(input("Digite o capítulo: "))
                inicio = int(input("Digite o versículo inicial: "))
                fim = int(input("Digite o versículo final: "))
                
                if not livro or capitulo <= 0 or inicio <= 0 or fim <= 0:
                    print("Erro: Verifique os valores digitados!")
                    continue
                
                if inicio > fim:
                    print("Erro: Versículo inicial deve ser menor que final!")
                    continue
                
                versiculo = f"{inicio}-{fim}"
                dados = buscar_versiculo(livro, capitulo, versiculo)
                exibir_passagem_completa(dados)
            
            except ValueError:
                print("Erro: Digite valores numéricos válidos!")
        
        elif opcao == "3":
            exibir_exemplos()
        
        elif opcao == "4":
            print("\nQue Deus te abençoe! Até logo! 🙏")
            break
        
        else:
            print("Opção inválida! Digite 1, 2, 3 ou 4.")


def exibir_exemplos():
    """
    Exibe exemplos de buscas e faz algumas automaticamente
    """
    print("\n" + "="*70)
    print("EXEMPLOS DE BUSCAS POPULARES 📖")
    print("="*70)
    
    exemplos = [
        ("João", 3, "16", "Versículo mais famoso da Bíblia"),
        ("Gênesis", 1, "1", "Primeiro versículo da Bíblia"),
        ("Salmos", 23, "1", "Salmo 23 - O Senhor é meu Pastor"),
        ("Mateus", 6, "9", "Oração do Pai Nosso"),
        ("1 João", 4, "7", "Deus é Amor"),
    ]
    
    print("\nExemplos disponíveis:\n")
    for i, (livro, cap, vers, descricao) in enumerate(exemplos, 1):
        print(f"{i}. {livro} {cap}:{vers} - {descricao}")
    
    print("\n6. Ver lista de todos os versículos disponíveis")
    print("7. Voltar ao menu")
    
    try:
        escolha = int(input("\nEscolha um exemplo (1-7): "))
        
        if escolha == 6:
            exibir_lista_versiculos()
        elif escolha == 7:
            return
        elif 1 <= escolha <= 5:
            livro, cap, vers, descricao = exemplos[escolha - 1]
            print(f"\n💡 {descricao}")
            dados = buscar_versiculo(livro, cap, vers)
            exibir_versiculo(dados)
        else:
            print("Opção inválida!")
    
    except ValueError:
        print("Erro: Digite um número válido!")


def exibir_lista_versiculos():
    """
    Exibe todos os versículos disponíveis na base de dados
    """
    print("\n" + "="*70)
    print("VERSÍCULOS DISPONÍVEIS NA BASE DE DADOS")
    print("="*70 + "\n")
    
    for chave, dados in sorted(BIBLIA_PORTUGUES.items()):
        print(f"• {dados['referencia']}")
    
    print("\n" + "="*70 + "\n")


# Execução
if __name__ == "__main__":
    print("\n" + "="*70)
    print("BEM-VINDO AO BUSCADOR DE VERSÍCULOS DA BÍBLIA! 📖")
    print("="*70)
    print("\nEste programa se conecta com a BibleAPI para buscar versículos")
    print("em português (Tradução Nova - Almeida Revisada)\n")
    
    menu_principal()
