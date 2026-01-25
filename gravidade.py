"""
Programa para calcular Gravidade e Peso

Fórmulas:
1. Peso: P = m * g
2. Lei da Gravitação Universal: F = G * (m1 * m2) / d²

P = Peso (Newton - N)
m = massa (quilograma - kg)
g = aceleração da gravidade (m/s²) ≈ 9.8
G = Constante gravitacional = 6.674 × 10⁻¹¹ N⋅m²/kg²
F = Força gravitacional (Newton - N)
d = Distância entre os centros (metros - m)
"""

# Constantes
G = 6.674e-11  # Constante gravitacional
g_TERRA = 9.8  # Aceleração da gravidade na Terra


def calcular_peso(massa, gravidade=g_TERRA):
    """
    Calcula o peso usando P = m * g
    
    Args:
        massa (float): Massa em kg
        gravidade (float): Aceleração da gravidade em m/s²
    
    Returns:
        float: Peso em Newtons
    """
    peso = massa * gravidade
    return peso


def calcular_massa_por_peso(peso, gravidade=g_TERRA):
    """
    Calcula a massa a partir do peso: m = P / g
    
    Args:
        peso (float): Peso em N
        gravidade (float): Aceleração da gravidade em m/s²
    
    Returns:
        float: Massa em kg
    """
    massa = peso / gravidade
    return massa


def calcular_forca_gravitacional(massa1, massa2, distancia):
    """
    Calcula a força gravitacional usando F = G * (m1 * m2) / d²
    
    Args:
        massa1 (float): Primeira massa em kg
        massa2 (float): Segunda massa em kg
        distancia (float): Distância entre os centros em metros
    
    Returns:
        float: Força gravitacional em Newtons
    """
    forca = G * (massa1 * massa2) / (distancia ** 2)
    return forca


def exibir_resultado_peso(massa, gravidade, peso):
    """
    Exibe o resultado do cálculo de peso
    """
    print("\n" + "="*60)
    print("CÁLCULO DE PESO: P = m * g")
    print("="*60)
    print(f"Massa (m):           {massa} kg")
    print(f"Gravidade (g):       {gravidade} m/s²")
    print(f"Peso (P):            {peso} N (Newton)")
    print("="*60 + "\n")


def exibir_resultado_massa(peso, gravidade, massa):
    """
    Exibe o resultado do cálculo de massa
    """
    print("\n" + "="*60)
    print("CÁLCULO DE MASSA: m = P / g")
    print("="*60)
    print(f"Peso (P):            {peso} N")
    print(f"Gravidade (g):       {gravidade} m/s²")
    print(f"Massa (m):           {massa} kg")
    print("="*60 + "\n")


def exibir_resultado_forca_gravitacional(massa1, massa2, distancia, forca):
    """
    Exibe o resultado da força gravitacional
    """
    print("\n" + "="*60)
    print("CÁLCULO DE FORÇA GRAVITACIONAL: F = G * (m1 * m2) / d²")
    print("="*60)
    print(f"Massa 1 (m1):        {massa1} kg")
    print(f"Massa 2 (m2):        {massa2} kg")
    print(f"Distância (d):       {distancia} m")
    print(f"Constante G:         {G} N⋅m²/kg²")
    print(f"Força (F):           {forca:.6e} N")
    print("="*60 + "\n")


def menu_principal():
    """
    Exibe o menu principal e gerencia as operações
    """
    while True:
        print("\n" + "="*60)
        print("CALCULADORA DE GRAVIDADE")
        print("="*60)
        print("1. Calcular Peso (P = m * g)")
        print("2. Calcular Massa (m = P / g)")
        print("3. Calcular Força Gravitacional (F = G * m1 * m2 / d²)")
        print("4. Informações sobre Gravidade em outros planetas")
        print("5. Sair")
        print("="*60)
        
        opcao = input("Escolha uma opção (1-5): ").strip()
        
        if opcao == "1":
            try:
                massa = float(input("Digite a massa (em kg): "))
                
                print("\nUsar gravidade da Terra (9.8 m/s²)? (s/n): ", end="")
                usar_terra = input().strip().lower()
                
                if usar_terra == "n":
                    gravidade = float(input("Digite a aceleração da gravidade (em m/s²): "))
                else:
                    gravidade = g_TERRA
                
                if massa <= 0 or gravidade <= 0:
                    print("Erro: Valores devem ser positivos!")
                    continue
                
                peso = calcular_peso(massa, gravidade)
                exibir_resultado_peso(massa, gravidade, peso)
            
            except ValueError:
                print("Erro: Digite valores numéricos válidos!")
        
        elif opcao == "2":
            try:
                peso = float(input("Digite o peso (em N): "))
                
                print("\nUsar gravidade da Terra (9.8 m/s²)? (s/n): ", end="")
                usar_terra = input().strip().lower()
                
                if usar_terra == "n":
                    gravidade = float(input("Digite a aceleração da gravidade (em m/s²): "))
                else:
                    gravidade = g_TERRA
                
                if peso < 0 or gravidade <= 0:
                    print("Erro: Peso não-negativo e gravidade positiva!")
                    continue
                
                massa = calcular_massa_por_peso(peso, gravidade)
                exibir_resultado_massa(peso, gravidade, massa)
            
            except ValueError:
                print("Erro: Digite valores numéricos válidos!")
        
        elif opcao == "3":
            try:
                massa1 = float(input("Digite a primeira massa (em kg): "))
                massa2 = float(input("Digite a segunda massa (em kg): "))
                distancia = float(input("Digite a distância entre os centros (em metros): "))
                
                if massa1 <= 0 or massa2 <= 0 or distancia <= 0:
                    print("Erro: Todos os valores devem ser positivos!")
                    continue
                
                forca = calcular_forca_gravitacional(massa1, massa2, distancia)
                exibir_resultado_forca_gravitacional(massa1, massa2, distancia, forca)
            
            except ValueError:
                print("Erro: Digite valores numéricos válidos!")
        
        elif opcao == "4":
            print("\n" + "="*60)
            print("GRAVIDADE EM DIFERENTES PLANETAS (m/s²)")
            print("="*60)
            planetas = {
                "Mercúrio": 3.7,
                "Vênus": 8.87,
                "Terra": 9.8,
                "Marte": 3.71,
                "Júpiter": 24.79,
                "Saturno": 10.44,
                "Urano": 8.87,
                "Netuno": 11.15,
                "Lua": 1.62
            }
            
            for planeta, grav in planetas.items():
                print(f"{planeta:.<20} {grav} m/s²")
            print("="*60 + "\n")
        
        elif opcao == "5":
            print("\nAté logo!")
            break
        
        else:
            print("Opção inválida! Digite 1, 2, 3, 4 ou 5.")


# Execução
if __name__ == "__main__":
    menu_principal()
