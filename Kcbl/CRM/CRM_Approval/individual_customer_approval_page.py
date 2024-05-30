import time

from selenium.webdriver.common.by import By

from Kcbl.Base.BasePage import BaseClass


class IndividualCRMApprovalPage(BaseClass):
    def __init__(self):
        ################### Individual Customer Menu Locator ######################

        self.crm_locator = By.XPATH, "//app-menu/ul/li[2]/a"
        self.approval_locator = By.XPATH, "//app-menu/ul/li[2]/ul/li[3]/a"
        self.individual_locator = By.XPATH, "//app-menu/ul/li[2]/ul/li[3]/ul/li[1]/a"

        ############################### Individual Customer Form Locator ###############################

        #################### View List #####################

        self.view_button_locator = By.XPATH, "//table/tbody/tr[1]/td[8]/button"

        # Scroll down
        self.scroll_bottom_locator = "window.scrollTo(0,document.body.scrollHeight)"

        self.next_button_locator = By.XPATH, "//form/pe-steps/button[2]"

        self.accept_button_locator = By.ID, "accept_btn"
        self.reject_button_locator = By.ID, "reject_btn"
        self.close_button_locator = By.XPATH, "//form/pe-steps/div[2]/div[3]/div[4]/div/div/button"

        self.accept_popup_button_locator = By.XPATH, "//p-footer/button[1]"
        self.reject_popup_button_locator = By.XPATH, "//p-footer/button[1]"
        self.cancel_popup_button_locator = By.XPATH, "//p-footer/button[2]"

        self.status_locator = By.XPATH, "//table/tbody/tr[1]/td[5]"
        self.workflow_stage_locator = By.XPATH, "//table/tbody/tr[1]/td[6]"

        self.success_locator = By.XPATH, "/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div/div/div[1]"

    def crm_individual_customer_approval_step_with_accept(self):
        ################### Individual Customer Menu Operations ######################

        # self.click(self.crm_locator)
        # if run reject scenario than comment [self.click(self.approval_locator)] line
        self.click(self.approval_locator)
        self.click(self.individual_locator)

        #################### View List #####################

        self.click(self.view_button_locator)
        time.sleep(1)

        # Registration step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Address step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Identifier step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Document step
        self.js_script(self.scroll_bottom_locator)
        # time.sleep(1)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Spouse Detail step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Overview step
        self.js_script(self.scroll_bottom_locator)
        # Accept Button
        self.click(self.accept_button_locator)

        # Get Success Message
        success = self.get_text(self.success_locator)

        # status = self.get_text(self.status_locator)
        # workflow_stage = self.get_text(self.workflow_stage_locator)

        return success

    def crm_individual_customer_approval_step_with_reject(self):
        ################### Individual Customer Menu Operations ######################

        # self.click(self.crm_locator)
        self.click(self.approval_locator)
        time.sleep(3)
        self.click(self.individual_locator)

        #################### View List #####################

        self.click(self.view_button_locator)
        time.sleep(1)

        # Registration step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Address step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Identifier step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Document step
        self.js_script(self.scroll_bottom_locator)
        # time.sleep(1)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Spouse Detail step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Overview step
        self.js_script(self.scroll_bottom_locator)
        # Reject Button
        self.click(self.reject_button_locator)
        self.click(self.reject_popup_button_locator)

        status = self.get_text(self.status_locator)
        workflow_stage = self.get_text(self.workflow_stage_locator)

        return [status, workflow_stage]

    def crm_individual_customer_approval_step_with_save(self):
        #################### View List #####################

        self.click(self.view_button_locator)
        time.sleep(1)

        # Registration step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Address step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Identifier step
        self.js_script(self.scroll_bottom_locator)
        # time.sleep(1)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Document step
        self.js_script(self.scroll_bottom_locator)
        # time.sleep(1)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Spouse Detail step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        time.sleep(1)

        # Overview step
        self.js_script(self.scroll_bottom_locator)
        # Accept Button
        self.click(self.accept_button_locator)

        self.click(self.accept_popup_button_locator)
        # self.click(self.cancel_popup_button_locator)

        status = self.get_text(self.status_locator)
        workflow_stage = self.get_text(self.workflow_stage_locator)

        return [status, workflow_stage]
