from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

import pytest

@pytest.fixture(params=["chrome", "firefox"], scope='class')
def init_driver(request):
    if request.param=="chrome":
        web_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    if request.param=="firefox":
        web_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    
    request.cls.driver = web_driver
    #web_driver.implicitly_wait(10)
    yield
    web_driver.close()
