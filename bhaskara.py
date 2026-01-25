import math

def resolver_bascara(a, b, c):
    """
    Resolve uma equação quadrática usando a fórmula de Bhaskara.
    
    A equação é: ax² + bx + c = 0
    
    Args:
        a: Coeficiente de x²
        b: Coeficiente de x
        c: Termo independente
    
    Returns:
        Tupla com as raízes ou mensagem sobre o resultado
    """
    
    # Verifica se é uma equação quadrática válida
    if a == 0:
        print("Erro: 'a' não pode ser zero. Esta não é uma equação quadrática.")
        return None
    
    # Calcula o discriminante (delta)
    delta = b**2 - 4*a*c
    
    print(f"\nEquação: {a}x² + {b}x + {c} = 0")
    print(f"Delta (Δ) = b² - 4ac = {b}² - 4·{a}·{c} = {delta}")
    
    # Analisa o resultado baseado no discriminante
    if delta < 0:
        print("\nΔ < 0: A equação não possui raízes reais.")
        print("(Possui raízes complexas)")
        return None
    
    elif delta == 0:
        print("\nΔ = 0: A equação possui uma raiz real (raiz dupla).")
        x = -b / (2*a)
        print(f"x = {x}")
        return (x,)
    
    else:  # delta > 0
        print("\nΔ > 0: A equação possui duas raízes reais distintas.")
        
        # Calcula as duas raízes
        sqrt_delta = math.sqrt(delta)
        x1 = (-b + sqrt_delta) / (2*a)
        x2 = (-b - sqrt_delta) / (2*a)
        
        print(f"\nx₁ = (-b + √Δ) / 2a = (-{b} + {sqrt_delta:.4f}) / {2*a} = {x1:.4f}")
        print(f"x₂ = (-b - √Δ) / 2a = (-{b} - {sqrt_delta:.4f}) / {2*a} = {x2:.4f}")
        
        return (x1, x2)


def main():
    """Função principal para interação com o usuário."""
    print("=" * 50)
    print("        RESOLVEDOR DE EQUAÇÃO QUADRÁTICA")
    print("         Fórmula de Bhaskara: ax² + bx + c = 0")
    print("=" * 50)
    
    try:
        # Pede os coeficientes
        a = float(input("\nDigite o coeficiente 'a' (de x²): "))
        b = float(input("Digite o coeficiente 'b' (de x): "))
        c = float(input("Digite o coeficiente 'c' (termo independente): "))
        
        # Resolve a equação
        resultado = resolver_bascara(a, b, c)
        
        if resultado:
            print("\n" + "=" * 50)
            if len(resultado) == 1:
                print(f"Raiz: {resultado[0]:.4f}")
            else:
                print(f"Raízes: x₁ = {resultado[0]:.4f}, x₂ = {resultado[1]:.4f}")
            print("=" * 50)
    
    except ValueError:
        print("\nErro: Digite valores numéricos válidos!")


if __name__ == "__main__":
    main()
