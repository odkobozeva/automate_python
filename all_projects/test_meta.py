import pytest
import requests
from bs4 import BeautifulSoup
import allure
import variables.url
import variables.meta_apple
import variables.meta_android
import variables.meta_hinews
import re

apple_with_robots = variables.url.url_apple_with_robots
apple_without_robots = variables.url.url_apple_without_robots
meta_description_apple = variables.meta_apple.description
meta_title_apple = variables.meta_apple.title

hinews_with_robots = variables.url.url_hinews_with_robots
hinews_without_robots = variables.url.url_hinews_without_robots
meta_description_hinews = variables.meta_hinews.description
meta_title_hinews = variables.meta_hinews.title

android_with_robots = variables.url.url_android_with_robots
android_without_robots = variables.url.url_android_without_robots
meta_description_android = variables.meta_android.description
meta_title_android = variables.meta_android.title



'''appleinsider'''


@pytest.mark.robots
@allure.feature('Проверка meta name="robots"')
@pytest.mark.parametrize('url', apple_with_robots)
def test_check_meta_robots_apple(env, url):
    check_meta_robots(env, url)


@pytest.mark.robots
@allure.feature('Проверка meta without name="robots"')
@pytest.mark.parametrize('url', apple_without_robots)
def test_check_meta_without_robots_apple(env, url):
    check_meta_without_robots(env, url)


@pytest.mark.canonical
@allure.feature('Проверка link canonical')
@pytest.mark.parametrize('url', apple_with_robots + apple_without_robots)
def test_check_meta_canonical_apple(env, url):
    check_meta_canonical(env, url)


@pytest.mark.description
@allure.feature('Проверка meta description')
@pytest.mark.parametrize("url", meta_description_apple)
def test_check_meta_description_apple(env, url):
    check_meta_description(env, url)

@pytest.mark.title
@allure.feature('Проверка meta title')
@pytest.mark.parametrize("url", meta_title_apple)
def test_check_meta_title_apple(env, url):
    check_meta_title(env, url)


'''hi-news'''


@pytest.mark.robots
@allure.feature('Проверка meta name="robots"')
@pytest.mark.parametrize('url', hinews_with_robots)
def test_check_meta_robots_hinews(env, url):
    check_meta_robots(env, url)


@pytest.mark.robots
@allure.feature('Проверка meta without name="robots"')
@pytest.mark.parametrize('url', hinews_without_robots)
def test_check_meta_without_robots_hinews(env, url):
    check_meta_without_robots(env, url)


@pytest.mark.canonical
@allure.feature('Проверка link canonical')
@pytest.mark.parametrize('url', hinews_with_robots + hinews_without_robots)
def test_check_meta_canonical_hinews(env, url):
    check_meta_canonical(env, url)


@pytest.mark.description
@allure.feature('Проверка meta description')
@pytest.mark.parametrize("url", meta_description_hinews)
def test_check_meta_description_hinews(env, url):
    check_meta_description(env, url)


@pytest.mark.title
@allure.feature('Проверка meta title')
@pytest.mark.parametrize("url", meta_title_hinews)
def test_check_meta_title_hinews(env, url):
    check_meta_title(env, url)


'''androidinsider'''


@pytest.mark.robots
@allure.feature('Проверка meta name="robots"')
@pytest.mark.parametrize('url', android_with_robots)
def test_check_meta_robots_android(env, url):
    check_meta_robots(env, url)


@pytest.mark.robots
@allure.feature('Проверка meta without name="robots"')
@pytest.mark.parametrize('url', android_without_robots)
def test_check_meta_without_robots_android(env, url):
    check_meta_without_robots(env, url)


@pytest.mark.canonical
@allure.feature('Проверка link canonical')
@pytest.mark.parametrize('url', android_with_robots + android_without_robots)
def test_check_meta_canonical_android(env, url):
    check_meta_canonical(env, url)


@pytest.mark.description
@allure.feature('Проверка meta description')
@pytest.mark.parametrize("url", meta_description_android)
def test_check_meta_description_android(env, url):
    check_meta_description(env, url)


@pytest.mark.title
@allure.feature('Проверка meta title')
@pytest.mark.parametrize("url", meta_title_android)
def test_check_meta_title_android(env, url):
    check_meta_title(env, url)


def check_meta_robots(env, url):
    print(f'Проверяем {env}{url}')
    meta_robots = ''
    try:
        response = requests.get(env + url).text
        meta_robots = BeautifulSoup(response, features="lxml").find_all('meta', attrs={'name': 'robots'})
    except:
        print("Ошибка соединения")
        pytest.fail('Status - Fail')

    if len(meta_robots) == 0:
        print("На странице нет meta name='robots'\n")
        pytest.fail('Status - Fail. meta name="robots"')
    elif len(meta_robots) > 1:
        print("На странице несколько meta name='robots'\n")
        pytest.fail('Status - Fail. На странице несколько meta name="robots"')
    try:
        with allure.step(f"{meta_robots[0]} - {env}{url}"):
            assert meta_robots[0]['content'] == 'noyaca'
    except AssertionError:
        print(f"Изменился meta robots - {meta_robots[0]} - {env}{url}\n")
        pytest.fail('Status - Fail')


def check_meta_without_robots(env, url):
    print(f'Проверяем {env}{url}')
    meta_robots = None
    try:
        response = requests.get(env + url).text
        meta_robots = BeautifulSoup(response, features="lxml").find('meta', attrs={'name': 'robots'})
    except:
        print("Ошибка соединения")
        pytest.fail('Status - Fail')

    try:
        with allure.step(f'Тэг meta name="robots" отсутствует - {env}{url}'):
            assert meta_robots is None
    except AssertionError:
        print(f"Ошибка. Присутствует тэг - {meta_robots}\n")
        pytest.fail('Status - Fail')


def check_meta_canonical(env, url):
    print(f'Проверяем {env}{url}')
    meta_canonical = ''
    try:
        response = requests.get(env + url).text
        meta_canonical = BeautifulSoup(response, features="lxml").find_all('link', attrs={'rel': 'canonical'})
    except:
        print(f"Ошибка соединения\n")
        pytest.fail('Status - Fail')

    if len(meta_canonical) > 1:
        print("На странице несколько link rel='canonical'\n")
        pytest.fail('Status - Fail. На странице несколько link rel="canonical"')
    elif len(meta_canonical) == 0:
        print("На странице нет link rel='canonical'\n")
        pytest.fail('Status - Fail. На странице нет link rel="canonical"')

    url = re.sub('/page/.*', '', url)
    env = re.sub('beta:ateb@', '', env)
    try:
        with allure.step(f'link rel="canonical" равен - {env}{url}'):
            assert meta_canonical[0]['href'] == env + url
    except AssertionError:
        print(f'Изменился link rel="canonical". Было - {env}{url}  Cтало - {meta_canonical[0]["href"]}\n')
        pytest.fail('Status - Fail. Изменился link rel="canonical"')


def check_meta_description(env, url):
    for key in url.keys():
        print(f'Проверяем {env}{key}')
        try:
            response = requests.get(env + key).text
            meta = BeautifulSoup(response, features="lxml").find_all('meta', attrs={'name': 'description'})

        except:
            print(f"Ошибка соединения\n")
            pytest.fail('Status - Fail')

        if len(meta) > 1:
            print("На странице несколько meta name ='description'\n")
            pytest.fail('Status - Fail. На странице несколько meta name ="description"')

        elif len(meta) == 0:
            meta_content = ''
        else:
            meta_content = meta[0]["content"]

        try:
            with allure.step(key):
                with allure.step(f'Было - {url[key]}'):
                    pass
                with allure.step(f'Стало - {meta_content}'):
                    pass
                assert url[key] == meta_content
        except AssertionError:
            print("Изменился meta description. См. отчет.\n")
            pytest.fail('Status - Fail. Изменился meta description. См. отчет.')


def check_meta_title(env, url):
    for key in url.keys():
        print(f'Проверяем {env}{key}')
        try:
            response = requests.get(env + key).text
            meta = BeautifulSoup(response, features="lxml").head.title

        except:
            print(f"Ошибка соединения\n")
            pytest.fail('Status - Fail')

        if len(meta) > 1:
            print("На странице несколько meta name ='title'\n")
            pytest.fail('Status - Fail. На странице несколько meta name ="title"')

        elif len(meta) == 0:
            meta_content = ''
        else:
            meta_content = meta.text

        try:
            with allure.step(key):
                with allure.step(f'Было - {url[key]}'):
                    pass
                with allure.step(f'Стало - {meta_content}'):
                    pass
                assert url[key] == meta_content
        except AssertionError:
            print("Изменился meta title. См. отчет.\n")
            pytest.fail('Status - Fail. Изменился meta title. См. отчет.')