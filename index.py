import cv2
import matplotlib.pyplot as plt

def processar():
    img = cv2.imread('Odair.png')
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    plt.figure(figsize=(5, 4))
    
    # 1. Pegar o gerenciador da janela
    manager = plt.get_current_fig_manager()
    
    # 2. Trocar o Título
    manager.set_window_title('Meu Visualizador de Fotos v1.0')
    
    # 3. Trocar o Ícone (Apenas para Windows/Tkinter)
    # Substitua 'seu_icone.ico' pelo nome do seu arquivo
    try:
        manager.window.iconbitmap('icon.ico')
    except Exception as e:
        print(f"Não foi possível carregar o ícone: {e}")

    plt.imshow(img_rgb)
    plt.axis('off')
    plt.title("Odair Gabriel")
    plt.show()

if __name__ == "__main__":
    processar()