import time

from selenium.webdriver.common.by import By

from Kcbl.Base.BasePage import BaseClass


class IndividualLoanRegistrationPage(BaseClass):
    def __init__(self, product, frequency):
        ################### Individual Loan Menu Locator ######################

        self.loan_locator = By.XPATH, "//app-menu/ul/li[3]/a"
        self.operation_locator = By.XPATH, "//app-menu/ul/li[3]/ul/li[1]/a"
        self.application_locator = By.XPATH, "//app-menu/ul/li[3]/ul/li[1]/ul/li[1]/a"
        self.individual_locator = By.XPATH, "//app-menu/ul/li[3]/ul/li[1]/ul/li[1]/ul/li[1]/a/span[1]"

        ############################### Individual Loan Form Locator ###############################

        #################### Step 1: Registration #####################

        self.enable_button_locator = By.XPATH, "//form/pe-steps/p-toolbar/div/div/div[2]/button[1]"
        self.product_locator = By.ID, "DMP_PRODCODE"
        self.product_selection_locator = By.XPATH, "//*[@id='DMP_PRODCODE']//ul/p-dropdownitem[" + product + "]/li"
        self.classification_individual_locator = By.XPATH, "//label[text()='Individual']"
        self.classification_business_locator = By.XPATH, "//label[text()='Business']"
        self.customerNumber_locator = By.XPATH, "//*[@id='CMP_CUSTCODEundefined']//input"
        self.title_locator = By.XPATH, "//*[@id='MBM_BKMSTITLEundefined']//input"
        self.sourceOfFunds_locator = By.ID, "PFS_FUSOID"
        self.sourceOfFunds_selection_locator = By.XPATH, "//*[@id='PFS_FUSOID']//ul/p-dropdownitem/li/span"
        self.mainPurpose_locator = By.ID, "PPO_MAINPURPOSE"
        self.mainPurpose_selection_locator = By.XPATH, "//*[@id='PPO_MAINPURPOSE']//ul/p-dropdownitem[1]/li/span"

        # Scroll down by 500 pixels
        self.scroll_500_pixel_locator = "window.scrollBy(0, 500);"

        self.groupPurpose_locator = By.ID, "PPO_GRPPURPOSE"
        self.groupPurpose_selection_locator = By.XPATH, "//*[@id='PPO_GRPPURPOSE']//ul/p-dropdownitem[1]/li"
        self.detailPurpose_locator = By.ID, "PPO_PURPCODE"
        self.detailPurpose_selection_locator = By.XPATH, "//*[@id='PPO_PURPCODE']//ul/p-dropdownitem[1]/li"
        self.creditOfficer_locator = By.ID, "PCD_CORDCODE"
        self.creditOfficer_selection_locator = By.XPATH, "//*[@id='PCD_CORDCODE']//ul/p-dropdownitem[1]/li"
        # Business Since Date
        self.business_dos_locator = By.XPATH, "//*[@id='DBS_DATEundefined']/div[2]/p-calendar/span"
        self.business_dos_month_locator = By.XPATH, "//*[@id='DBS_DATEundefined']//select[1]/option[7]"
        self.business_dos_year_locator = By.XPATH, "//*[@id='DBS_DATEundefined']//select[2]/option[114]"
        self.business_dos_day_locator = By.XPATH, "//*[@id='DBS_DATEundefined']//table/tbody/tr[4]/td[4]/span"

        self.supplier_pm_button_locator = By.XPATH, "//*[@id='SUPP_PAYMENT_METHODundefined']//input"
        self.salesFrequency_locator = By.ID, "SALESFREQ"
        self.salesFrequency_selection_locator = By.XPATH, "//*[@id='SALESFREQ']//ul/p-dropdownitem[4]/li"
        self.customer_pm_button_locator = By.XPATH, "//*[@id='CMP_PAYMENT_METHundefined']//input"
        self.workCategory_locator = By.ID, "WORK_CATECODE"
        self.workCategory_selection_locator = By.XPATH, "//*[@id='WORK_CATECODE']//ul/p-dropdownitem[3]/li/span"

        # Scroll down
        self.scroll_bottom_locator = "window.scrollTo(0,document.body.scrollHeight)"

        self.next_button_locator = By.XPATH, "//form/pe-steps/button[2]"

        ######################### Step 3: Cash Flow ########################
        # Financial Income
        self.income_code_locator = By.ID, "PIT_TYPECODE"
        self.income_code_selection_locator = By.XPATH, "//*[@id='PIT_TYPECODE']//ul/p-dropdownitem[1]/li"
        self.income_frequency_locator = By.ID, "BFI_FMODCODE"
        self.income_frequency_selection_locator = By.XPATH, "//*[@id='BFI_FMODCODE']//ul/p-dropdownitem[3]/li"
        self.income_currency_locator = By.ID, "BFI_CURRCODE"
        self.income_currency_selection_locator = By.XPATH, "//*[@id='BFI_CURRCODE']//ul/p-dropdownitem[1]/li"
        self.income_amount_locator = By.XPATH, "//*[@id='BN_MS_FI_FINANCIALINCOMEundefined']/tr[2]/td[5]//input"

        # Scroll down by 1800 pixels
        self.scroll_1500_pixel_locator = "window.scrollBy(0, 1500);"

        # Financial Expense
        self.expense_code_locator = By.ID, "PET_EXPENSECODE"
        self.expense_code_selection_locator = By.XPATH, "//*[@id='PET_EXPENSECODE']//ul/p-dropdownitem[1]/li"
        self.expense_frequency_locator = By.ID, "BFE_FMODCODE"
        self.expense_frequency_selection_locator = By.XPATH, "//*[@id='BFE_FMODCODE']//ul/p-dropdownitem[3]/li"
        self.expense_currency_locator = By.ID, "BFE_CURRCODE"
        self.expense_currency_selection_locator = By.XPATH, "//*[@id='BFE_CURRCODE']//ul/p-dropdownitem[1]/li"
        self.expense_amount_locator = By.XPATH, "//*[@id='BN_MS_FE_FINANCIALEXPENSEundefined']/tr[2]/td[5]//input"

        # Actual Activity Expense
        self.type_locator = By.ID, "PET_LAEXPENSECODE"
        self.type_selection_locator = By.XPATH, "//*[@id='PET_LAEXPENSECODE']//ul/p-dropdownitem[1]/li"
        self.currency_locator = By.ID, "LAE_CURRCODE"
        self.currency_selection_locator = By.XPATH, "//*[@id='LAE_CURRCODE']//ul/p-dropdownitem[1]/li"
        self.value_locator = By.XPATH, "//*[@id='loanActivityExpenseundefined']/tr[2]/td[4]//input"

        #################### Step 4: Documents #####################

        self.document_type_locator = By.ID, "PDT_DOTYCODE"
        self.document_type_selection_locator = By.XPATH, "//*[@id='PDT_DOTYCODE']//ul/p-dropdownitem[1]/li/span"
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

        #################### Step 5: Guarantor #####################

        self.guarantorCustomer_locator = By.XPATH, "//*[@id='BN_MS_LG_LOANGUARANTORundefined']/tr[2]/td[1]/input"

        #################### Step 6: Correlation #####################

        self.correlationAccount_locator = By.XPATH, "//*[@id='MBM_BKMSNUMBER_REFundefined']//input"

        #################### Step 7: Loan Details #####################

        self.appliedAmount_locator = By.XPATH, "//*[@id='BLA_LNAPPLIEDAMOUNTFCundefined']//input"
        self.interestRate_locator = By.XPATH, "//*[@id='BLA_LNACINTERESTRATEundefined']//input"
        self.effectiveDate_locator = By.XPATH, "//*[@id='BLA_LNACEFFECTIVEDATEundefined']//span"
        # effective date change by tr[]/td[] according to disbursement date
        self.effectiveDay_locator = By.XPATH, "//*[@id='BLA_LNACEFFECTIVEDATEundefined']//table/tbody/tr[5]/td[6]/span"
        self.paymentFrequency_locator = By.ID, "PFM_FMODCODE"
        self.paymentFrequency_selection_locator = By.XPATH, "//*[@id='PFM_FMODCODE']//ul/p-dropdownitem[" + frequency + "]/li"
        self.duration_locator = By.XPATH, "//*[@id='BLA_LNACTOTALDURATIONundefined']//input"
        self.generate_button_locator = By.ID, "generateSchedule"
        self.clear_button_locator = By.ID, "clearValues"

        #################### Step 3: Overview #####################

        self.save_button_locator = By.ID, "accept_btn"

        self.accept_button_locator = By.XPATH, "//p-footer/button[1]"

        self.success_locator = By.XPATH, "/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div/div/div[1]"

        self.success_close_locator = By.XPATH, "/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div/button/span"

    def loan_individual_registration_step(self, customer_number, title, supplier_pm, customer_pm):
        ################### Individual Loan Menu Operations ######################

        self.click(self.loan_locator)
        self.click(self.operation_locator)
        self.click(self.application_locator)
        self.click(self.individual_locator)

        ################### Individual Loan Form ######################

        #################### Step 1: Registration #####################

        self.click(self.enable_button_locator)

        self.click(self.product_locator)
        self.click(self.product_selection_locator)
        self.click(self.classification_individual_locator)
        self.write(self.customerNumber_locator, customer_number)
        self.write(self.title_locator, title)
        self.click(self.sourceOfFunds_locator)
        self.click(self.sourceOfFunds_selection_locator)
        self.click(self.mainPurpose_locator)
        self.click(self.mainPurpose_selection_locator)

        # scroll by pixel
        self.js_script(self.scroll_500_pixel_locator)

        self.click(self.groupPurpose_locator)
        self.click(self.groupPurpose_selection_locator)
        self.click(self.detailPurpose_locator)
        self.click(self.detailPurpose_selection_locator)
        self.click(self.creditOfficer_locator)
        self.click(self.creditOfficer_selection_locator)

        # Business Since Date
        self.click(self.business_dos_locator)
        self.click(self.business_dos_month_locator)
        self.click(self.business_dos_year_locator)
        self.click(self.business_dos_day_locator)

        self.write(self.supplier_pm_button_locator, supplier_pm)
        self.click(self.salesFrequency_locator)
        self.click(self.salesFrequency_selection_locator)
        self.write(self.customer_pm_button_locator, customer_pm)
        self.click(self.workCategory_locator)
        self.click(self.workCategory_selection_locator)

        self.js_script(self.scroll_bottom_locator)

        self.click(self.next_button_locator)

        # Social Activity
        self.js_script(self.scroll_bottom_locator)

        self.click(self.next_button_locator)

    def loan_individual_cashflow_step(self, income_amount, expense_amount, value):
        ######################### Step 3: Cash Flow ########################
        # Financial Income
        self.click(self.income_code_locator)
        self.click(self.income_code_selection_locator)
        self.click(self.income_frequency_locator)
        self.click(self.income_frequency_selection_locator)
        self.click(self.income_currency_locator)
        self.click(self.income_currency_selection_locator)
        self.write(self.income_amount_locator, income_amount)

        # scroll by pixel
        self.js_script(self.scroll_1500_pixel_locator)

        # Financial Expense
        self.click(self.expense_code_locator)
        self.click(self.expense_code_selection_locator)
        self.click(self.expense_frequency_locator)
        self.click(self.expense_frequency_selection_locator)
        self.click(self.expense_currency_locator)
        self.click(self.expense_currency_selection_locator)
        self.write(self.expense_amount_locator, expense_amount)

        # Actual Activity Expense
        self.click(self.type_locator)
        self.click(self.type_selection_locator)
        self.click(self.currency_locator)
        self.click(self.currency_selection_locator)
        self.write(self.value_locator, value)

        self.js_script(self.scroll_bottom_locator)

        self.click(self.next_button_locator)

    def loan_individual_documents_step(self, description, document_upload_image):
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

    def loan_individual_guarantor_step(self, customer_number):
        #################### Step 5: Guarantor #####################

        self.write(self.guarantorCustomer_locator, customer_number)

        # self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)

    def loan_individual_correlation_step(self, correlation_account):
        #################### Step 6: Correlation  #####################

        self.write(self.correlationAccount_locator, correlation_account)

        # self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)

    def loan_individual_details_step(self, amount, duration):
        #################### Step 6: Loan Detail  #####################

        self.write(self.appliedAmount_locator, amount)
        interest = self.get_value(self.interestRate_locator)

        # For RF Effective date is compulsory
        # self.click(self.effectiveDate_locator)
        # self.click(self.effectiveDay_locator)

        self.click(self.paymentFrequency_locator)
        self.click(self.paymentFrequency_selection_locator)
        self.write(self.duration_locator, duration)
        self.click(self.generate_button_locator)
        time.sleep(1)
        # self.click(self.clear_button_locator)

        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        # Collateral
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)
        # Checklist
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)

        # Overview
        self.js_script(self.scroll_bottom_locator)
        self.click(self.save_button_locator)
        self.click(self.accept_button_locator)
        success = self.get_text(self.success_locator)
        self.click(self.success_close_locator)

        return success

