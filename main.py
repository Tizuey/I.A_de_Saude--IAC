import cv2

def process_image(image_path):
    """Processa a imagem capturada aplicando segmentação e máscara."""
    img = cv2.imread(image_path)

    # Verifica se a imagem foi carregada corretamente
    if img is None:
        print("Erro ao carregar a imagem.")
        return

    # Aplica desfoque para reduzir ruído
    blur = cv2.GaussianBlur(img, (3, 3), 0)

    # Converte para HSV e extrair o canal de saturação
    sat = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)[:, :, 1]

    # Binarização do canal de saturação
    thresh = cv2.threshold(sat, 50, 255, cv2.THRESH_BINARY)[1]

    # Aplica operações morfológicas para criar máscara
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
    morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=1)
    mask = cv2.morphologyEx(morph, cv2.MORPH_OPEN, kernel, iterations=1)

    # Converte para escala de cinza e aplicar Otsu
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    otsu = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    # Salva resultados
    cv2.imwrite("assets/mask/mask.png", mask)
    cv2.imwrite("assets/otsu/otsu.png", otsu)

    # Exibe imagens
    cv2.imshow("Original", img)
    cv2.imshow("Máscara", mask)
    cv2.imshow("Resultado final Otsu", otsu)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    image_path = "assets/images/img.png"
    if image_path:
        process_image(image_path)