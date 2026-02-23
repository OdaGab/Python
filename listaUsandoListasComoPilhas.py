# Usando Listas como Pilhas (LIFO - Last In, First Out)

# Uma pilha é uma estrutura de dados onde o último elemento a entrar
# é o primeiro a sair (LIFO - Last In, First Out)
# Em Python, podemos usar listas para implementar pilhas com append() e pop()

print("="*50)
print("PILHAS COM LISTAS - LIFO (Last In, First Out)")
print("="*50 + "\n")

# 1. Exemplo básico de pilha
print("1. EXEMPLO BÁSICO DE PILHA:\n")

pilha = []
print("Pilha vazia:", pilha)

# Adicionando elementos (empilhando)
pilha.append("Livro 1")
pilha.append("Livro 2")
pilha.append("Livro 3")
pilha.append("Livro 4")
print("Após adicionar 4 livros:", pilha)

# Removendo elementos (desempilhando)
topo = pilha.pop()
print(f"Livro removido do topo: {topo}")
print("Pilha após remover:", pilha)

topo = pilha.pop()
print(f"Livro removido do topo: {topo}")
print("Pilha após remover:", pilha)

print("\n" + "="*50 + "\n")

# 2. Simulação de navegação no browser (histórico)
print("2. SIMULAÇÃO DE HISTÓRICO DE NAVEGAÇÃO:\n")

historico = []

def visitar_pagina(pilha, url):
    pilha.append(url)
    print(f"→ Visitando: {url}")

def voltar_pagina(pilha):
    if len(pilha) > 1:
        pilha.pop()  # Remove página atual
        pagina = pilha[-1]  # Pega a anterior
        print(f"← Voltando para: {pagina}")
        return pagina
    elif len(pilha) == 1:
        print("← Sem histórico anterior")
        return None
    else:
        print("← Histórico vazio")
        return None

# Navegando em páginas
visitar_pagina(historico, "https://google.com")
visitar_pagina(historico, "https://github.com")
visitar_pagina(historico, "https://python.org")
visitar_pagina(historico, "https://stackoverflow.com")

print(f"\nHistórico: {historico}\n")

# Voltando páginas
voltar_pagina(historico)
print(f"Histórico: {historico}\n")

voltar_pagina(historico)
print(f"Histórico: {historico}\n")

voltar_pagina(historico)
print(f"Histórico: {historico}\n")

voltar_pagina(historico)

print("\n" + "="*50 + "\n")

# 3. Verificando o elemento do topo sem remover
print("3. OPERAÇÕES COM PILHA:\n")

pratos = []

def empilhar_prato(pilha, cor):
    pilha.append(cor)
    print(f"+ Prato {cor} adicionado")

def desempilhar_prato(pilha):
    if len(pilha) > 0:
        prato = pilha.pop()
        print(f"- Prato {prato} removido")
        return prato
    else:
        print("- Nenhum prato na pilha!")
        return None

def topo_pilha(pilha):
    if len(pilha) > 0:
        return pilha[-1]
    else:
        return None

def pilha_vazia(pilha):
    return len(pilha) == 0

# Operações
empilhar_prato(pratos, "Branco")
empilhar_prato(pratos, "Azul")
empilhar_prato(pratos, "Vermelho")

print(f"Prato no topo: {topo_pilha(pratos)}")
print(f"Total de pratos: {len(pratos)}")
print(f"Pilha vazia? {pilha_vazia(pratos)}")

print()
desempilhar_prato(pratos)
print(f"Prato no topo agora: {topo_pilha(pratos)}")

print()
desempilhar_prato(pratos)
desempilhar_prato(pratos)
print(f"Pilha vazia agora? {pilha_vazia(pratos)}")

print("\n" + "="*50 + "\n")

# 4. Inverter uma string usando pilha
print("4. INVERTENDO TEXTO COM PILHA:\n")

def inverter_string(texto):
    pilha = []
    
    # Empilha cada caractere
    for caractere in texto:
        pilha.append(caractere)
    
    # Desempilha para inverter
    invertido = ""
    while len(pilha) > 0:
        invertido += pilha.pop()
    
    return invertido

texto_original = "Python"
texto_invertido = inverter_string(texto_original)

print(f"Texto original: {texto_original}")
print(f"Texto invertido: {texto_invertido}")

print()

texto_original2 = "Hello World"
texto_invertido2 = inverter_string(texto_original2)

print(f"Texto original: {texto_original2}")
print(f"Texto invertido: {texto_invertido2}")

print("\n" + "="*50 + "\n")

# 5. Verificar parênteses balanceados
print("5. VERIFICAR PARÊNTESES BALANCEADOS:\n")

def parenteses_balanceados(expressao):
    pilha = []
    pares = {'(': ')', '[': ']', '{': '}'}
    
    for caractere in expressao:
        if caractere in pares:  # Abre
            pilha.append(caractere)
        elif caractere in pares.values():  # Fecha
            if len(pilha) == 0:
                return False
            abre = pilha.pop()
            if pares[abre] != caractere:
                return False
    
    return len(pilha) == 0

expressoes = [
    "((a + b) * c)",
    "([{a}])",
    "((a + b)",
    "([)]",
    "{a + [b * (c / d)]}",
]

for expr in expressoes:
    resultado = parenteses_balanceados(expr)
    status = "✓ Balanceado" if resultado else "✗ Não balanceado"
    print(f"{expr:20} -> {status}")

print("\n" + "="*50 + "\n")

# 6. Desfazer (Undo) / Refazer (Redo)
print("6. SISTEMA DE DESFAZER/REFAZER:\n")

class EditorTexto:
    def __init__(self):
        self.historico_desfazer = []
        self.historico_refazer = []
        self.texto = ""
    
    def adicionar_texto(self, texto):
        self.historico_desfazer.append(self.texto)
        self.texto += texto
        self.historico_refazer = []  # Limpa redo
        print(f"+ Texto adicionado: '{self.texto}'")
    
    def desfazer(self):
        if len(self.historico_desfazer) > 0:
            self.historico_refazer.append(self.texto)
            self.texto = self.historico_desfazer.pop()
            print(f"← Desfeito: '{self.texto}'")
        else:
            print("← Nada para desfazer")
    
    def refazer(self):
        if len(self.historico_refazer) > 0:
            self.historico_desfazer.append(self.texto)
            self.texto = self.historico_refazer.pop()
            print(f"→ Refeito: '{self.texto}'")
        else:
            print("→ Nada para refazer")
    
    def mostrar_texto(self):
        print(f"Texto atual: '{self.texto}'")

editor = EditorTexto()

editor.adicionar_texto("Hello")
editor.adicionar_texto(" World")
editor.mostrar_texto()
print()

editor.desfazer()
editor.mostrar_texto()
print()

editor.refazer()
editor.mostrar_texto()
print()

editor.adicionar_texto("!")
editor.mostrar_texto()

print("\n" + "="*50 + "\n")

# 7. Comparação: PILHA vs FILA
print("7. COMPARAÇÃO: PILHA (Stack) vs FILA (Queue):\n")

print("PILHA (Stack) - LIFO:")
print("  - Último a entrar, primeiro a sair")
print("  - Usa append() e pop()")
print("  - Exemplos: histórico, undo/redo, navegação\n")

print("FILA (Queue) - FIFO:")
print("  - Primeiro a entrar, primeiro a sair")
print("  - Usa append() e pop(0)")
print("  - Exemplos: fila de atendimento, processamento de tarefas\n")

print("Visual:")
print("\nPilha (Stack):        Fila (Queue):")
print("  [4]                   [1] [2] [3] [4]")
print("  [3]                   ")
print("  [2]                   Remove primeiro")
print("  [1]                   ")
print("Remove último")

print("\n" + "="*50 + "\n")

# 8. Converter para decimal usando pilha
print("8. CONVERTER NÚMERO BINÁRIO PARA DECIMAL:\n")

def binario_para_decimal(binario_str):
    pilha = []
    potencia = 0
    
    # Coloca cada dígito na pilha
    for digito in binario_str:
        pilha.append(int(digito))
    
    # Remove da pilha (de trás para frente) e calcula
    decimal = 0
    while len(pilha) > 0:
        digito = pilha.pop()
        decimal += digito * (2 ** potencia)
        potencia += 1
    
    return decimal

binarios = ["101", "1010", "11111", "10000"]

for bin_num in binarios:
    decimal = binario_para_decimal(bin_num)
    print(f"{bin_num} (binário) = {decimal} (decimal)")
