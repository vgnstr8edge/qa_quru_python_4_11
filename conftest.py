from selene import browser
import pytest


@pytest.fixture
def browser_settings():
    browser.config.hold_browser_open = True
    browser.open('https://demoqa.com/automation-practice-form')
    browser.driver.maximize_window()
    browser.config.timeout = 6.0
    #browser.config.window_height = 1920
    #browser.config.window_width = 1080




