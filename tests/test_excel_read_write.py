import openpyxl
from selenium.webdriver.common.by import By
from utilities import XLUtility
import pytest
import time


path = "C://Users/Welcome/PycharmProjects/ SeleniumProject/data.xlsx"
rows = XLUtility.getRowCount(path,'Sheet1')


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_search_bus_case(self):
        for r in range(2, rows + 1,):
            source_place = XLUtility.readData(path, "Sheet1", r, 1)
            time.sleep(3)
            source = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Source']")
            source.click()
            source.clear()
            source.send_keys(source_place)
            time.sleep(2)
            list_of_element = self.driver.find_element(By.XPATH, "//div[@id='downshift-1-menu']//div//li//span")
            # list_of_element.click()
            print("list of element", list_of_element.text)
            if list_of_element.text == 'Pune, Maharashtra':
                print('record found')
                list_of_element.click()
            elif list_of_element.text == 'Mumbai, Maharashtra':
                print("record found")
            des_place = XLUtility.readData(path, "Sheet1", r, 2)
            des = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Destination']")
            des.click()
            des.clear()
            des.send_keys(des_place)
            time.sleep(1)
            des_list = self.driver.find_element(By.XPATH, "//div[@id='downshift-2-menu']//div//li//span")
            print(des_list.text)
            print("list of element", des_list.text)
            if des_list.text == 'Nashik, Maharashtra':
                print('record found')
                des_list.click()
            elif des_list.text == 'Yeola, Maharashtra':
                print('record found')
                des_list.click()
            elif des_list.text == 'Mumbai, Maharashtra':
                print('record found')
                des_list.click()
            elif des_list.text == 'Kotamgaon, Maharashtra':
                print('record found')
                des_list.click()
            elif des_list.text == 'Kopargaon, Maharashtra':
                print('record found')
                des_list.click()
            elif des_list.text == 'Pune, Maharashtra':
                print('record found')
                des_list.click()
            elif des_list.text == 'Rahuri, Maharashtra':
                print('record found')
                des_list.click()
            elif des_list.text == 'Shirdi, Maharashtra':
                print('record found')
                des_list.click()

            time.sleep(10)
            # driver.find_element(By.XPATH,"//input[@placeholder='Pick a date']").send_keys("Oct 12, 2023")
            self.driver.find_element(By.XPATH, "//button[@data-testid='searchBusBtn']").click()
            time.sleep(10)

            if self.driver.title == 'Bus Booking - Online Bus Ticket Booking of all Bus types at best prices':
                print("test is passed")
                XLUtility.writeData(path,"Sheet1",r,3,"test passed")
            else:
                print("test is failed")
                XLUtility.writeData(path,"Sheet1",r,3,"test failed")
            self.driver.get("https://www.goibibo.com/")
            time.sleep(5)
            category = self.driver.find_element(By.XPATH, "/html/body/div/div[1]/div/header/ul/li[5]/a/p")
            category.click()
            time.sleep(3)