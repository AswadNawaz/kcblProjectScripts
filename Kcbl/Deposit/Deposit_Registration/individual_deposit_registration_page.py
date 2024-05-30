from selenium.webdriver.common.by import By

from Kcbl.Base.BasePage import BaseClass


class IndividualDepositRegistrationPage(BaseClass):
    def __init__(self, product):
        ################### Individual Deposit Menu Locator ######################

        self.deposit_locator = By.XPATH, "//app-menu/ul/li[4]/a"
        self.operation_locator = By.XPATH, "//app-menu/ul/li[4]/ul/li[1]/a"
        self.openAccount_locator = By.XPATH, "//app-menu/ul/li[4]/ul/li[1]/ul/li[1]/a"
        self.individual_locator = By.XPATH, "//app-menu/ul/li[4]/ul/li[1]/ul/li[1]/ul/li[1]/a"

        ############################### Individual Deposit Form Locator #############################

        #################### Step 1: Registration #####################

        self.enable_button_locator = By.XPATH, "//form/pe-steps/p-toolbar/div/div/div[2]/button[1]"
        self.product_locator = By.ID, "DMP_PRODCODE"
        self.product_selection_locator = By.XPATH, "//*[@id='DMP_PRODCODE']//ul/p-dropdownitem[" + product + "]/li"
        self.customerNumber_locator = By.XPATH, "//*[@id='CMP_CUSTCODEundefined']//input"
        self.customerName_locator = By.XPATH, "//*[@id='CMP_NAMEundefined']//input"
        self.title_locator = By.XPATH, "//*[@id='MBM_BKMSTITLEundefined']//input"
        self.identificationType_locator = By.ID, "PIT_IDENCODE"
        self.identificationNumber_locator = By.XPATH, "//*[@id='PIT_IDENVALUEundefined']//input"
        self.accountPurpose_locator = By.ID, "ACC_PURPOSE"
        self.accountPurpose_selection_locator = By.XPATH, "//*[@id='ACC_PURPOSE']//ul/p-dropdownitem[1]/li"
        self.creditOfficer_locator = By.ID, "PCD_CORDCODE"
        self.creditOfficer_selection_locator = By.XPATH, "//*[@id='PCD_CORDCODE']//ul/p-dropdownitem[1]/li"
        self.accountNature_locator = By.ID, "ANR_ACNRCODE"
        self.accountNature_selection_locator = By.XPATH, "//*[@id='ANR_ACNRCODE']//ul/p-dropdownitem[2]/li"
        self.accountNature1_locator = By.ID, "AccountNature"
        self.accountNature1_selection_locator = By.XPATH, "//*[@id='AccountNature']//ul/p-dropdownitem[1]/li"

        # Scroll down
        self.scroll_bottom_locator = "window.scrollTo(0,document.body.scrollHeight)"

        self.next_button_locator = By.XPATH, "//form/pe-steps/button[2]"

        #################### Step 2: Documents #####################

        self.document_type_locator = By.ID, "PDT_DOTYCODE"
        self.document_type_selection_locator = By.XPATH, "//*[@id='PDT_DOTYCODE']//ul/p-dropdownitem[1]/li"
        self.documentDescription_locator = By.XPATH, "//*[@id='BDO_DOCUMENTDESC0']//input"
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
        self.extra_click_locator = By.XPATH, "//form/pe-steps/div[2]/pe-step[2]/div[1]/div/dynamic-form"

        ######## 2nd

        self.document_add_button_locator = By.XPATH, "//form/pe-steps/div[2]/pe-step[2]/div[2]/div[2]/button"
        self.document_type_2_locator = By.XPATH, "//form/pe-steps/div[2]/pe-step[2]/div[2]/div/dynamic-form/div/div/p-card/div/div/div[2]/div/div[1]/div[2]/p-dropdown/div/span"
        self.document_type_selection_2_locator = By.XPATH, "//*[@id='PDT_DOTYCODE1']//ul/p-dropdownitem[2]/li"
        self.document_upload_image_2_locator = By.XPATH, "//*[@id='BDO_DOCUMENTFILE1']//input"
        self.document_upload_button_2_locator = By.XPATH, "//*[@id='BDO_DOCUMENTFILE1']//p-button[1]/button"

        #################### Step 3: Relations #####################

        self.introducerCustomer_locator = By.XPATH, "//*[@id='CMP_INTRODUCERCUSTCODEundefined']//input"

        #################### Step 3: Overview #####################

        self.save_button_locator = By.ID, "accept_btn"

        self.accept_button_locator = By.XPATH, "//p-footer/button[1]"

        self.success_locator = By.XPATH, "/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div/div/div[1]"

        self.success_close_locator = By.XPATH, "/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div/button/span"

    def deposit_menu(self):
        ################### Individual Deposit Menu Operations ######################

        self.click(self.deposit_locator)
        self.click(self.operation_locator)
        self.click(self.openAccount_locator)
        self.click(self.individual_locator)

    def deposit_individual_registration_step(self, customer_number, title):

        ################### Individual Depsoit Form ######################

        #################### Step 1: Registration #####################

        self.click(self.enable_button_locator)

        self.click(self.product_locator)
        self.click(self.product_selection_locator)
        self.write(self.customerNumber_locator, customer_number)
        name = self.get_value(self.customerName_locator)
        self.write(self.title_locator, title)
        type = self.get_value(self.identificationType_locator)
        identification_number = self.get_value(self.identificationNumber_locator)
        self.click(self.accountPurpose_locator)
        self.click(self.accountPurpose_selection_locator)
        self.click(self.creditOfficer_locator)
        self.click(self.creditOfficer_selection_locator)
        self.click(self.accountNature_locator)
        self.click(self.accountNature_selection_locator)
        self.click(self.accountNature1_locator)
        self.click(self.accountNature1_selection_locator)

        self.js_script(self.scroll_bottom_locator)

        self.click(self.next_button_locator)

    def deposit_individual_documents_step(self, description, document_upload_image):
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
        self.click(self.extra_click_locator)
        self.click(self.document_add_button_locator)

        self.js_script(self.scroll_bottom_locator)

        self.click(self.document_type_2_locator)
        self.click(self.document_type_selection_2_locator)
        self.write(self.document_upload_image_2_locator, document_upload_image)
        self.click(self.document_upload_button_2_locator)
        self.click(self.extra_click_locator)

        self.js_script(self.scroll_bottom_locator)


        self.click(self.next_button_locator)

    def deposit_individual_relations_step(self, customer_number):
        #################### Step 4: Relations #####################

        self.write(self.introducerCustomer_locator, customer_number)

        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        # Overview
        self.js_script(self.scroll_bottom_locator)

        self.click(self.save_button_locator)
        self.click(self.accept_button_locator)
        success = self.get_text(self.success_locator)
        self.click(self.success_close_locator)

        return success
