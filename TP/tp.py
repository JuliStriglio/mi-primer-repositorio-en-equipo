import cv2
import numpy as np

# Cargar imagen del muñeco
muñeco = cv2.imread('C:/Users/Juli/Documents/UTN2024/Soporte/TP/image2.webp', cv2.IMREAD_UNCHANGED)

# Cargar imagen de fondo
fondo = cv2.imread('C:/Users/Juli/Documents/UTN2024/Soporte/TP/image1.jpg')

# Redimensionar el fondo para que se ajuste a la ventana
window_height, window_width = 720, 1280
fondo = cv2.resize(fondo, (window_width, window_height))

# Superponer imagen
def overlay_image(background, overlay, x, y):
    """ Superpone una imagen sobre otra. """
    bg_height, bg_width = background.shape[:2]
    ol_height, ol_width = overlay.shape[:2]

    if x + ol_width > bg_width or y + ol_height > bg_height:
        return background  # No superpone si la imagen sale del fondo

    alpha_mask = overlay[:, :, 3] / 255.0
    for c in range(0, 3):
        background[y:y+ol_height, x:x+ol_width, c] = (1.0 - alpha_mask) * background[y:y+ol_height, x:x+ol_width, c] + alpha_mask * overlay[:, :, c]

    return background

# Función para simular el movimiento de caminar
def simulate_walking(x, y, step_size, frame_count):
    angle = frame_count % 360  # Cambiar ángulo para simular caminar
    delta_x = int(step_size * np.cos(np.radians(angle)))
    delta_y = int(step_size * np.sin(np.radians(angle)))
    return x + delta_x, y + delta_y

# Inicializar la ventana de OpenCV
cv2.namedWindow('Hulk movil')

# Posición inicial del muñeco
muñeco_x, muñeco_y = window_width // 2, window_height // 2

# Parámetros de movimiento
step_size = 10
frame_count = 0

while True:
    # Crear una copia del fondo
    frame = fondo.copy()
    
    # Actualizar la posición del muñeco simulando caminar
    muñeco_x, muñeco_y = simulate_walking(muñeco_x, muñeco_y, step_size, frame_count)
    
    # Asegurarse de que el muñeco no salga de la ventana
    muñeco_x = max(0, min(muñeco_x, window_width - muñeco.shape[1]))
    muñeco_y = max(0, min(muñeco_y, window_height - muñeco.shape[0]))
    
    # Superponer el muñeco en la posición actual
    frame = overlay_image(frame, muñeco, muñeco_x, muñeco_y)
    
    # Mostrar la imagen
    cv2.imshow('Hulk movil', frame)
    
    frame_count += 1
    
    if cv2.waitKey(30) & 0xFF == 27:
        break

cv2.destroyAllWindows()
