from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

import pytest

@pytest.fixture(scope='class')
def init_chrome_driver(request):
    ch_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    request.cls.driver = ch_driver
    yield
    ch_driver.quit()

@pytest.fixture(scope='class')
def init_ff_driver(request):
    ff_driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = ff_driver
    yield
    ff_driver.quit()
    
@pytest.mark.usefixtures("init_chrome_driver")
class Base_Chrome_Test:
    pass

class Test_Google_Chrome(Base_Chrome_Test):
    def test_google_title_chrome(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title=="Google"


@pytest.mark.usefixtures("init_ff_driver")
class Base_Firefox_Test:
    pass

class Test_Google_Firefox(Base_Firefox_Test):
    def test_google_title_firefox(self):
        self.driver.get("http://www.google.com")
        assert self.driver.title=="Google"
