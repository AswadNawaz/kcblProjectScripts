import time
from unittest import TestCase
from Kcbl.Login.login_test import LoginTest
from Kcbl.CRM.CRM_Registration.individual_customer_registration_page import IndividualCRMRegistrationPage


class IndividualCRMRegistrationTest(TestCase):
    def test_crm_individual_customer(self):
        LoginTest().test_login("0003", "aswad", "Aswad@123")
        crm_registration_page = IndividualCRMRegistrationPage()

        #################### Step 1: Registration #####################

        identification_number = "3423423427825"
        first_name = "Dildar"
        last_name = "Jameel"
        full_name = 'Dildar Jameel'
        father_name = "M Jameel"
        mother_name = "M"
        parental_name = "F"
        place = "a"
        monthly_income = 100000
        other_income = 1000
        month = 1
        introducer = 'I'
        children = 2
        dependent = 1
        know = 'K'

        identity_type = crm_registration_page.crm_individual_customer_registration_step(identification_number, first_name, last_name, full_name, father_name, mother_name, parental_name, place, monthly_income, other_income, month, introducer, children, dependent, know)

        #################### Step 2: Address #####################

        address = "islamabad"
        telephone = "09876787611"
        mobile = "09878787765"
        email = "dildar@gmail.com"
        crm_registration_page.crm_individual_customer_address_step(address, telephone, mobile, email)

        #################### Step 3: Identification #####################

        family_number = "1223"
        upload_image = "E:\\Office Work\\Images\\sampleFile.jpeg"
        type_number = crm_registration_page.crm_individual_customer_identification_step(family_number, upload_image)
        identification_type, number = type_number
        self.assertEqual(identity_type, identification_type)
        self.assertEqual(identification_number, number)

        #################### Step 4: Documents #####################

        comments = "A"
        document_upload_image = "E:\\Office Work\\Images\\jpeg_image.jpg"
        success = crm_registration_page.crm_individual_customer_documents_step(comments, document_upload_image)
        self.assertEqual("Success", success)

        time.sleep(3)

