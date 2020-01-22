import pytest
import variables.url
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@pytest.fixture(scope="session")
def browser():
    capabilities = DesiredCapabilities.CHROME
    capabilities['loggingPrefs'] = {'browser': 'ALL'}
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--env", action="store")
    parser.addoption("--url", action="store", default=None, help="Choose url: hinews, android, apple, 2bitcoins")


@pytest.fixture(scope='session')
def env(request):
    env_value = request.config.option.env
    if env_value == 'dev':
        env_value = 'http://beta:ateb@dev.'
    else:
        env_value = 'https://'
    return env_value


@pytest.fixture(scope='session')
def url_amp(request):
    url_value = request.config.option.url
    if url_value == '2bitcoins':
        url_value = variables.url.url_bitcoins_amp
    elif url_value == 'android':
        url_value = variables.url.url_android_amp
    elif url_value == 'apple':
        url_value = variables.url.url_apple_amp
    elif url_value == 'hinews':
        url_value = variables.url.url_hinews_amp
    else:
        raise pytest.UsageError("--url must be: hinews, android, apple, 2bitcoins")
    return url_value
