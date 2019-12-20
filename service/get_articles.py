import pytest
import requests
from bs4 import BeautifulSoup


def test_main():
    get_url('https://appleinsider.ru/page/')


# получить список урлов из заголовков
def get_url(url):
    a = []
    for i in range(37, 50, 4):  # страницы 40-2500 с шагом 250
        print(url + str(i))
        response = requests.get(url + str(i)).text
        items = BeautifulSoup(response, 'html.parser').find_all('h2')
        for item in items:
            a.append(item.a['href'].replace("https://", ""))

    #напечатать все
    # for item in a:
    #     print(f'\'{item}\',')

    #напечатать каждый третий элемент массива
    for item in range(0, len(a), 3):
        # print(f'\'{item}\',')
        print(f'\'{a[item]}\',')
