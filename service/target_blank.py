import pytest
import requests
from bs4 import BeautifulSoup


@pytest.mark.parametrize('url', ['https://mvet.ru/'])
def test_main(url):
    target(url)


def target(url):
    a = []
    response = requests.get(url).text
    items = BeautifulSoup(response, 'html.parser')
    for i in items.find_all('a', target=False):
        if i['href'][:16] !='https://mvet.ru/' and i['href'][:1] != '#' and len(i['href']) > 0 and i['href'][:3] != 'tel' and i['href'][:1] != '/':
        # if i['href'][:16] != 'https://mvet.ru/':
            print("Found the URL:", i['href'])
    print('_______________________________________________')




