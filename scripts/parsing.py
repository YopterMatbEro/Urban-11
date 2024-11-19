import json
import lxml
from datetime import datetime
import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent


def get_name_and_nickname_from_git():
    url = 'https://github.com/YopterMatbEro'  # overview профиля, можно указать другой профиль, найдется его имя и никнейм
    response = requests.get(url).text
    git_soup = BeautifulSoup(response, 'lxml')
    name = git_soup.find('span', class_='p-name vcard-fullname d-block overflow-hidden', itemprop='name').text
    nickname = git_soup.find('span', class_='p-nickname vcard-username d-block', itemprop='additionalName').text
    print(name, nickname)  # Evgeniy Ishimtsev / YopterMatbEro


def habr_daily_top_parser():
    ua = UserAgent()
    headers = {
        'accept': 'application/json, text/plain, */*',
        'user-Agent': ua.google,
    }
    article_dict = {}
    url = f'https://habr.com/ru/top/daily/'  # ежедневный топ статей

    habr = requests.get(url, headers=headers).text

    habr_soup = BeautifulSoup(habr, 'lxml')
    all_hrefs_articles = habr_soup.find_all('a', class_='tm-title__link')  # все статьи

    for article in all_hrefs_articles:
        article_name = article.find('span').text  # названия статей
        article_link = f'https://habr.com{article.get("href")}'  # ссылки
        article_dict[article_name] = article_link

    with open(f'habr_parsing/articles_{datetime.now().strftime("%d_%m_%Y")}.json', 'w', encoding='utf-8') as file:
        try:
            json.dump(article_dict, file, indent=4, ensure_ascii=False)  # запись в .json-файл (отступы=4, без кодировки)
            print('Статьи были успешно получены')
        except:
            print('Статьи не удалось получить')


if __name__ == "__main__":
    print('Запускайте функции через файл module_11_1.py')
