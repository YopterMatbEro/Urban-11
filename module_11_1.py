import os
from scripts.parsing import get_name_and_nickname_from_git, habr_daily_top_parser
from scripts.work_with_images import make_miniatures, make_collage, make_animation


if __name__ == '__main__':
    # requests
    # Простейшее обращение к overview странице указанного профиля и вывод указанного имени с никнеймом
    # get_name_and_nickname_from_git()

    # Парсинг ежедневного топа статей с Хабр
    # habr_daily_top_parser()

    # Pillow
    # Директория и список файлов-исходников
    directory = './sources/'
    image_names_list = os.listdir(directory)  # список изображений
    paths_to_images = [os.path.join(directory, image) for image in image_names_list]  # пути к изображениям

    # Создание миниатюр изображений
    make_miniatures(*paths_to_images)

    # Создание коллажа из миниатюр
    # make_collage()

    # Создание анимации из нескольких картинок
    # make_animation()
