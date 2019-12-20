import pytest
import requests
import allure
from lxml import html
import variables.url
import time


url_hinews = variables.url.url_hinews_response
url_android = variables.url.url_android_response
url_apple = variables.url.url_apple_response
url_2bitcoins = variables.url.url_2bitcoins_response


@allure.feature('Проверяем время отклика')
@pytest.mark.parametrize('url', [url_hinews, url_android, url_apple, url_2bitcoins])
def test_response_time(url):
    print(time.strftime('\n%H:%M:%S, %d/%m/%Y'), f'Проверяем время отклика {url[0]}\n')
    if response_time(url):
        print('status - OK')
    else:
        print('status - FAIL')
        pytest.fail('Большое время отклика')


def response_time(url):
    flag = True
    for i in url:
        response = requests.get(i).elapsed.total_seconds()
        try:
            with allure.step(f'{response} - время отклика - {i}'):
                assert response < 3
                print(f'{response} - меньше 3 секунд - {i}')
        except AssertionError:
            flag = False
            print(f'{response} - больше 3 секунд - {i}')
    return flag
