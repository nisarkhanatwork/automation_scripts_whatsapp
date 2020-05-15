from datetime import time
from time import sleep

from appium import webdriver
import unittest
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
            if l.text == "Bob":
                l.click()
                break

        iters = 1
        while_iter = 1
        start, end = 0, 0
        checks = ["02", "06", "10", "14", "18", "22", "26", "30"]
        while(1):
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            if current_time[6:] == "00":
                print("Low Bandwidth Test Of Steganography Channel")
                print("Start receiving: ", current_time)
                code_len = 8
                check_item = 0
                while(code_len):
                    while(current_time[6:] != checks[check_item]):
                        t = time.localtime()
                        current_time = time.strftime("%H:%M:%S", t)

                    el = self.driver.find_elements_by_id("com.whatsapp:id/conversation_contact_status")
                    for l in el:
                        if l.text[:6] == "typing":
                            print(" 1 ")
                        else: 
                            print(" 0 ")
                        
                        check_item = check_item + 1
                        code_len = code_len - 1
i = WaxApp()
i.setUp()
