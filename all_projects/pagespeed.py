import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import time
# from xvfbwrapper import Xvfb


@pytest.mark.parametrize('url', [
    'https://appleinsider.ru/',
    # 'https://androidinsider.ru/feed',
    # 'https://hinews.ru/feed',
    # 'https://2bitcoins.ru/feed/zen',
    # 'https://2bitcoins.ru/feed/'
])
def test_rss_validation(url, browser):
    feed_page = ValidationHelper(browser)
    feed_page.go_to_site()
    feed_page.enter_url(url)
    feed_page.click_on_the_check_button()
    result_mobile = feed_page.get_result_mobile()
    mob = feed_page.check_result(browser, url, result_mobile, 'mobile')
    feed_page.switch_to_desktop_tab()
    result_desktop = feed_page.get_result_desktop()
    desk = feed_page.check_result(browser, url, result_desktop, 'desktop')
    time.sleep(2)
    if mob and desk:
        print('status - OK')
    else:
        print('status - FAIL')
        pytest.fail('Маленькая скорость')
    # feed_page.switch_to_desktop_tab()
    # print(feed_page.get_result_desktop())

    # time.sleep(5)
    # text_result = feed_page.get_text_result()
    # feed_page.check_result(url, result, text_result)


class ValidatorW3Locators:
    LOCATOR_INPUT = (By.TAG_NAME, 'input')
    LOCATOR_BUTTON = (By.XPATH, "//*[contains(text(), 'АНАЛИЗИРОВАТЬ')]")
    LOCATOR_DESKTOP_TAB = (By.XPATH, "//*[contains(text(), 'Для компьютеров')]")
    LOCATOR_RESULT = (By.CLASS_NAME, 'lh-score__gauge')
    # LOCATOR_TEXT_RESULT = ('//*[@id="main"]/p[1]')


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'https://developers.google.com/speed/pagespeed/insights/?hl=RU'
        # self.base_url = 'https://appleinsider.ru/'

    def go_to_site(self):
        return self.browser.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_all_elements_located(locator), message=f"Can't find element by locator {locator}")


class ValidationHelper(BasePage):

    def enter_url(self, word):
        return self.find_element(ValidatorW3Locators.LOCATOR_INPUT).send_keys(word)

    def click_on_the_check_button(self):
        return self.find_element(ValidatorW3Locators.LOCATOR_BUTTON, time=10).click()

    def switch_to_desktop_tab(self):
        return self.find_element(ValidatorW3Locators.LOCATOR_DESKTOP_TAB, time=10).click()

    def get_screenshot(self, url, strategy):
        timestamp = str(time.time())
        url_name = url.replace('https://', '').replace('/feed', '').replace('/', '')
        self.browser.set_window_size(1900, 5000)
        self.browser.save_screenshot('temp/' + timestamp + strategy + url_name + '.png')
        allure.attach.file('temp/' + timestamp + strategy + url_name + '.png')

    def get_result_mobile(self):
        try:
            result = self.find_elements(ValidatorW3Locators.LOCATOR_RESULT, time=10)[0].text
        except:
            result = 'Не удалось провалидировать страницу\n'
        return result

    def get_result_desktop(self):
        try:
            result = self.find_elements(ValidatorW3Locators.LOCATOR_RESULT, time=10)[1].text
        except:
            result = 'Не удалось провалидировать страницу\n'
        return result

    def check_result(self, browser, url, result, strategy):
        flag = True
        ts = str(time.time())
        with allure.step(f'{strategy} - {url}'):
            try:
                with allure.step(f'{result} > 100'):
                    self.get_screenshot(url, strategy)
                    assert int(result) > 100
                    # print('Скорость больше 70')
            except AssertionError:
                flag = False
                print(result + ' - mobile - ' + url)
        return flag









    #
    # def get_text_result(self):
    #     try:
    #         text = self.find_element_by_xpath(ValidatorW3Locators.LOCATOR_TEXT_RESULT, time=10).text
    #     except:
    #         text = ''
    #     return text
    #
    # def get_screenshot(self, url):
    #     timestamp = str(time.time())
    #     url_name = url.replace('https://', '').replace('/feed', '').replace('/', '')
    #     self.browser.set_window_size(1900, 3000)
    #     self.browser.save_screenshot('temp_feed/' + timestamp + url_name + '.png')
    #     allure.attach.file('temp_feed/' + timestamp + url_name + '.png')
    #
    # def check_result(self, url, result, text_result):
    #     try:
    #         with allure.step(f'{url} - {result}'):
    #             assert result == 'Congratulations!'
    #             print(f'{url} - {text_result}')
    #     except AssertionError:
    #         self.get_screenshot(url)
    #         print(f'\n{url} - {result}')
    #         if text_result:
    #             print(f'Текст ошибки - {text_result}\n')
    #         pytest.fail('Ошибка валидации')
    #
