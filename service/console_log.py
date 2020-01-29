import pytest
import allure
import time


@pytest.mark.parametrize('url', [
    'https://2miners.com/',
    'https://2miners.com/eth-mining-pool',
    'https://2miners.com/eth-network-hashrate',
    # 'https://2miners.com/eth-network-difficulty',
    # 'https://2miners.com/open',
    # 'https://status.2miners.com/',
    # 'https://2miners.com/blog/december-work-progress-report/',
    # 'https://eth.2miners.com/en',
    # 'https://eth.2miners.com/en/blocks',
    # 'https://eth.2miners.com/en/payments',
    # 'https://eth.2miners.com/en/miners',
    # 'https://eth.2miners.com/en/help',
    # 'https://2miners.com/eth-stats/',
])
def test_console_log(url, browser):
    print(f'Проверяем {url}')
    page = BasePage(browser)
    page.go_to_site(url)
    time.sleep(3)
    err_list = page.get_log()
    flag = check_log(url, err_list)
    if not flag:
        page.get_screenshot(url)
    check_result(flag, url)


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def go_to_site(self, url):
        return self.browser.get(url)

    def get_log(self):
        return self.browser.get_log('browser')

    def get_screenshot(self, url):
        timestamp = str(time.time())
        url_name = url.replace('https://', '').replace('/', '_')
        self.browser.set_window_size(1900, 3000)
        self.browser.save_screenshot('temp_console_log/' + timestamp + url_name + '.png')
        allure.attach.file('temp_console_log/' + timestamp + url_name + '.png')


def check_log(url, err_list):
    flag = True
    with allure.step(url):
        for index, err in enumerate(err_list):
            if err['level'] == 'SEVERE':
                flag = False
                print(index, err)
    return flag


def check_result(flag, url):
    if not flag:
        pytest.fail('Ошибки в консоли')
    else:
        print('В консоли нет "SEVERE" ошибок\n')
