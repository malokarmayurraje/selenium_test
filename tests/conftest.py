import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities import ReadConfigurations


@pytest.fixture()
def setup_and_teardown(request):
    #browser = ReadConfigurations.read_configuration("basic info","browser")
    driver = webdriver.Chrome()
    driver.maximize_window()
    #url = ReadConfigurations.read_configuration("basic info","url")
    driver.get("https://www.goibibo.com/")
    time.sleep(5)
    driver.find_element(By.XPATH, "//div[@data-id='auth-flow-section']//span[@class='logSprite icClose']").click()
    category = driver.find_element(By.XPATH, "/html/body/div/div[1]/div/header/ul/li[5]/a/p")
    category.click()
    request.cls.driver = driver
    yield
    driver.quit()