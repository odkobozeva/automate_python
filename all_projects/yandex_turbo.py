import pytest
import requests
import allure
import time


@allure.feature('Проверяем яндекс турбо')
@pytest.mark.parametrize('url', ['hi-news.ru', 'appleinsider.ru', 'androidinsider.ru'])
def test_main(url):
    print(f'\nПроверяем {url}')
    if yandex_turbo_stat(url):
        print('status - OK')
    else:
        print('status - FAIL')
        pytest.fail(f'Ошибка яндекс турбо - {url}')


def yandex_turbo(url, current_time):
    header = {'Authorization': 'OAuth AQAAAAAA_kG0AAUEer70CsapOkTJigQ-GDj9LWA'}
    result = requests.get(f'https://api.webmaster.yandex.net/v4/user/16662964/hosts/https:{url}:443/turbo/tasks/', headers=header).json()
    pages_count, errors_count, warnings_count = 0, 0, 0
    for task in result['tasks']:
        try:
            if task['created_at'][:10] == current_time:
                with allure.step(f"{task['created_at'][:10]} - {task['task_id']} - {task['load_status']}"):
                    result_task = requests.get(f'https://api.webmaster.yandex.net/v4/user/16662964/hosts/https:{url}:443/turbo/tasks/' + task['task_id'], headers=header).json()
                    with allure.step(f"{result_task['stats']['pages_count']} - pages"):
                        pages_count += result_task['stats']['pages_count']
                    with allure.step(f"{result_task['stats']['errors_count']} - errors"):
                        errors_count += result_task['stats']['errors_count']
                    with allure.step(f"{result_task['stats']['warnings_count']} - warnings"):
                        warnings_count += result_task['stats']['warnings_count']
            else:
                break
        except:
            print(f'Ошибка {task}')
    return pages_count, errors_count, warnings_count


def yandex_turbo_stat(url):
    current_time = time.strftime('%Y-%m-%d')
    pages_count, errors_count, warnings_count = yandex_turbo(url, current_time)
    with allure.step('Статистика'):
        if pages_count > 0:
            percent_errors = int((errors_count + warnings_count) / pages_count * 100)
            with allure.step(f'{percent_errors}% - процент ошибок'):
                print(f'{percent_errors}% - процент ошибок')
            with allure.step(f'{pages_count} - всего страниц'):
                print(f'{pages_count} - всего страниц')
            with allure.step(f'{errors_count} - всего ошибок'):
                print(f'{errors_count} - всего ошибок')
            with allure.step(f'{warnings_count} - всего предупреждений'):
                print(f'{warnings_count} - всего предупреждений')
        else:
            with allure.step(f'{current_time} - посты не выгружались'):
                print(f'\n{current_time} - посты не выгружались')
                print()
                return False
    return percent_errors < 15

