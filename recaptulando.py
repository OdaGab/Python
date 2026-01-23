# 1. Hello
print("--- Bem-vindo ao programa de Recapitulação de Python ---")

# 6. Tipo String e 4. Tipo Numérico
# Declaração de variáveis de diferentes tipos
nome_produto = "Console de Videogame"  # String
preco_unitario = 2999.90  # Float (Numérico)
quantidade_em_estoque = 15  # Integer (Numérico)

print(f"\nProduto: {nome_produto}, Preço: R$ {preco_unitario:.2f}")

# 2. Operações Aritméticas
valor_total_estoque = preco_unitario * quantidade_em_estoque
print(f"Valor total do estoque: R$ {valor_total_estoque:.2f}")

# 3. Operações de Porcentagem
percentual_imposto = 15.0  # 15%
valor_imposto = valor_total_estoque * (percentual_imposto / 100)
print(f"Valor do imposto ({percentual_imposto}%): R$ {valor_imposto:.2f}")

# 7. Escopo de Variáveis
# `variavel_global` pode ser acessada em qualquer lugar do script
variavel_global = "Configuração Padrão da Loja"

def analisar_venda(valor_venda):
    # `mensagem_analise` é uma variável local, só existe dentro desta função
    mensagem_analise = f"Analisando venda de R$ {valor_venda}"
    print(f"\n{mensagem_analise}")
    print(f"Usando a configuração: '{variavel_global}'")


analisar_venda(450.75)
# Tentar acessar `mensagem_analise` aqui fora causaria um erro de escopo.

# 5. Tipo Booleano
tem_desconto_ativo = True
compra_aprovada = False
print(f"\nStatus da Promoção: Desconto Ativo? {tem_desconto_ativo}")

# 8, 9, 10, 11, 12. Estruturas Condicionais e Operadores Lógicos (if, elif, else, and, or, not)
idade_cliente = 25
valor_compra = 500

print("\n--- Análise de Crédito e Desconto ---")
# AND: ambas as condições devem ser verdadeiras
if valor_compra > 300 and idade_cliente > 21:
    print("Cliente elegível para análise de crédito especial.")
    compra_aprovada = True

# OR: pelo menos uma condição deve ser verdadeira
if valor_compra > 1000 or tem_desconto_ativo:
    print("Aplicando desconto automático na compra.")

# ELIF e NOT: verificado se a condição anterior for falsa
elif not compra_aprovada:
    print("Compra não aprovada. Sugerir pagamento à vista.")

# ELSE: executado se nenhuma das condições anteriores (if/elif) for verdadeira
else:
    print("Compra aprovada sem benefícios adicionais.")

# 14. Estrutura IN
# Verifica se um item está dentro de uma sequência (lista)
categorias_validas = ["eletrônicos", "jogos", "acessórios"]
categoria_produto = "jogos"
print(f"\nCategorias válidas: {categorias_validas}")

if categoria_produto in categorias_validas:
    print(f"O produto da categoria '{categoria_produto}' é válido para venda.")
else:
    print(f"Categoria '{categoria_produto}' não encontrada.")

# 13. Estrutura IS
# Compara se duas variáveis são o MESMO objeto na memória
objeto_a = [1, 2, 3]
objeto_b = [1, 2, 3]  # Conteúdo igual, mas objeto diferente
objeto_c = objeto_a   # Aponta para o mesmo objeto

print("\n--- Comparação de Objetos (is vs ==) ---")
print(f"objeto_a == objeto_b (compara valor): {objeto_a == objeto_b}")  # True
print(f"objeto_a is objeto_b (compara identidade): {objeto_a is objeto_b}")  # False
print(f"objeto_a is objeto_c (compara identidade): {objeto_a is objeto_c}")  # True

print("\n--- Fim da recapitulação ---")
