from datetime import time
from time import sleep
from appium import webdriver
import unittest
from selenium.webdriver.common.action_chains import ActionChains
import time

class WaxApp(unittest.TestCase):
    def setUp(self):
        desired_caps = {}
        desired_caps['platformName']='Android'
        desired_caps['platformVersion']='9'
        desired_caps['deviceName']='<Enter your Mobile name>'
        desired_caps['deviceId']='<Enter your device Id>'
        desired_caps['noReset']='true'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)
        self.driver.start_activity("com.whatsapp", "HomeActivity");

        el = self.driver.find_elements_by_id('com.whatsapp:id/conversations_row_contact_name')
        for l in el:
            if l.text == "Alice":
                l.click()
                break

        element = self.driver.find_element_by_id("com.whatsapp:id/text_entry_layout")
        checks = ["00", "04", "08", "12", "16", "20", "24", "28"]
        check_item = 0
        code_len = 8
        char_codes = ['01010010', '11100011', '00011001']
        codes = 0
        t = time.localtime()
        current_time = time.strftime("%H:%M:%S", t)
        while(1):
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            while(current_time[6:] != checks[check_item]): 
                t = time.localtime()
                current_time = time.strftime("%H:%M:%S", t)
            print(char_codes[codes][check_item])
            if(char_codes[codes][check_item] == '1'): 
                actions.send_keys('X')
            actions.perform()
            check_item = (check_item + 1) % code_len 
            if check_item == 0:
                cpdes = (codes + 1) % len(char_codes)
                print("Start Sending...")
i = WaxApp()
i.setUp()
