from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_google():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.google.com")
    assert driver.title=="Google"
    driver.quit()

def test_facebook():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.facebook.com")
    assert driver.title=="Facebook – log in or sign up"
    driver.quit()

def test_instagram():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.instagram.com")
    assert driver.title=="Instagram"
    driver.quit()
    
def test_gmail():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.gmail.com")
    assert driver.title=="Gmail"
    driver.quit()

def test_rediff():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)
    driver.get("http://www.rediff.com")
    assert driver.title=="Rediff.com: News | Rediffmail | Stock Quotes | Rediff Gurus"
    driver.quit()