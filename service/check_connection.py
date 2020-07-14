import pytest
import requests
import allure
import variables.url


@pytest.fixture(scope='session')
def get_url(request):
    url_value = request.config.option.url
    if url_value == 'hinews':
        url_value = 'hi-news.ru/'
    if url_value == 'android':
        url_value = 'androidinsider.ru/'
    if url_value == 'apple':
        url_value = 'appleinsider.ru/'
    if url_value == 'bitcoins':
        url_value = '2bitcoins.ru/'
    if url_value == 'dash':
        url_value = 'eth.2miners.com/en'
    return url_value


@allure.feature('Проверка ответа сервера')
def test_connection(env, get_url):
    flag = True
    url = env + get_url + '?a=1'
    if url == 'http://beta:ateb@dev.eth.2miners.com/en':
        url = url.replace("dev.eth", "eth.dev")
    try:
        status_auth = requests.get(url).status_code
        try:
            with allure.step(f'{status_auth} - ответ сервера - {url}'):
                assert status_auth == 200
        except AssertionError:
            flag = False
            print(f'Server Error - {status_auth} - {url}')
    except requests.ConnectionError:
        flag = False
        print(f'Connection Error - {url}')
    except requests.Timeout:
        flag = False
        print(f'Timeout - {url}')

    if flag:
        print('Проверка соединения - Passed')
    else:
        pytest.fail('Проверка соединения - Failed')
