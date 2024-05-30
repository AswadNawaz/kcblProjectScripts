import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from Kcbl.Base.BasePage import BaseClass


class IndividualCRMRegistrationPage(BaseClass):
    def __init__(self):
        ################### Individual Customer Menu Locator ######################

        self.crm_locator = By.XPATH, "//app-menu/ul/li[2]/a"
        self.operation_locator = By.XPATH, "//app-menu/ul/li[2]/ul/li[1]/a"
        self.registration_locator = By.XPATH, "//app-menu/ul/li[2]/ul/li[1]/ul/li[1]/a"
        self.individual_locator = By.XPATH, "//app-menu/ul/li[2]/ul/li[1]/ul/li[1]/ul/li[1]/a"

        ############################### Individual Customer Form Locator ###############################

        #################### Step 1: Registration #####################

        self.enable_button_locator = By.XPATH, "//form/pe-steps/p-toolbar/div/div/div[2]/button[1]/span[1]"
        self.identificationType_locator = By.ID, "PIT_IDENCODE_2"
        self.identificationType_selection_locator = By.XPATH, "//*[@id='PIT_IDENCODE_2']//ul/p-dropdownitem[1]/li"
        self.identificationTypeText_locator = By.XPATH, "//*[@id='PIT_IDENCODE_2']/div/span"
        self.identificationNumber_locator = By.XPATH, "//*[@id='CIT_IDENVALUE_2undefined']//input"
        self.firstName_locator = By.XPATH, "//*[@id='CMP_FIRSTNAMEundefined']//input"
        self.lastName_locator = By.XPATH, "//*[@id='CMP_LASTNAMEundefined']//input"
        self.fullName_locator = By.XPATH, "//*[@id='CMP_FULLNAMEundefined']//input"
        self.gender_locator = By.ID, "CMP_CUSTSEX"
        self.gender_selection_locator = By.XPATH, "//*[@id='CMP_CUSTSEX']//ul/p-dropdownitem[2]/li"
        self.salutation_locator = By.ID, "CMP_SALUTATION"
        self.salutation_selection_locator = By.XPATH, "//*[@id='CMP_SALUTATION']//li"
        self.maritalStatus_locator = By.ID, "CMP_MARITALSTATUS"
        self.maritalStatus_selection_locator = By.XPATH, "//*[@id='CMP_MARITALSTATUS']//ul/p-dropdownitem[1]/li"
        self.fatherName_locator = By.XPATH, "//*[@id='CMP_FATHERNAMEundefined']//input"
        self.motherName_locator = By.XPATH, "//*[@id='CMP_MOTHERNAMEundefined']//input"
        self.parentageName_locator = By.XPATH, "//*[@id='CMP_CUSTPRTGNAMEundefined']//input"
        self.customerNationality_locator = By.XPATH, "//label[text()='Local National']"
        self.nationality_locator = By.ID, "CMP_NATIONALITY"
        self.nationality_selection_locator = By.XPATH, "//*[@id='CMP_NATIONALITY']//ul/p-dropdownitem[1]/li"
        self.dob_locator = By.XPATH, "//*[@id='CMP_CUSTDATEBIRTHundefined']/div[2]/p-calendar/span"
        self.dob_month_locator = By.XPATH, "//*[@id='CMP_CUSTDATEBIRTHundefined']//select[1]/option[1]"
        self.dob_year_locator = By.XPATH, "//*[@id='CMP_CUSTDATEBIRTHundefined']//select[2]/option[92]"
        self.dob_day_locator = By.XPATH, "//*[@id='CMP_CUSTDATEBIRTHundefined']//table/tbody/tr[4]/td[4]/span"
        self.birthCountry_locator = By.ID, "CMP_BIRTHPLACE"
        self.birthCountry_selection_locator = By.XPATH, "//*[@id='CMP_BIRTHPLACE']//ul/p-dropdownitem[1]/li"
        self.birthPlace_locator = By.ID, "CMP_BIRTHCITY"
        self.birthPlace_input_locator = By.XPATH, "//*[@id='CMP_BIRTHCITY']/div/div[3]/div[1]/div/input"
        self.birthPlace_selection_locator = By.XPATH, "//*[@id='CMP_BIRTHCITY']//ul/p-dropdownitem[1]/li"

        # Scroll down by 500 pixels
        self.scroll_some_pixel_locator = "window.scrollBy(0, 500);"

        self.education_locator = By.ID, "CMP_EDUCATION"
        self.education_selection_locator = By.XPATH, "//*[@id='CMP_EDUCATION']//ul/p-dropdownitem[5]/li"
        self.disability_yes_locator = By.XPATH, "//label[text()='Yes']"
        self.disability_no_locator = By.XPATH, "//label[text()='No']"
        self.occupation_locator = By.ID, "CMP_OCCUPATION"
        self.occupation_selection_locator = By.XPATH, "//*[@id='CMP_OCCUPATION']//ul/p-dropdownitem[1]/li"
        self.estimated_monthly_income_locator = By.XPATH, "//*[@id='ESTM_INCOMEundefined']//input"
        self.estimated_other_income_locator = By.XPATH, "//*[@id='ESTO_INCOMEundefined']//input"
        self.work_category_locator = By.ID, "WORK_CATEGCODE"
        self.work_category_selection_locator = By.XPATH, "//*[@id='WORK_CATEGCODEundefined']//ul/p-dropdownitem[1]/li"
        self.work_sub_category_locator = By.ID, "WORK_SUBCATE"
        self.work_sub_category_selection_locator = By.XPATH, "//*[@id='WORK_SUBCATE']//ul/p-dropdownitem[1]/li/span"
        self.monthDuration_locator = By.XPATH, "//*[@id='WORK_HOURSundefined']/div[2]//input"
        self.work_type_locator = By.ID, "TYPE_WORK"
        self.work_type_selection_locator = By.XPATH, "//*[@id='TYPE_WORK']//ul/p-dropdownitem[1]/li/span"
        self.introducer_locator = By.XPATH, "//*[@id='CP_INTRODUCERundefined']//input"
        self.children_locator = By.XPATH, "//*[@id='CMP_CHILDRENundefined']//input"
        self.childrenAge_locator = By.ID, "CMP_CHILDAGE"
        self.childrenAge_selection_locator =By.XPATH, "//*[@id='CMP_CHILDAGE']//ul/p-dropdownitem[1]/li"
        self.dependentOther_locator = By.XPATH, "//*[@id='CMP_DEPOTHERundefined']//input"

        # Scroll down
        self.scroll_bottom_locator = "window.scrollTo(0,document.body.scrollHeight)"

        self.howDoYouKnow_locator = By.XPATH, "//*[@id='CMP_HTOKNOWundefined']//input"
        self.customerRisk_locator =By.ID, "CMP_CUSTRISK_RATE"
        self.customerRisk_selection_locator = By.XPATH, "//*[@id='CMP_CUSTRISK_RATE']//ul/p-dropdownitem[3]/li"

        self.next_button_locator = By.XPATH, "//form/pe-steps/button[2]"

        #################### Step 2: Address #####################

        self.address_type_locator = By.ID, "PAT_ADRSCODE"
        self.address_type_selection_locator = By.XPATH, "//*[@id='PAT_ADRSCODE']//ul/p-dropdownitem[2]/li"
        self.address_locator = By.XPATH, "//*[@id='PAD_ADRSDEFAULT0']/div[2]/input"
        self.address_country_locator = By.ID, "PCO_CTRYCODE"
        self.address_country_selection_locator = By.XPATH, "//*[@id='PCO_CTRYCODE']//ul/p-dropdownitem[1]/li"
        self.province_locator = By.ID, "PPV_PROVCODE"
        self.province_selection_locator = By.XPATH, "//*[@id='PPV_PROVCODE']//ul/p-dropdownitem[1]/li"
        self.district_locator = By.ID, "PDS_DISTCODE"
        self.district_selection_locator = By.XPATH, "//*[@id='PDS_DISTCODE']//ul/p-dropdownitem[1]/li"
        self.city_locator = By.ID, "PCT_CITYCODE"
        self.city_selection_locator = By.XPATH, "//*[@id='PCT_CITYCODE']//ul/p-dropdownitem[1]/li/span"
        self.telephone_locator = By.XPATH, "//*[@id='PAD_ADRSLNDPHONE0']/div[2]/input"
        self.mobile_locator = By.XPATH, "//*[@id='PAD_ADRSMOBPHONE0']/div[2]/input"
        self.email_locator = By.XPATH, "//*[@id='PAD_ADRSEMAIL0']/div[2]/input"
        self.mailing_address_locator = By.XPATH, "//*[@id='PAD_ADRSCORRESPONDENCE0']/div[2]/p-checkbox/div/div[2]"

        #################### Step 3: Identification #####################

        self.identification_type_locator = By.XPATH, "//*[@id='PIT_IDENCODE']/div/span"
        self.identification_number_locator = By.XPATH, "//*[@id='CIT_IDENVALUE0']//input"
        self.doi_locator = By.XPATH, "//*[@id='CIT_IDENISSUEDATE0']/div[2]/p-calendar/span"
        self.doi_month_locator = By.XPATH, "//*[@id='CIT_IDENISSUEDATE0']//select[1]/option[7]"
        self.doi_year_locator = By.XPATH, "//*[@id='CIT_IDENISSUEDATE0']//select[2]/option[114]"
        self.doi_day_locator = By.XPATH, "//*[@id='CIT_IDENISSUEDATE0']//table/tbody/tr[4]/td[4]/span"
        self.CNICLifetime_locator = By.XPATH, "//label[text()='No']"
        self.doe_locator = By.XPATH, "//*[@id='CIT_IDENEXPIRYDATE0']/div[2]/p-calendar/span"
        self.doe_month_locator = By.XPATH, "//*[@id='CIT_IDENEXPIRYDATE0']//select[1]/option[7]"
        self.doe_year_locator = By.XPATH, "//*[@id='CIT_IDENEXPIRYDATE0']//select[2]/option[114]"
        self.doe_day_locator = By.XPATH, "//*[@id='CIT_IDENEXPIRYDATE0']//table/tbody/tr[4]/td[4]/span"
        self.familyNumber_locator = By.XPATH, "//*[@id='CARD_NUMBER0']//input"
        self.upload_image_locator = By.XPATH, "//*[@id='CIT_IDENIMAGE0']//input"
        self.upload_button_locator = By.XPATH, "//*[@id='CIT_IDENIMAGE0']//p-button[1]/button"
        self.picture_cancel_button_locator = By.XPATH, "//*[@id='CIT_IDENIMAGE0']/div[2]/p-fileupload/div/div[2]/div/div/div/div[1]/button"
        self.primary_identification_locator = By.XPATH, "//*[@id='PIT_PRIMARYIDENCODE0']/div[2]/p-checkbox/div/div[2]"

        #################### Step 4: Documents #####################

        self.document_type_locator = By.ID, "PDT_DOTYCODE"
        self.document_type_selection_locator = By.XPATH, "//*[@id='PDT_DOTYCODE']//ul/p-dropdownitem[1]/li"
        self.comments_locator = By.XPATH, "//*[@id='CDO_COMMENT0']/div[2]/input"
        self.document_doi_locator = By.XPATH, "//*[@id='PDT_DOTYISSUEDATE0']/div[2]/p-calendar/span"
        self.document_doi_month_locator = By.XPATH, "//*[@id='PDT_DOTYISSUEDATE0']//select[1]/option[7]"
        self.document_doi_year_locator = By.XPATH, "//*[@id='PDT_DOTYISSUEDATE0']//select[2]/option[114]"
        self.document_doi_day_locator = By.XPATH, "//*[@id='PDT_DOTYISSUEDATE0']//table/tbody/tr[4]/td[4]/span"
        self.document_doe_locator = By.XPATH, "//*[@id='PDT_DOTYEXPIRYDATE0']/div[2]/p-calendar/span"
        self.document_doe_month_locator = By.XPATH, "//*[@id='PDT_DOTYEXPIRYDATE0']//select[1]/option[7]"
        self.document_doe_year_locator = By.XPATH, "//*[@id='PDT_DOTYEXPIRYDATE0']//select[2]/option[114]"
        self.document_doe_day_locator = By.XPATH, "//*[@id='PDT_DOTYEXPIRYDATE0']//table/tbody/tr[4]/td[4]/span"
        self.document_upload_image_locator = By.XPATH, "//*[@id='CDO_DCOUMENTFILE0']//input"
        self.document_upload_button_locator = By.XPATH, "//*[@id='CDO_DCOUMENTFILE0']//p-button[1]/button"

        self.save_button_locator = By.ID, "accept_btn"

        self.accept_button_locator = By.XPATH, "//p-footer/button[1]"

        self.success_locator = By.XPATH, "/html/body/my-app/app-root/div/div/p-toast/div/p-toastitem/div/div/div/div[1]"


    def crm_individual_customer_registration_step(self, identification_number, firstname, lastname, fullname, fathername, mothername, parentagename, place,
                                monthly_income, other_income, month, introducer, children, noOfDependent, know):
        ################### Individual Customer Menu Operations ######################

        self.click(self.crm_locator)
        self.click(self.operation_locator)
        self.click(self.registration_locator)
        self.click(self.individual_locator)

        ################### Individual Customer Form ######################

        #################### Step 1: Registration #####################

        self.click(self.enable_button_locator)

        self.click(self.identificationType_locator)
        self.click(self.identificationType_selection_locator)
        identity_type = self.get_text(self.identificationTypeText_locator)
        self.write(self.identificationNumber_locator, identification_number)
        self.write(self.firstName_locator, firstname)
        self.write(self.lastName_locator, lastname)
        self.write(self.fullName_locator, fullname)
        self.click(self.gender_locator)
        self.click(self.gender_selection_locator)
        self.click(self.salutation_locator)
        time.sleep(1)
        self.click(self.salutation_selection_locator)
        self.click(self.maritalStatus_locator)
        self.click(self.maritalStatus_selection_locator)
        self.write(self.fatherName_locator, fathername)
        self.write(self.motherName_locator, mothername)
        self.write(self.parentageName_locator, parentagename)
        self.click(self.customerNationality_locator)
        self.click(self.nationality_locator)
        self.click(self.nationality_selection_locator)

        # scroll by pixel
        self.js_script(self.scroll_some_pixel_locator)

        self.click(self.dob_locator)
        self.click(self.dob_month_locator)
        self.click(self.dob_year_locator)
        self.click(self.dob_day_locator)
        self.click(self.birthCountry_locator)
        self.click(self.birthCountry_selection_locator)
        self.click(self.birthPlace_locator)
        self.write(self.birthPlace_input_locator, place)
        self.write(self.birthPlace_input_locator, Keys.ENTER)
        self.click(self.birthPlace_selection_locator)

        # scroll by pixel
        # self.js_script(self.scroll_some_pixel_locator)

        self.click(self.education_locator)
        self.click(self.education_selection_locator)
        self.click(self.occupation_locator)
        self.click(self.occupation_selection_locator)
        self.click(self.disability_yes_locator)
        self.click(self.disability_no_locator)
        self.write(self.estimated_monthly_income_locator, monthly_income)
        self.write(self.estimated_other_income_locator, other_income)
        self.click(self.work_category_locator)
        self.click(self.work_category_selection_locator)
        self.click(self.work_sub_category_locator)
        self.click(self.work_sub_category_selection_locator)
        self.write(self.monthDuration_locator, month)
        self.click(self.work_type_locator)
        self.click(self.work_type_selection_locator)
        self.write(self.introducer_locator, introducer)
        self.write(self.children_locator, children)
        self.click(self.childrenAge_locator)
        self.click(self.childrenAge_selection_locator)
        self.write(self.dependentOther_locator, noOfDependent)

        self.js_script(self.scroll_bottom_locator)

        self.write(self.howDoYouKnow_locator, know)
        self.click(self.customerRisk_locator)
        self.click(self.customerRisk_selection_locator)

        self.click(self.next_button_locator)

        return identity_type


    def crm_individual_customer_address_step(self, address, telephone, mobile, email):

        #################### Step 2: Address #####################


        self.click(self.address_type_locator)
        self.click(self.address_type_selection_locator)
        self.write(self.address_locator, address)
        self.click(self.address_country_locator)
        self.click(self.address_country_selection_locator)
        self.click(self.province_locator)
        self.click(self.province_selection_locator)
        self.click(self.district_locator)
        self.click(self.district_selection_locator)
        self.click(self.city_locator)
        self.click(self.city_selection_locator)
        self.write(self.telephone_locator, telephone)
        self.write(self.mobile_locator, mobile)
        self.write(self.email_locator, email)
        self.click(self.mailing_address_locator)

        self.js_script(self.scroll_bottom_locator)

        self.click(self.next_button_locator)


    def crm_individual_customer_identification_step(self, family_number, upload_image):

        #################### Step 3: Identification #####################

        time.sleep(1)
        type = self.get_text(self.identification_type_locator)
        number = self.get_value(self.identification_number_locator)
        self.click(self.doi_locator)
        self.click(self.doi_month_locator)
        self.click(self.doi_year_locator)
        self.click(self.doi_day_locator)
        self.click(self.CNICLifetime_locator)
        self.click(self.doe_locator)
        self.click(self.doe_month_locator)
        self.click(self.doe_year_locator)
        self.click(self.doe_day_locator)
        self.write(self.familyNumber_locator, family_number)
        self.write(self.upload_image_locator, upload_image)
        self.click(self.upload_button_locator)
        self.click(self.picture_cancel_button_locator)
        self.click(self.primary_identification_locator)

        self.js_script(self.scroll_bottom_locator)

        self.click(self.next_button_locator)

        return [type, number]

    def crm_individual_customer_documents_step(self, comments, document_upload_image):

        #################### Step 4: Documents #####################

        self.click(self.document_type_locator)
        self.click(self.document_type_selection_locator)
        self.write(self.comments_locator, comments)
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
        time.sleep(3)

        # Spouse Step
        self.js_script(self.scroll_bottom_locator)
        self.click(self.next_button_locator)

        # Overview
        self.js_script(self.scroll_bottom_locator)

        self.click(self.save_button_locator)
        self.click(self.accept_button_locator)
        success = self.get_text(self.success_locator)

        return success
