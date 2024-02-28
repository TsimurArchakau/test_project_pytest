import pytest
from selenium import webdriver


@pytest.fixture(scope='class')
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--disable-geolocation')
    options.add_argument('--disable-notifications')
    options.add_argument('--window-size=1920,1080')
    with webdriver.Chrome(options=options) as driver:
        yield driver
