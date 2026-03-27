from PIL import Image
import os

# Путь к папке с фотографиями
path = "photo"
new_path = "photo_tests"
# 3420 1968


# Перебираем все файлы изображений в папке
for filename in os.listdir(path):
    if filename.endswith(".jpg") or filename.endswith(".png"):
        # Открываем изображение
        img = Image.open(os.path.join(path, filename))

        # Получаем размеры изображения
        img_width, img_height = img.size

        # Обрезаем правую и левую стороны изображения
        img = img.crop((0, 120, 2650, 1800))

        # Сохраняем измененное изображение
        img.save(os.path.join(new_path, filename))
