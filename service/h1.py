import pytest
import requests
from bs4 import BeautifulSoup


@pytest.mark.parametrize('url', ['https://appleinsider.ru/'])
def test_h(url):
    a = []
    response = requests.get(url).text
    items = BeautifulSoup(response, 'html.parser')
    print()
    for i in items.find_all(["h1", "h2", "h3", "h4", "h5", "h6"]):
        print(i.name + ' ' + i.text.strip())
    print('_______________________________________________')