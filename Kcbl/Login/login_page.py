from selenium.webdriver.common.by import By

from Kcbl.Base.BasePage import BaseClass

class LoginPage(BaseClass):
    def __init__(self):
        self.driver = self.browser_driver()
        self.organization_locator = By.ID, "clientid"
        self.username_locator = By.ID, "username"
        self.password_locator = By.ID, "password"
        self.login_locator = By.XPATH, "//form/div[5]/div/button"
        self.logout_locator = By.XPATH, "//app-topbar/div/div[2]/div/ul/li[2]/a"
        self.logout_button_locator = By.XPATH, "//app-topbar/div/div[2]/div[2]/ul/li[2]/ul/li/a[2]"
        self.logout_success_locator = By.XPATH, "//form/p-toast//div[2]"

    def login_with_valid_credentials(self, url, organization, username, password):
        self.driver.get(url)
        self.write(self.organization_locator, organization)
        self.write(self.username_locator, username)
        self.write(self.password_locator, password)
        self.click(self.login_locator)
        # Get the title of the current page
        actual_title = self.driver.title
        # self.implicit_wait(5)
        return actual_title

    def logout(self):
        self.click(self.logout_locator)
        self.click(self.logout_button_locator)
        actual_success_message = self.get_text(self.logout_success_locator)
        return actual_success_message
