import allure
from allure_commons.types import AttachmentType


def add_screen(browser):
    png = browser.driver.get_screen_as_png()
    allure.attach(png, 'screen', AttachmentType.PNG, '.png')


def add_logs(browser):
    log = "".join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', AttachmentType.TEXT, '.log')


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(html, 'page_source', AttachmentType.HTML, '.html')