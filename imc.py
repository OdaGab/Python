"""
Programa para calcular o Índice de Massa Corporal (IMC)

Fórmula: IMC = peso (kg) / altura² (m)

Classificação:
- Abaixo de 18,5: Abaixo do peso
- 18,5 a 24,9: Peso normal
- 25,0 a 29,9: Sobrepeso
- 30,0 a 34,9: Obesidade grau I
- 35,0 a 39,9: Obesidade grau II
- 40,0 ou mais: Obesidade grau III (mórbida)
"""

def calcular_imc(peso, altura):
    """
    Calcula o IMC usando a fórmula: IMC = peso / altura²
    
    Args:
        peso (float): Peso em quilogramas
        altura (float): Altura em metros
    
    Returns:
        float: Valor do IMC
    """
    imc = peso / (altura ** 2)
    return imc


def classificar_imc(imc):
    """
    Classifica o IMC de acordo com a tabela da OMS
    
    Args:
        imc (float): Valor do IMC
    
    Returns:
        tuple: (classificação, cor, recomendação)
    """
    if imc < 18.5:
        return "Abaixo do peso", "🔵", "Procure aumentar a ingestão calórica de forma saudável"
    elif 18.5 <= imc < 25:
        return "Peso normal", "🟢", "Parabéns! Mantenha seus hábitos saudáveis"
    elif 25 <= imc < 30:
        return "Sobrepeso", "🟡", "Recomenda-se aumentar a atividade física"
    elif 30 <= imc < 35:
        return "Obesidade grau I", "🟠", "Consulte um médico ou nutricionista"
    elif 35 <= imc < 40:
        return "Obesidade grau II", "🔴", "Acompanhamento médico é essencial"
    else:
        return "Obesidade grau III (Mórbida)", "⚫", "Procure imediatamente um profissional de saúde"


def exibir_resultado(peso, altura, imc, classificacao, cor, recomendacao):
    """
    Exibe o resultado do cálculo de IMC de forma formatada
    """
    print("\n" + "="*70)
    print("RESULTADO DO CÁLCULO DE IMC")
    print("="*70)
    print(f"Peso:                {peso} kg")
    print(f"Altura:              {altura} m")
    print(f"IMC:                 {imc:.2f} kg/m²")
    print("="*70)
    print(f"{cor} Classificação:     {classificacao}")
    print("="*70)
    print(f"💡 Recomendação:      {recomendacao}")
    print("="*70 + "\n")


def obter_dados_usuario():
    """
    Obtém peso e altura do usuário com validação
    
    Returns:
        tuple: (peso, altura) ou None se entrada inválida
    """
    try:
        peso = float(input("Digite o peso (em kg): "))
        altura = float(input("Digite a altura (em metros, ex: 1.75): "))
        
        # Validação
        if peso <= 0 or altura <= 0:
            print("Erro: Peso e altura devem ser valores positivos!")
            return None
        
        if altura > 3:
            print("Erro: Altura muito alta! Verifique se digitou em metros (ex: 1.75)")
            return None
        
        return peso, altura
    
    except ValueError:
        print("Erro: Digite valores numéricos válidos!")
        return None


def exibir_tabela_imc():
    """
    Exibe a tabela de classificação de IMC
    """
    print("\n" + "="*70)
    print("TABELA DE CLASSIFICAÇÃO DE IMC (OMS)")
    print("="*70)
    print(f"{'Classificação':<30} {'IMC':<20}")
    print("-"*70)
    print(f"{'Abaixo do peso':<30} {'Menor que 18,5':<20}")
    print(f"{'Peso normal':<30} {'18,5 a 24,9':<20}")
    print(f"{'Sobrepeso':<30} {'25,0 a 29,9':<20}")
    print(f"{'Obesidade grau I':<30} {'30,0 a 34,9':<20}")
    print(f"{'Obesidade grau II':<30} {'35,0 a 39,9':<20}")
    print(f"{'Obesidade grau III (Mórbida)':<30} {'40,0 ou mais':<20}")
    print("="*70 + "\n")


def calcular_peso_ideal(altura, imc_minimo=18.5, imc_maximo=24.9):
    """
    Calcula o peso ideal baseado na altura
    
    Args:
        altura (float): Altura em metros
        imc_minimo (float): IMC mínimo desejado
        imc_maximo (float): IMC máximo desejado
    
    Returns:
        tuple: (peso_mínimo, peso_máximo)
    """
    peso_minimo = imc_minimo * (altura ** 2)
    peso_maximo = imc_maximo * (altura ** 2)
    return peso_minimo, peso_maximo


def exibir_peso_ideal(altura, peso_minimo, peso_maximo):
    """
    Exibe o peso ideal para a altura
    """
    print("\n" + "="*70)
    print("PESO IDEAL PARA SUA ALTURA")
    print("="*70)
    print(f"Altura:              {altura} m")
    print(f"Peso mínimo:         {peso_minimo:.2f} kg")
    print(f"Peso máximo:         {peso_maximo:.2f} kg")
    print(f"Intervalo ideal:     {peso_minimo:.2f} kg a {peso_maximo:.2f} kg")
    print("="*70 + "\n")


def menu_principal():
    """
    Exibe o menu principal e gerencia as operações
    """
    while True:
        print("\n" + "="*70)
        print("CALCULADORA DE ÍNDICE DE MASSA CORPORAL (IMC)")
        print("="*70)
        print("1. Calcular IMC")
        print("2. Ver tabela de classificação")
        print("3. Calcular peso ideal por altura")
        print("4. Sair")
        print("="*70)
        
        opcao = input("Escolha uma opção (1-4): ").strip()
        
        if opcao == "1":
            print("\n--- CÁLCULO DE IMC ---")
            dados = obter_dados_usuario()
            
            if dados:
                peso, altura = dados
                imc = calcular_imc(peso, altura)
                classificacao, cor, recomendacao = classificar_imc(imc)
                
                exibir_resultado(peso, altura, imc, classificacao, cor, recomendacao)
        
        elif opcao == "2":
            exibir_tabela_imc()
        
        elif opcao == "3":
            try:
                altura = float(input("Digite sua altura (em metros, ex: 1.75): "))
                
                if altura <= 0 or altura > 3:
                    print("Erro: Altura inválida!")
                    continue
                
                peso_min, peso_max = calcular_peso_ideal(altura)
                exibir_peso_ideal(altura, peso_min, peso_max)
            
            except ValueError:
                print("Erro: Digite um valor numérico válido!")
        
        elif opcao == "4":
            print("\nAté logo! Mantenha-se saudável! 💪")
            break
        
        else:
            print("Opção inválida! Digite 1, 2, 3 ou 4.")


# Execução
if __name__ == "__main__":
    menu_principal()
