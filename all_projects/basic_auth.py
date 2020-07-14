import pytest
import requests
import allure


@allure.feature('Проверка работы сервера и базовой авторизации')
@pytest.mark.parametrize('url', ['http://webdev.2miners.com/'])
def test_basic_auth_2miners(url):
    main(url)


@allure.feature('Проверка работы сервера и базовой авторизации')
@pytest.mark.parametrize('url', ['https://eth.webdev.2miners.com/en'])
def test_basic_auth_2minersdash(url):
    main(url)

@allure.feature('Проверка работы сервера и базовой авторизации')
@pytest.mark.parametrize('url', ['http://dev.2bitcoins.ru/'])
def test_basic_auth_2bitcoins(url):
    main(url)


@allure.feature('Проверка работы сервера и базовой авторизации')
@pytest.mark.parametrize('url', ['http://dev.appleinsider.ru/'])
def test_basic_auth_apple(url):
    main(url)


@allure.feature('Проверка работы сервера и базовой авторизации')
@pytest.mark.parametrize('url', ['http://dev.androidinsider.ru/'])
def test_basic_auth_android(url):
    main(url)


@allure.feature('Проверка работы сервера и базовой авторизации')
@pytest.mark.parametrize('url', ['http://dev.hi-news.ru/'])
def test_basic_auth_hinews(url):
    main(url)


def main(url):
    print(f'Проверяем {url}')
    if server_is_available(url) and basic_auth(url):
        print('Status - Passed')
    else:
        print('Status - FAIL')
        pytest.fail('Basic Authentication - failed')


def server_is_available(url):
    status_auth = 0
    try:
        with allure.step(f'Проверяем ответ сервера от - {url}'):
            status_auth = requests.get(f'{url}', auth=('****', '****')).status_code
            assert status_auth == 200

    except requests.exceptions.SSLError:
        print('SSL Cert Verification Error')

    except requests.ConnectionError:
        print('Connection Error')

    except AssertionError:
        print('Server Error')
    finally:
        return status_auth == 200


def basic_auth(url):
    status = 0
    try:
        status = requests.get(f'{url}').status_code
        with allure.step(f'Проверяем базовую авторизацию - {url}'):
            assert status == 401
    except AssertionError:
        print('Базовая авторизация отключена')
    except:
        print('Не удалось получить статус')
    finally:
        return status == 401
