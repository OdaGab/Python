"""
Programa para calcular a Área de um Triângulo

Fórmulas:
1. Usando base e altura: A = (base × altura) / 2
2. Fórmula de Heron: A = √(s(s-a)(s-b)(s-c)), onde s = (a+b+c)/2
3. Usando as coordenadas dos vértices: A = |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2
"""

import math


def calcular_area_base_altura(base, altura):
    """
    Calcula a área do triângulo usando base e altura
    A = (base × altura) / 2
    
    Args:
        base (float): Base do triângulo
        altura (float): Altura do triângulo
    
    Returns:
        float: Área do triângulo
    """
    area = (base * altura) / 2
    return area


def calcular_area_heron(lado1, lado2, lado3):
    """
    Calcula a área usando a Fórmula de Heron
    A = √(s(s-a)(s-b)(s-c)), onde s = (a+b+c)/2
    
    Args:
        lado1, lado2, lado3 (float): Comprimento dos três lados
    
    Returns:
        float: Área do triângulo ou None se inválido
    """
    # Verifica se os lados formam um triângulo válido
    if not validar_triangulo(lado1, lado2, lado3):
        return None
    
    # Calcula o semi-perímetro
    s = (lado1 + lado2 + lado3) / 2
    
    # Aplica a fórmula de Heron
    area = math.sqrt(s * (s - lado1) * (s - lado2) * (s - lado3))
    return area


def calcular_area_coordenadas(x1, y1, x2, y2, x3, y3):
    """
    Calcula a área usando as coordenadas dos vértices
    A = |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2
    
    Args:
        x1, y1, x2, y2, x3, y3 (float): Coordenadas dos três vértices
    
    Returns:
        float: Área do triângulo
    """
    area = abs((x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2)
    return area


def validar_triangulo(lado1, lado2, lado3):
    """
    Valida se os três lados formam um triângulo válido
    
    Args:
        lado1, lado2, lado3 (float): Comprimento dos lados
    
    Returns:
        bool: True se forma um triângulo válido
    """
    # A soma de dois lados deve ser maior que o terceiro lado
    if (lado1 + lado2 > lado3 and 
        lado1 + lado3 > lado2 and 
        lado2 + lado3 > lado1):
        return True
    return False


def calcular_perimetro(lado1, lado2, lado3):
    """
    Calcula o perímetro do triângulo
    
    Args:
        lado1, lado2, lado3 (float): Comprimento dos lados
    
    Returns:
        float: Perímetro
    """
    return lado1 + lado2 + lado3


def exibir_resultado_base_altura(base, altura, area):
    """
    Exibe o resultado usando base e altura
    """
    print("\n" + "="*70)
    print("ÁREA DO TRIÂNGULO - MÉTODO: BASE E ALTURA")
    print("="*70)
    print(f"Base (b):            {base} unidades")
    print(f"Altura (h):          {altura} unidades")
    print(f"Fórmula:             A = (base × altura) / 2")
    print(f"Cálculo:             A = ({base} × {altura}) / 2")
    print(f"Área:                {area:.2f} unidades²")
    print("="*70 + "\n")


def exibir_resultado_heron(lado1, lado2, lado3, area):
    """
    Exibe o resultado usando a fórmula de Heron
    """
    s = (lado1 + lado2 + lado3) / 2
    perimetro = calcular_perimetro(lado1, lado2, lado3)
    
    print("\n" + "="*70)
    print("ÁREA DO TRIÂNGULO - MÉTODO: FÓRMULA DE HERON")
    print("="*70)
    print(f"Lado 1 (a):          {lado1} unidades")
    print(f"Lado 2 (b):          {lado2} unidades")
    print(f"Lado 3 (c):          {lado3} unidades")
    print(f"Perímetro:           {perimetro:.2f} unidades")
    print(f"Semi-perímetro (s):  {s:.2f} unidades")
    print(f"Fórmula:             A = √(s(s-a)(s-b)(s-c))")
    print(f"Cálculo:             A = √({s:.2f} × {s-lado1:.2f} × {s-lado2:.2f} × {s-lado3:.2f})")
    print(f"Área:                {area:.2f} unidades²")
    print("="*70 + "\n")


def exibir_resultado_coordenadas(x1, y1, x2, y2, x3, y3, area):
    """
    Exibe o resultado usando coordenadas
    """
    print("\n" + "="*70)
    print("ÁREA DO TRIÂNGULO - MÉTODO: COORDENADAS DOS VÉRTICES")
    print("="*70)
    print(f"Vértice 1:           ({x1}, {y1})")
    print(f"Vértice 2:           ({x2}, {y2})")
    print(f"Vértice 3:           ({x3}, {y3})")
    print(f"Fórmula:             A = |x1(y2-y3) + x2(y3-y1) + x3(y1-y2)| / 2")
    print(f"Área:                {area:.2f} unidades²")
    print("="*70 + "\n")


def menu_principal():
    """
    Exibe o menu principal e gerencia as operações
    """
    while True:
        print("\n" + "="*70)
        print("CALCULADORA DE ÁREA DE TRIÂNGULO")
        print("="*70)
        print("1. Calcular usando Base e Altura")
        print("2. Calcular usando a Fórmula de Heron (3 lados)")
        print("3. Calcular usando Coordenadas dos Vértices")
        print("4. Sair")
        print("="*70)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            try:
                base = float(input("Digite a base do triângulo: "))
                altura = float(input("Digite a altura do triângulo: "))
                
                if base <= 0 or altura <= 0:
                    print("Erro: Base e altura devem ser positivas!")
                    continue
                
                area = calcular_area_base_altura(base, altura)
                exibir_resultado_base_altura(base, altura, area)
            
            except ValueError:
                print("Erro: Digite valores numéricos válidos!")
        
        elif opcao == "2":
            try:
                print("\nDigite os comprimentos dos três lados:")
                lado1 = float(input("Lado 1: "))
                lado2 = float(input("Lado 2: "))
                lado3 = float(input("Lado 3: "))
                
                if lado1 <= 0 or lado2 <= 0 or lado3 <= 0:
                    print("Erro: Todos os lados devem ser positivos!")
                    continue
                
                if not validar_triangulo(lado1, lado2, lado3):
                    print(f"Erro: Os valores {lado1}, {lado2}, {lado3} não formam um triângulo válido!")
                    print(f"A soma de dois lados deve ser maior que o terceiro lado.")
                    continue
                
                area = calcular_area_heron(lado1, lado2, lado3)
                exibir_resultado_heron(lado1, lado2, lado3, area)
            
            except ValueError:
                print("Erro: Digite valores numéricos válidos!")
        
        elif opcao == "3":
            try:
                print("\nDigite as coordenadas dos três vértices:")
                print("Vértice 1:")
                x1 = float(input("  x1: "))
                y1 = float(input("  y1: "))
                
                print("Vértice 2:")
                x2 = float(input("  x2: "))
                y2 = float(input("  y2: "))
                
                print("Vértice 3:")
                x3 = float(input("  x3: "))
                y3 = float(input("  y3: "))
                
                # Verifica se os pontos formam um triângulo válido
                area = calcular_area_coordenadas(x1, y1, x2, y2, x3, y3)
                
                if area == 0:
                    print("Erro: Os três pontos são colineares (não formam um triângulo)!")
                    continue
                
                exibir_resultado_coordenadas(x1, y1, x2, y2, x3, y3, area)
            
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
