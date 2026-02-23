import cv2
from skimage.metrics import structural_similarity as compare_ssim
import matplotlib
matplotlib.use("TkAgg")
from matplotlib import pyplot as plt

# -----------------------------
# Funções de visualização
# -----------------------------
def showSingleImage(img, title, size):
    _, axis = plt.subplots(figsize=size)
    axis.imshow(img, cmap="gray" if len(img.shape) == 2 else None)
    axis.set_title(title, fontdict={"fontsize": 22, "fontweight": "medium"})
    plt.show()

def showMultipleImages(imgsArray, titlesArray, size, x, y):
    if x < 1 or y < 1:
        print("ERRO: X e Y não podem ser zero ou abaixo de zero!")
        return

    def _imshow(ax, im):
        if len(im.shape) == 2:
            ax.imshow(im, cmap="gray")
        else:
            ax.imshow(im)

    if x == 1 and y == 1:
        showSingleImage(imgsArray[0], titlesArray[0], size)
        return

    if x == 1:
        fig, axis = plt.subplots(y, figsize=size)
        for i, im in enumerate(imgsArray):
            _imshow(axis[i], im)
            axis[i].set_anchor("NW")
            axis[i].set_title(titlesArray[i], fontdict={"fontsize": 18, "fontweight": "medium"}, pad=10)
        plt.show()
        return

    if y == 1:
        fig, axis = plt.subplots(1, x, figsize=size)
        for i, im in enumerate(imgsArray):
            _imshow(axis[i], im)
            axis[i].set_anchor("NW")
            axis[i].set_title(titlesArray[i], fontdict={"fontsize": 18, "fontweight": "medium"}, pad=10)
        plt.show()
        return

    fig, axis = plt.subplots(y, x, figsize=size)
    xId, yId, titleId = 0, 0, 0
    for im in imgsArray:
        axis[yId, xId].set_title(
            titlesArray[titleId],
            fontdict={"fontsize": 18, "fontweight": "medium"},
            pad=10,
        )
        axis[yId, xId].set_anchor("NW")
        _imshow(axis[yId, xId], im)

        if len(titlesArray[titleId]) == 0:
            axis[yId, xId].axis("off")

        titleId += 1
        xId += 1
        if xId == x:
            xId = 0
            yId += 1

    plt.show()

# -----------------------------
# Métricas
# -----------------------------
def calculate_psnr(img1, img2):
    return cv2.PSNR(img1, img2)

def calculate_ssim(img1, img2):
    ssim, _ = compare_ssim(img1, img2, full=True)
    return ssim

# -----------------------------
# Programa principal
# -----------------------------
def main():
    path = "data/raw/NORMAL2-IM-0359-0001.jpeg"

    bgr = cv2.imread(path)
    if bgr is None:
        raise FileNotFoundError(f"Não foi possível ler a imagem em: {path}")

    img_rgb = cv2.cvtColor(bgr, cv2.COLOR_BGR2RGB)
    showSingleImage(img_rgb, "Raio-X", (5, 7))

    original_gray = cv2.cvtColor(bgr, cv2.COLOR_BGR2GRAY)

    # Filtro Gaussiano
    gaussian_blur_gray = cv2.GaussianBlur(original_gray, (3, 3), 0)

    imgsArray = [img_rgb, gaussian_blur_gray]
    titlesArray = ["Original (RGB)", "Filtro Gaussiano (Gray)"]
    showMultipleImages(imgsArray, titlesArray, (12, 8), 2, 1)

    # Métricas PSNR e SSIM
    psnr_value = calculate_psnr(original_gray, gaussian_blur_gray)
    ssim_value = calculate_ssim(original_gray, gaussian_blur_gray)

    print(f"PSNR entre as imagens: {psnr_value:.2f} dB")
    print(f"SSIM entre as imagens: {ssim_value:.4f}")

    # -----------------------------
    # Segmentação por limiarização com trackbar
    # -----------------------------
    ESCAPE_KEY_ASCII = 27
    windowTitle = "Ajuste de Limiarizacao"

    # imagem base do threshold
    img_thresh = cv2.resize(gaussian_blur_gray, (700, 700), interpolation=cv2.INTER_AREA)

    # janela redimensionável + tamanho inicial pra aparecer a trackbar
    cv2.namedWindow(windowTitle, cv2.WINDOW_NORMAL)
    cv2.resizeWindow(windowTitle, 800, 900)

    # imagem que será exibida
    copyimg = img_thresh.copy()

    def onChange(th):
        nonlocal copyimg
        _, copyimg = cv2.threshold(img_thresh, th, 255, cv2.THRESH_BINARY)
        cv2.imshow(windowTitle, copyimg)

    cv2.createTrackbar("limiarizacao", windowTitle, 0, 255, onChange)
    onChange(0)

    while True:
        keyPressed = cv2.waitKey(20) & 0xFF
        if keyPressed == ESCAPE_KEY_ASCII:
            break

        try:
            if cv2.getWindowProperty(windowTitle, cv2.WND_PROP_VISIBLE) < 1:
                break
        except cv2.error:
            break

    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()