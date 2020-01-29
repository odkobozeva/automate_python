import pytest
import requests
import allure


@allure.feature('Проверяем работу API')
@pytest.mark.parametrize('api', [
    'https://currencies.2miners.com/api/v1/ticker',
    'https://currencies.2miners.com/api/v1/ticker/ethereum',
    'https://status-api.2miners.com',
    'https://2miners.com/api/full-payments',
    'https://eth.2miners.com/api/payments',
    'https://eth.2miners.com/api/blocks',
    'https://eth.2miners.com/api/stats',
    'https://hr.2miners.com/api/v1/pool/payments',
    'https://hr.2miners.com/api/v1/pool/stats',
    'https://hr.2miners.com/api/v1/pool/hashrate',
    'https://hr.2miners.com/api/v1/pool/fee_rewards',
    'https://hr.2miners.com/api/v1/pool/hashrate/short',
    'https://hr.2miners.com/api/v1/dashboards/hashrate/eth',
    'https://hr.2miners.com/api/v1/hashrate/1d/eth',
])
def test_api(api):
    flag = True
    print(f'Проверяем {api}')
    try:
        response = requests.get(api)
        response_status = response.status_code
        try:
            with allure.step(f'{response_status}  - статус код - {api}'):
                assert response_status == 200
                print(f'{response_status} - статус код')
            try:
                with allure.step('Не пустое тело ответа'):
                    assert response.text
            except AssertionError:
                flag = False
                print(f'{response_status} - пустое тело ответа\n')
        except AssertionError:
            flag = False
            print(f'{response_status} - статус код\n')
    except:
        flag = False
        print('Не удалось получить статус код')
    if not flag:
        pytest.fail('Ошибка в апи')
