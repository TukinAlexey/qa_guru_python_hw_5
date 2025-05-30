import pytest
from selene import browser

@pytest.fixture(scope="session")
def browser_screen_size():
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield browser
    browser.quit()

@pytest.fixture
def open_browser(browser_screen_size):
    browser_screen_size.open('https://demoqa.com/automation-practice-form')