import pytest
from selene.support.shared import browser
from selenium import webdriver


@pytest.fixture(scope="function", autouse=True)
def browser_setup():
    # Настройки
    options = webdriver.ChromeOptions()
    # options.page_load_strategy = 'eager'
    browser.config.driver_options = options
    browser.config.browser_name = 'chrome'
    browser.config.base_url = 'https://demoqa.com'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    browser.open('/automation-practice-form')

    yield

    # Закрыть браузер
    browser.quit()