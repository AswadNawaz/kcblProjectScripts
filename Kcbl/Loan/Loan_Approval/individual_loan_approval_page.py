import time

from selenium.webdriver.common.by import By

from Kcbl.Base.BasePage import BaseClass


class IndividualLoanApprovalPage(BaseClass):
    def __init__(self):
        ################### Individual Loan Menu Locator ######################

        self.loan_locator = By.XPATH, "//app-menu/ul/li[2]/a"
        self.approval_locator = By.XPATH, "//app-menu/ul/li[2]/ul/li[2]/a"
        self.individual_locator = By.XPATH, "//app-menu/ul/li[2]/ul/li[2]/ul/li[1]/a"

        ############################### Individual Loan Form Locator ###############################

        #################### View List #####################

        self.view_button_locator = By.XPATH, "//*[@id='mbl-text-brk']/button"

        # Scroll down
        self.scroll_bottom_locator = "window.scrollTo(0,document.body.scrollHeight)"

        self.next_button_locator = By.XPATH, "//form/pe-steps/button[2]"

        self.vote_1_yes_locator = By.XPATH, ("//*[@id='BN_MS_LC_LOANCOMMITTEEundefined']/tr[2]/td[4]/div/div["
                                             "1]/custom-radiobutton/label")
        self.vote_2_yes_locator = By.XPATH, ("//*[@id='BN_MS_LC_LOANCOMMITTEEundefined']/tr[3]/td[4]/div/div["
                                             "1]/custom-radiobutton/label")

        self.accept_button_locator = By.ID, "accept_btn"
        self.reject_button_locator = By.ID, "reject_btn"
        self.close_button_locator = By.XPATH, "//form/pe-steps/div[2]/div[3]/div[4]/div/div/button"

        self.accept_popup_button_locator = By.XPATH, "//p-footer/button[1]"
        self.reject_popup_button_locator = By.XPATH, "//p-footer/button[1]"

        self.status_locator = By.XPATH, "//table/tbody/tr[1]/td[5]"
        self.workflow_stage_locator = By.XPATH, "//table/tbody/tr[1]/td[6]"

        self.success_locator = By.XPATH, "/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div/div/div[1]"

        self.success_close_locator = By.XPATH, ("/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div"
                                                "/button/span")

    def loan_individual_approval_with_accept(self):
        ################### Individual Loan Menu Operations ######################

        self.click(self.loan_locator)
        # if run reject scenario than comment [self.click(self.approval_locator)] line
        self.click(self.approval_locator)
        self.click(self.individual_locator)

        #################### View List #####################

        self.click(self.view_button_locator)
        time.sleep(3)

        # Registration step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Social Activity step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Cash Flow step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Document step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Guarantors step
        # self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Correlation step
        # self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(3)

        # Loan Details step
        self.js_script(self.scroll_bottom_locator)
        # element_state = nobtn.get_attribute("disabled")
        vote_1 = self.get_attribute(self.vote_1_yes_locator, "p-disabled")
        vote_2 = self.get_attribute(self.vote_2_yes_locator, "p-disabled")

        self.click(self.vote_1_yes_locator)
        self.click(self.vote_2_yes_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Collateral step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Checklist step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Overview step
        self.js_script(self.scroll_bottom_locator)
        # Accept Button
        self.click(self.accept_button_locator)
        self.click(self.accept_popup_button_locator)

        # Get Success Message
        success = self.get_text(self.success_locator)

        # status = self.get_text(self.status_locator)
        # workflow_stage = self.get_text(self.workflow_stage_locator)

        self.click(self.success_close_locator)

        return success
