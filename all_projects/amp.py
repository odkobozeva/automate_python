import pytest
import requests
import allure
import subprocess
import json
from bs4 import BeautifulSoup


@allure.feature('Проверяем валидацию AMP')
def test_amp_validate(env, url_amp):
    articles = get_last_posts_amp(env, url_amp)
    if check_validate(env, articles):
        print('AMP validation - success')
    else:
        pytest.fail('Ошибка валидации AMP')


def get_last_posts_amp(env, url):
    if url[0] == '2bitcoins.ru/amp/':
        find_link = {'tag': 'article', 'class': 'post-preview'}
    elif url[0] == 'appleinsider.ru/amp/':
        find_link = {'tag': 'h2', 'class': 'entry-title'}
    else:
        find_link = {'tag': 'h2', 'class': 'loop-title'}
    try:
        response = requests.get(env + url[0]).text
        articles = BeautifulSoup(response, 'html.parser').find_all(find_link['tag'], find_link['class'])
        for i in articles:
            article_url = i.a["href"].replace("https://", "").replace("http://dev.", "")
            url.append(article_url)
    except AssertionError:
        print('не удалось получить список последних постов')
    return url


def check_validate(env, articles):
    flag = True
    for article_url in articles:
        str_result = subprocess.run(f'amphtml-validator {env}{article_url} --format=json', shell=True, universal_newlines=True, stdout=subprocess.PIPE).stdout
        result = json.loads(str_result)
        status = result[f'{env}{article_url}']['status']
        with allure.step(f"{status} - {env}{article_url}"):
            try:
                assert status == 'PASS'
            except AssertionError:
                flag = False
                print(f"{status} - {env}{article_url}")
                errors = result[env + article_url]['errors']
                for counter, error in enumerate(errors):
                    with allure.step(f"{counter} - {error['message']}"):
                        print(counter, error['message'])
    return flag
