import pytest
from selenium.webdriver.common.by import By
import time


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_bus_case_one(self):
        source = self.driver.find_element(By.XPATH,"//input[@placeholder='Enter Source']")
        source.click()
        time.sleep(2)
        source.send_keys("Pune")
        time.sleep(2)
        list_of_element = self.driver.find_element(By.XPATH,"//div[@id='downshift-1-menu']//div//li//span")
        #list_of_element.click()

        print("list of element",list_of_element.text)
        if list_of_element.text == 'Pune, Maharashtra':
            print('record found')
            list_of_element.click()

        des = self.driver.find_element(By.XPATH,"//input[@placeholder='Enter Destination']")
        des.click()
        time.sleep(2)
        des.send_keys("Nashik")
        time.sleep(2)
        des_list = self.driver.find_element(By.XPATH,"//div[@id='downshift-2-menu']//div//li//span")
        print(des_list.text)

        print("list of element", des_list.text)
        if des_list.text == 'Nashik, Maharashtra':
            print('record found')
            des_list.click()

        time.sleep(10)
        #driver.find_element(By.XPATH,"//input[@placeholder='Pick a date']").send_keys("Oct 12, 2023")
        self.driver.find_element(By.XPATH,"//button[@data-testid='searchBusBtn']").click()
        time.sleep(10)

    def test_search_bus_case_two(self):
        source = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Source']")
        source.click()
        time.sleep(2)
        source.send_keys("Mumbai")
        time.sleep(2)
        list_of_element = self.driver.find_element(By.XPATH, "//div[@id='downshift-1-menu']//div//li//span")
        # list_of_element.click()

        print("list of element", list_of_element.text)
        if list_of_element.text == 'Mumbai, Maharashtra':
            print('record found')
            list_of_element.click()

        des = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Destination']")
        des.click()
        time.sleep(2)
        des.send_keys("Nashik")
        time.sleep(2)
        des_list = self.driver.find_element(By.XPATH, "//div[@id='downshift-2-menu']//div//li//span")
        print(des_list.text)

        print("list of element", des_list.text)
        if des_list.text == 'Nashik, Maharashtra':
            print('record found')
            des_list.click()

        time.sleep(10)
        # driver.find_element(By.XPATH,"//input[@placeholder='Pick a date']").send_keys("Oct 12, 2023")
        self.driver.find_element(By.XPATH, "//button[@data-testid='searchBusBtn']").click()
        time.sleep(10)

        # li_dt = driver.find_element(By.XPATH, "//ul[@class='dcalendarstyles__DateWrapDiv-sc-r2jz2t-7 gJsKZe']/li[@style='color: black;']/span")
        # li_dt.click()
        # print("date is", li_dt.)
        # if li_dt.text == '10':
        #    print("date is correct")
        #    li_dt.click()

    def test_inavlid_search_bus(self):
        source = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Source']")
        source.click()
        time.sleep(2)
        source.send_keys("coat")
        time.sleep(2)
        list_of_element = self.driver.find_element(By.XPATH, "//div[@id='downshift-1-menu']//div//li//span")

        print("list of element", list_of_element.text)
        if list_of_element.text == 'Pune, Maharashtra':
            print('record found')
            list_of_element.click()
        else:
            print("no record found")