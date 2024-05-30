import time

import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BaseClass:
    @pytest.fixture(scope="session")
    def browser(self):
        global driver
        option = webdriver.ChromeOptions()
        option.add_argument("--incognito")
        # option.add_argument("--headless")
        option.add_argument("--start-maximized")
        driver = webdriver.Chrome(options=option)
        # driver.get("https://kcbltest.ciihive.com/")
        # if browser_name == "chrome":
        #     option = webdriver.ChromeOptions()
        #     option.add_argument("--incognito")
        #     # option.add_argument("--headless")
        #     option.add_argument("--start-maximized")
        #     driver = webdriver.Chrome(options=option)
        #     driver.get("https://kcbltest.ciihive.com/")
        #
        # elif browser_name == "firefox":
        #     option = webdriver.FirefoxOptions()
        #     option.add_argument("--start-maximized")
        #     driver = webdriver.Firefox(options=option)
        #     driver.get("https://kcbltest.ciihive.com/")
        #
        # elif browser_name == "edge":
        #     option = webdriver.EdgeOptions()
        #     option.add_argument("--inprivate")
        #     option.add_argument("--start-maximized")
        #     driver = webdriver.Edge(options=option)
        #     driver.get("https://kcbltest.ciihive.com/")
        #
        # elif browser_name == "ie":
        #     option = webdriver.IeOptions()
        #     option.add_argument("--start-maximized")
        #     driver = webdriver.Ie(options=option)
        #     driver.get("https://kcbltest.ciihive.com/")
        #
        # else:
        #     driver = None
        yield driver
        driver.quit()

    def browser_driver(self):
        return driver

    # def browser_close(self):
    #     time.sleep(3)
    #     driver.quit()

    def click(self, locator):
        WebDriverWait(driver, 5).until(EC.element_to_be_clickable(locator)).click()

    def locate(self, locator):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
    def write(self, locator, text):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator)).send_keys(text)

    def clear(self, locator):
        WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator)).clear()

    def get_value(self, locator):
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
        return element.get_attribute("value")

    def get_text(self, locator):
        element = WebDriverWait(driver, 5).until(EC.presence_of_element_located(locator))
        return element.text

    def js_script(self, locator):
        driver.execute_script(locator)

    def current_url(self):
        return driver.current_url

    def implicit_wait(self, time):
        driver.implicitly_wait(time)

    # def explicit_wait(self, locator):
    #     WebDriverWait(driver, 5).until(EC.visibility_of_element_located(locator))

