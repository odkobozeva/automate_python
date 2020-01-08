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
        find_post = {'tag': 'div', 'class': 'type-post'}
        find_link_more = {'tag': 'a', 'class': 'more-link'}

    elif f'{url}' == 'https://appleinsider.ru/':
        find_post = {'tag': 'article', 'class': ''}
        find_link_more = {'tag': 'a', 'class': 'btn-outline'}
    elif f'{url}' == 'https://androidinsider.ru/':
        find_post = {'tag': 'div', 'class': 'post-title'}
        find_link_more = {'tag': 'a', 'class': 'more-link'}
    flag = True
    response = requests.get(f'{url}').text
    articles = BeautifulSoup(response, 'html.parser').find_all(find_post['tag'], find_post['class'])
    link_more = BeautifulSoup(response, 'html.parser').find_all(find_link_more['tag'], find_link_more['class'])
    post_url = [article.a['href'] for article in articles]
    post_link_more = [link['href'] for link in link_more]
    for i in post_url:
        if i not in post_link_more:
            flag = False
            print(f'Нет тэга <!--more--> {i}')
    return flag
