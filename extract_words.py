import cv2
import numpy as np
from PIL import Image
# Aquí iría la lógica para extraer palabras y convertirlas en clave privada
# Cargar la imagen
image_path = "C:/Users/Joaqu/OneDrive/Escritorio/CGDHoYiU0AEQXze.jpeg"  # Cambia esto por la ruta de tu imagen
image = cv2.imread(image_path)
# Convertir a escala de grises
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Aplicar un umbral
_, thresh_image = cv2.threshold(gray_image, 128, 255, cv2.THRESH_BINARY_INV)
# Obtener contornos de las palabras
contours, _ = cv2.findContours(thresh_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Lista para almacenar las palabras extraídas
words = []

# Loop a través de cada contorno encontrado
for contour in contours:
    x, y, w, h = cv2.boundingRect(contour)
    roi = thresh_image[y:y+h, x:x+w]  # Región de interés
    # Aquí puedes usar OCR para leer el texto
    # Por ejemplo, usando pytesseract:
    # import pytesseract
    # word = pytesseract.image_to_string(roi)
    # words.append(word.strip())
