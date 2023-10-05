import time
import pytest
from selenium.webdriver.common.by import By



@pytest.mark.usefixtures("setup_and_teardown")
class Testsort:
    def test_sort_seat(self):
        source = self.driver.find_element(By.XPATH, "//input[@placeholder='Enter Source']")
        source.click()
        time.sleep(2)
        source.send_keys("Pune")
        time.sleep(2)
        list_of_element = self.driver.find_element(By.XPATH, "//div[@id='downshift-1-menu']//div//li//span")
        # list_of_element.click()

        print("list of element", list_of_element.text)
        if list_of_element.text == 'Pune, Maharashtra':
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
        order = self.driver.find_element(By.XPATH,"//span[@data-val='high_price']")
        order.click()
        time.sleep(5)
        select_bus = self.driver.find_element(By.XPATH," //div//p[text()='Mahakali Travels']")
        select_bus.click()
        select_seat = self.driver.find_element(By.XPATH,"//button[@class='Button-sc-110xfhu-4 jcHJWt']//span[@class='SrpActiveCardstyles__PayTxtSpan-sc-yk1110-32 dPUgol']")
        select_seat.click()
        boarding_point = self.driver.find_element(By.CLASS_NAME, "RadioButtonstyles__RadioInput-sc-wz601o-2 gbafxd")
        boarding_point.click()
#        for i in boarding_point.text:
#            if boarding_point.text == 'Wakdewadi New Bus Stand':
#                print(boarding_point.text)
#                boarding_point.text.click()
        dropping_point = self.driver.find_element(By.XPATH,"//div//p[@class='location'][text()='Nashik Road Near Pawan Hotel Bitco Point']")
        dropping_point.text.click()


        list_of_seat = self.driver.find_element(By.XPATH,"//span[@class='tooltipTxt']//span[@class='seatNum']")

        print(list_of_seat.text)
        for i in list_of_seat.text:
            if list_of_seat.text == '10':
                list_of_seat.click()
                print("seat selected")

