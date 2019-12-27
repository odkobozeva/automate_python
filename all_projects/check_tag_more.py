import pytest
import requests
import json
from lxml import html
from lxml import etree
from bs4 import BeautifulSoup
import allure


@pytest.mark.parametrize('url', ['https://hi-news.ru/',
                                 'https://appleinsider.ru/',
                                 'https://androidinsider.ru/'])
def test_main(url):
    print(f'Проверяем {url}')
    if tag_is_exist(url):
        print('Status - Passed')
    else:
        print()
        print('Status - FAIL')
        pytest.fail('Basic Authentication - failed')


def tag_is_exist(url):
    if f'{url}' == 'https://hi-news.ru/':
        find_post = ('div', 'type-post')
        find_link_more = ('a', 'more-link')

    elif f'{url}' == 'https://appleinsider.ru/':
        find_post = ('article', '')
        find_link_more = ('a', 'btn-outline')

    elif f'{url}' == 'https://androidinsider.ru/':
        find_post = ('div', 'post-title')
        find_link_more = ('a', 'more-link')
    flag = True
    response = requests.get(f'{url}').text
    articles = BeautifulSoup(response, 'html.parser').find_all(find_post[0], find_post[1])
    link_more = BeautifulSoup(response, 'html.parser').find_all(find_link_more[0], find_link_more[1])
    post_url = [article.a['href'] for article in articles]
    post_link_more = [link['href'] for link in link_more]
    for i in post_url:
        if i not in post_link_more:
            flag = False
            print(f'Нет тэга <!--more--> {i}')
    return flag
