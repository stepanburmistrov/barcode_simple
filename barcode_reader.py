import cv2
from pyzbar import pyzbar

def decode_barcode(image):
    # Распознавание штрихкодов на изображении
    decoded_objects = pyzbar.decode(image)
    for obj in decoded_objects:
        # Вывести данные штрихкода
        print("Data", obj.data.decode("utf-8"))
        # Обвести штрихкод на изображении
        image = cv2.rectangle(image, (obj.rect.left, obj.rect.top), 
                              (obj.rect.left + obj.rect.width, obj.rect.top + obj.rect.height),
                              (0, 255, 0), 2)
    return image

# Загрузка изображения
image_path = "barcode.jpg"  # Замените на путь к вашему изображению
image = cv2.imread(image_path)

# Распознавание штрихкодов
decoded_image = decode_barcode(image)

# Показать изображение
cv2.imshow("Image", decoded_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
