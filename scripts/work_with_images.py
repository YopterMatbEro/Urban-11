import os
from PIL import Image


def make_miniatures(*files):
    size = (128, 128)

    for infile in files:
        outfile = os.path.splitext(infile)[0].replace('sources', 'for_miniatures') + '.jpeg'
        if infile != outfile:
            try:
                with Image.open(infile) as im:
                    im.thumbnail(size)
                    im.save(outfile, "JPEG")
                    print('Успешно создана миниатюра для', infile)
            except OSError:
                print('Не удалось создать thumbnail для', infile)


def make_collage():
    # Загружаем миниатюры для создания коллажа
    directory = './for_miniatures/'
    image_names_list = os.listdir(directory)
    images = [Image.open(os.path.join(directory, image)) for image in image_names_list]

    # Предположим, что все изображения одинакового размера (для этого сделали их миниатюрами)
    width, height = images[0].size

    # Определяем размеры коллажа (например, 2 строки и 2 столбца, т.к. у нас 4 миниатюры)
    collage_width = 2 * width
    collage_height = 2 * height

    # Создаем пустое изображение для коллажа
    collage = Image.new('RGB', (collage_width, collage_height))

    # Размещаем изображения на коллаже
    collage.paste(images[0], (0, 0))  # Верхний левый угол
    collage.paste(images[1], (width, 0))  # Верхний правый угол
    collage.paste(images[2], (0, height))  # Нижний левый угол
    collage.paste(images[3], (width, height))  # Нижний правый угол

    collage.save('./for_collage/collage.jpg')


def make_animation():
    """
    В интернете легче найти картинки для анимации в цельном виде, чем отдельными изображениями, а потому сначала
    разобьем условный коллаж на изображения
    """
    # Извлечение изображений из коллажа для создания анимации
    collage = Image.open('./for_animation/collage.png')
    collage_width, collage_height = collage.size

    num_columns = 5
    num_rows = 4

    tile_width = collage_width // num_columns
    tile_height = collage_height // num_rows

    # Вычисляем координаты для обрезки
    for row in range(num_rows):
        for column in range(num_columns):
            left = column * tile_width
            upper = row * tile_height
            right = left + tile_width
            lower = upper + tile_height

            tile = collage.crop((left, upper, right, lower))

            tile.save(f'./for_animation/image_{row * num_columns + column + 1}.png')

    directory = './for_animation/'

    # Если файл анимации уже есть, удаляем, во избежание проблем
    animation_path = os.path.join(directory, 'animation.gif')
    if os.path.exists(animation_path):
        os.remove(animation_path)

    # Определяем список имён файлов для анимации
    images = [os.path.join(directory, file) for file in os.listdir(directory)]

    # Загружаем изображения для анимации
    frames = []
    for image in images[1:]:  # Открываем каждый кадр и добавляем в список frames (исключая файл collage.png c < i)
        frame = Image.open(image)
        frames.append(frame)

    # Сохраняем как GIF
    frames[0].save(
        './for_animation/animation.gif',
        save_all=True,
        append_images=frames[1:],
        duration=80,  # Время отображения каждого кадра в миллисекундах
        loop=0  # Количество циклов анимации (0 - бесконечно).
    )


if __name__ == "__main__":
    print('Запускайте функции через файл: module_11_1.py')
