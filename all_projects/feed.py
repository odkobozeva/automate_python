import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import time
# from xvfbwrapper import Xvfb


@pytest.mark.parametrize('url', [
    'https://appleinsider.ru/feed/zen',
    'https://androidinsider.ru/feed',
    'https://hinews.ru/feed',
    'https://2bitcoins.ru/feed/zen',
    'https://2bitcoins.ru/feed/'
])
def test_rss_validation(url, browser):
    feed_page = ValidationHelper(browser)
    feed_page.go_to_site()
    feed_page.enter_url(url)
    feed_page.click_on_the_check_button()
    result = feed_page.get_result()
    text_result = feed_page.get_text_result()
    feed_page.check_result(url, result, text_result)


class ValidatorW3Locators:
    LOCATOR_INPUT_ADDRESS_FIELD = (By.ID, 'url')
    LOCATOR_CHECK_BUTTON = ('//a[@class="submit"]/span')
    LOCATOR_RESULT = (By.TAG_NAME, 'h2')
    LOCATOR_TEXT_RESULT = ('//*[@id="main"]/p[1]')


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'https://validator.w3.org/feed/'

    def go_to_site(self):
        return self.browser.get(self.base_url)

    def find_element(self, locator, time=10):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_element_by_xpath(self, locator, time=10):
        return self.browser.find_element_by_xpath(locator)


class ValidationHelper(BasePage):

    def enter_url(self, word):
        return self.find_element(ValidatorW3Locators.LOCATOR_INPUT_ADDRESS_FIELD).send_keys(word)

    def click_on_the_check_button(self):
        return self.find_element_by_xpath(ValidatorW3Locators.LOCATOR_CHECK_BUTTON, time=10).click()

    def get_result(self):
        try:
            result = self.find_element(ValidatorW3Locators.LOCATOR_RESULT, time=10).text
        except:
            result = 'Не удалось провалидировать страницу\n'
        return result

    def get_text_result(self):
        try:
            text = self.find_element_by_xpath(ValidatorW3Locators.LOCATOR_TEXT_RESULT, time=10).text
        except:
            text = ''
        return text

    def get_screenshot(self, url):
        timestamp = str(time.time())
        url_name = url.replace('https://', '').replace('/feed', '').replace('/', '')
        self.browser.set_window_size(1900, 3000)
        self.browser.save_screenshot('temp_feed/' + timestamp + url_name + '.png')
        allure.attach.file('temp_feed/' + timestamp + url_name + '.png')

    def check_result(self, url, result, text_result):
        try:
            with allure.step(f'{url} - {result}'):
                assert result == 'Congratulations!'
                print(f'{url} - {text_result}')
        except AssertionError:
            self.get_screenshot(url)
            print(f'\n{url} - {result}')
            if text_result:
                print(f'Текст ошибки - {text_result}\n')
            pytest.fail('Ошибка валидации')

