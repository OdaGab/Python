"""
Programa para calcular a Segunda Lei de Newton: F = m * a

F = Força (Newton - N)
m = massa (quilograma - kg)
a = aceleração (metro por segundo ao quadrado - m/s²)
"""

def calcular_forca(massa, aceleracao):
    """
    Calcula a força usando a fórmula F = m * a
    
    Args:
        massa (float): Massa em quilogramas
        aceleracao (float): Aceleração em m/s²
    
    Returns:
        float: Força em Newtons
    """
    forca = massa * aceleracao
    return forca


def exibir_resultado(massa, aceleracao, forca):
    """
    Exibe o resultado do cálculo de forma formatada
    
    Args:
        massa (float): Massa em kg
        aceleracao (float): Aceleração em m/s²
        forca (float): Força em N
    """
    print("\n" + "="*60)
    print("SEGUNDA LEI DE NEWTON: F = m * a")
    print("="*60)
    print(f"Massa (m):        {massa} kg")
    print(f"Aceleração (a):   {aceleracao} m/s²")
    print(f"Força (F):        {forca} N (Newton)")
    print("="*60 + "\n")


def obter_entrada():
    """
    Obtém a entrada do usuário com validação
    
    Returns:
        tuple: (massa, aceleração) ou None se entrada inválida
    """
    try:
        massa = float(input("Digite a massa (em kg): "))
        aceleracao = float(input("Digite a aceleração (em m/s²): "))
        
        # Validação
        if massa <= 0 or aceleracao < 0:
            print("Erro: Massa deve ser positiva e aceleração não-negativa!")
            return None
        
        return massa, aceleracao
    
    except ValueError:
        print("Erro: Digite valores numéricos válidos!")
        return None


def menu_principal():
    """
    Exibe o menu principal e gerencia as operações
    """
    while True:
        print("\n" + "="*60)
        print("CALCULADORA DA SEGUNDA LEI DE NEWTON")
        print("="*60)
        print("1. Calcular Força (F = m * a)")
        print("2. Calcular Massa (m = F / a)")
        print("3. Calcular Aceleração (a = F / m)")
        print("4. Sair")
        print("="*60)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            dados = obter_entrada()
            if dados:
                massa, aceleracao = dados
                forca = calcular_forca(massa, aceleracao)
                exibir_resultado(massa, aceleracao, forca)
        
        elif opcao == "2":
            try:
                forca = float(input("Digite a força (em N): "))
                aceleracao = float(input("Digite a aceleração (em m/s²): "))
                
                if forca < 0 or aceleracao <= 0:
                    print("Erro: Força não-negativa e aceleração positiva!")
                    continue
                
                massa = forca / aceleracao
                print("\n" + "="*60)
                print("CÁLCULO DE MASSA")
                print("="*60)
                print(f"Força (F):        {forca} N")
                print(f"Aceleração (a):   {aceleracao} m/s²")
                print(f"Massa (m):        {massa} kg")
                print("="*60 + "\n")
            
            except ValueError:
                print("Erro: Digite valores numéricos válidos!")
        
        elif opcao == "3":
            try:
                forca = float(input("Digite a força (em N): "))
                massa = float(input("Digite a massa (em kg): "))
                
                if forca < 0 or massa <= 0:
                    print("Erro: Força não-negativa e massa positiva!")
                    continue
                
                aceleracao = forca / massa
                print("\n" + "="*60)
                print("CÁLCULO DE ACELERAÇÃO")
                print("="*60)
                print(f"Força (F):        {forca} N")
                print(f"Massa (m):        {massa} kg")
                print(f"Aceleração (a):   {aceleracao} m/s²")
                print("="*60 + "\n")
            
            except ValueError:
                print("Erro: Digite valores numéricos válidos!")
        
        elif opcao == "4":
            print("\nAté logo!")
            break
        
        else:
            print("Opção inválida! Digite 1, 2, 3 ou 4.")


# Execução
if __name__ == "__main__":
    menu_principal()
