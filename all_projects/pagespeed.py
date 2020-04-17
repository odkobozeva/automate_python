import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import time
import variables.url_hinews
import variables.url_apple
import variables.url_android
import variables.url_2bitcoins
hinews_pagespeed = variables.url_hinews.pagespeed
apple_pagespeed = variables.url_apple.pagespeed
android_pagespeed = variables.url_android.pagespeed
bitcoins_pagespeed = variables.url_2bitcoins.pagespeed
# from xvfbwrapper import Xvfb
# from xvfbwrapper import Xvfb


@pytest.mark.hinews
@allure.feature('Проверяем pagespeed для hinews')
@pytest.mark.parametrize('url', hinews_pagespeed)
def test_pagespeed_validation_hinews(url, browser):
    pagespeed_validation(url, browser)


@pytest.mark.apple
@allure.feature('Проверяем pagespeed для apple')
@pytest.mark.parametrize('url', apple_pagespeed)
def test_pagespeed_validation_apple(url, browser):
    pagespeed_validation(url, browser)


@pytest.mark.android
@allure.feature('Проверяем pagespeed для android')
@pytest.mark.parametrize('url', android_pagespeed)
def test_pagespeed_validation_android(url, browser):
    pagespeed_validation(url, browser)


@pytest.mark.bitcoins
@allure.feature('Проверяем pagespeed для 2bitcoins')
@pytest.mark.parametrize('url', bitcoins_pagespeed)
def test_pagespeed_validation_2bitcoins(url, browser):
    pagespeed_validation(url, browser)


def pagespeed_validation(url, browser):
    main_page = ValidationHelper(browser)
    main_page.go_to_site()
    main_page.enter_url(url)
    main_page.click_on_the_check_button()
    result_mobile = main_page.get_result_mobile()
    mob = main_page.check_result(url, result_mobile, 'mobile')
    main_page.switch_to_desktop_tab()
    result_desktop = main_page.get_result_desktop()
    desk = main_page.check_result(url, result_desktop, 'desktop')
    if mob and desk:
        print('status - OK')
    else:
        print('status - FAIL')
        pytest.fail('Скорость меньше 80 баллов')


class ValidatorW3Locators:
    LOCATOR_INPUT = (By.TAG_NAME, 'input')
    LOCATOR_BUTTON = (By.XPATH, "//*[contains(text(), 'АНАЛИЗИРОВАТЬ')]")
    LOCATOR_DESKTOP_TAB = (By.XPATH, "//*[contains(text(), 'Для компьютеров')]")
    LOCATOR_RESULT = (By.XPATH, "//*[@class='lh-gauge__percentage']")


class BasePage:
    def __init__(self, browser):
        self.browser = browser
        self.base_url = 'https://developers.google.com/speed/pagespeed/insights/?hl=RU'

    def go_to_site(self):
        return self.browser.get(self.base_url)

    def find_element(self, locator, time=30):
        return WebDriverWait(self.browser, time).until(EC.presence_of_element_located(locator), message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=30):
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
            result = self.find_elements(ValidatorW3Locators.LOCATOR_RESULT, time=300)[0].text
            assert result.isdigit() is True
        except:
            result = 0
        return result

    def get_result_desktop(self):
        try:
            result = self.find_elements(ValidatorW3Locators.LOCATOR_RESULT, time=100)[1].text
            assert result.isdigit() is True
        except:
            result = 0
        return result

    def check_result(self, url, result, strategy):
        flag = True
        ts = str(time.time())

        try:
            with allure.step(f'{result} - {strategy} - {url}'):
                if int(result) == 0:
                    self.get_screenshot(url, strategy)
                    print(f'{strategy} - не удалось провалидировать страницу - {url}')
                    return False
                if int(result) < 80:
                    self.get_screenshot(url, strategy)
                assert int(result) > 80
                print(f'{result} - {strategy} - {url}')
        except:
            flag = False
            print(f'{result} - {strategy} - {url}')
        return flag
