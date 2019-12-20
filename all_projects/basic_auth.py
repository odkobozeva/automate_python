import pytest
import requests
import allure


@allure.feature('Проверка работы сервера и базовой авторизации')
@pytest.mark.parametrize('url', ['http://webdev.2miners.com/',
                                 'https://eth.dev.2miners.com/en',
                                 'http://dev.2bitcoins.ru/',
                                 'http://dev.hi-news.ru/',
                                 'http://dev.appleinsider.ru/',
                                 'http://dev.androidinsider.ru/',
                                 'https://staging.2masternodes.com/'])
def test_main(url):
    print(f'Проверяем {url}')
    if server_is_available(url) and basic_auth(url):
        print('Status - Passed')
    else:
        print('Status - FAIL')
        pytest.fail('Basic Authentication - failed')


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


def server_is_available(url):
    status_auth = 0
    try:
        with allure.step(f'Проверяем ответ сервера от - {url}'):
            status_auth = requests.get(f'{url}', auth=('beta', 'ateb')).status_code
            assert status_auth == 200

    except requests.exceptions.SSLError:
        print('SSL Cert Verification Error')

    except requests.ConnectionError:
        print('Connection Error')

    except AssertionError:
        print('Server Error')
    finally:
        return status_auth == 200
