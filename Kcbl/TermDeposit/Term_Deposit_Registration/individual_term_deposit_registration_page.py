from selenium.webdriver.common.by import By

from Kcbl.Base.BasePage import BaseClass


class IndividualTermDepositRegistrationPage(BaseClass):
    def __init__(self, product, roll_over):
        ################### Individual Term Deposit Menu Locator ######################

        self.termDeposit_locator = By.XPATH, "//app-menu/ul/li[5]/a"
        self.operation_locator = By.XPATH, "//app-menu/ul/li[5]/ul/li[1]/a"
        self.registration_locator = By.XPATH, "//app-menu/ul/li[5]/ul/li[1]/ul/li/a"
        self.individual_locator = By.XPATH, "//app-menu/ul/li[5]/ul/li[1]/ul/li/ul/li[1]/a"

        ############################### Individual Term Deposit Form Locator ###############################

        #################### Step 1: Registration #####################

        self.enable_button_locator = By.XPATH, "//form/pe-steps/p-toolbar/div/div/div[2]/button[1]"
        self.product_locator = By.ID, "DMP_PRODCODE"
        self.product_selection_locator = By.XPATH, "//*[@id='DMP_PRODCODE']//ul/p-dropdownitem[" + product + "]/li"
        self.customerNumber_locator = By.XPATH, "//*[@id='CMP_CUSTCODEundefined']//input"
        self.customerName_locator = By.XPATH, "//*[@id='CMP_NAMEundefined']//input"
        self.title_locator = By.XPATH, "//*[@id='MBM_BKMSTITLEundefined']//input"
        self.identificationType_locator = By.ID, "PIT_IDENCODE"
        self.identificationNumber_locator = By.XPATH, "//*[@id='PIT_IDENVALUEundefined']//input"
        self.accountNature_locator = By.ID, "ANR_ACNRCODE"
        self.accountNature_selection_locator = By.XPATH, "//*[@id='ANR_ACNRCODE']//ul/p-dropdownitem[2]/li"
        self.creditOfficer_locator = By.ID, "PCD_CORDCODE"
        self.creditOfficer_selection_locator = By.XPATH, "//*[@id='PCD_CORDCODE']//ul/p-dropdownitem[1]/li"

        # Scroll down
        self.scroll_bottom_locator = "window.scrollTo(0,document.body.scrollHeight)"

        self.next_button_locator = By.XPATH, "//form/pe-steps/button[2]"

        #################### Step 2: Booking #####################

        self.duration_locator = By.XPATH, "//*[@id='BTA_DURATIONundefined']//input"
        self.rollOver_locator = By.ID, "PRO_RLOVCODE"
        self.rollOver_selection_locator = By.XPATH, "//*[@id='PRO_RLOVCODE']//ul/p-dropdownitem[" + roll_over + "]/li"
        self.bookingAmount_locator = By.XPATH, "//*[@id='BTA_BOOKINGAMOUNTundefined']//input"
        self.commentDate_locator = By.XPATH, "//*[@id='BN_MS_TA_COMMENTSundefined']/tr[2]/td[1]/p-calendar/span/input"
        self.date_locator = By.XPATH, ("//*[@id='BN_MS_TA_COMMENTSundefined']/tr[2]/td[1]/p-calendar/span/div/div["
                                       "2]/button[1]/span")
        self.comment_locator = By.XPATH, "//*[@id='BN_MS_TA_COMMENTSundefined']/tr[2]/td[2]/input"

        #################### Step 3: Correlation #####################

        self.correlationAccount_locator = By.XPATH, "//*[@id='MBM_BKMSNUMBER_REFundefined']//input"

        #################### Step 4: Documents #####################

        self.document_type_locator = By.ID, "PDT_DOTYCODE"
        self.document_type_selection_locator = By.XPATH, "//*[@id='PDT_DOTYCODE']//ul/p-dropdownitem[1]/li"
        self.documentDescription_locator = By.XPATH, "//*[@id='BDO__DOCUMENTDESC0']//input"
        self.document_doi_locator = By.XPATH, "//*[@id='PDT_DOTYISSUEDATE0']/div[2]/p-calendar/span"
        self.document_doi_month_locator = By.XPATH, "//*[@id='PDT_DOTYISSUEDATE0']//select[1]/option[7]"
        self.document_doi_year_locator = By.XPATH, "//*[@id='PDT_DOTYISSUEDATE0']//select[2]/option[114]"
        self.document_doi_day_locator = By.XPATH, "//*[@id='PDT_DOTYISSUEDATE0']//table/tbody/tr[4]/td[4]/span"
        self.document_doe_locator = By.XPATH, "//*[@id='PDT_DOTYEXPIRYDATE0']/div[2]/p-calendar/span"
        self.document_doe_month_locator = By.XPATH, "//*[@id='PDT_DOTYEXPIRYDATE0']//select[1]/option[7]"
        self.document_doe_year_locator = By.XPATH, "//*[@id='PDT_DOTYEXPIRYDATE0']//select[2]/option[117]"
        self.document_doe_day_locator = By.XPATH, "//*[@id='PDT_DOTYEXPIRYDATE0']//table/tbody/tr[4]/td[4]/span"
        self.document_upload_image_locator = By.XPATH, "//*[@id='BDO_DOCUMENTFILE0']//input"
        self.document_upload_button_locator = By.XPATH, "//*[@id='BDO_DOCUMENTFILE0']//p-button[1]/button"

        #################### Step 5: Profit #####################

        self.interestType_locator = By.XPATH, "//*[@id='PTM_TMETDESCundefined']//input"
        self.rate_locator = By.XPATH, "//*[@id='PLC_CHARGECALCRATEundefined']//input"

        #################### Step 3: Overview #####################

        self.save_button_locator = By.ID, "accept_btn"

        self.accept_button_locator = By.XPATH, "//p-footer/button[1]"

        self.success_locator = By.XPATH, "/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div/div/div[1]"

        self.success_close_locator = By.XPATH, "/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div/button/span"

    def term_deposit_menu(self):
        ################### Individual Term Deposit Menu Operations ######################

        self.click(self.termDeposit_locator)
        self.click(self.operation_locator)
        self.click(self.registration_locator)
        self.click(self.individual_locator)

    def term_deposit_individual_registration_step(self, customer_number, title, loop_number):

        ################### Individual Term Deposit Form ######################

        #################### Step 1: Registration #####################

        if loop_number == 0:
            self.click(self.enable_button_locator)

        self.click(self.product_locator)
        self.click(self.product_selection_locator)
        self.write(self.customerNumber_locator, customer_number)
        name = self.get_value(self.customerName_locator)
        self.write(self.title_locator, title)
        type = self.get_value(self.identificationType_locator)
        identification_number = self.get_value(self.identificationNumber_locator)
        self.click(self.accountNature_locator)
        self.click(self.accountNature_selection_locator)
        self.click(self.creditOfficer_locator)
        self.click(self.creditOfficer_selection_locator)

        self.js_script(self.scroll_bottom_locator)

        self.click(self.next_button_locator)

    def term_deposit_individual_booking_step(self, duration, booking_amount, comment):
        #################### Step 2: Booking #####################

        self.write(self.duration_locator, duration)
        self.click(self.rollOver_locator)
        self.click(self.rollOver_selection_locator)
        self.write(self.bookingAmount_locator, booking_amount)

        ### Comment
        self.click(self.commentDate_locator)
        self.click(self.date_locator)
        self.write(self.comment_locator, comment)

        self.click(self.next_button_locator)

    def term_deposit_individual_correlation_step(self, deposit_account):
        #################### Step 3: Correlation #####################

        self.write(self.correlationAccount_locator, deposit_account)

        self.click(self.next_button_locator)
        self.click(self.next_button_locator)

    def term_deposit_individual_documents_step(self, description, document_upload_image):
        #################### Step 4: Documents #####################

        self.click(self.document_type_locator)
        self.click(self.document_type_selection_locator)
        self.write(self.documentDescription_locator, description)
        self.click(self.document_doi_locator)
        self.click(self.document_doi_month_locator)
        self.click(self.document_doi_year_locator)
        self.click(self.document_doi_day_locator)
        self.click(self.document_doe_locator)
        self.click(self.document_doe_month_locator)
        self.click(self.document_doe_year_locator)
        self.click(self.document_doe_day_locator)
        self.write(self.document_upload_image_locator, document_upload_image)
        self.click(self.document_upload_button_locator)

        self.click(self.next_button_locator)
        self.click(self.next_button_locator)

    def term_deposit_individual_profit_step(self):
        #################### Step 5: Profit #####################

        interest_type = self.get_value(self.interestType_locator)
        rate = self.get_value(self.rate_locator)

        # self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)

        return [interest_type, rate]

    def term_deposit_individual_overview_step(self):
        # Overview
        self.js_script(self.scroll_bottom_locator)

        self.click(self.save_button_locator)
        self.click(self.accept_button_locator)
        success = self.get_text(self.success_locator)
        self.click(self.success_close_locator)

        return success
