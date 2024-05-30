import csv
from Kcbl.Base.BasePage import BaseClass
from Kcbl.Login.login_test import TestLogin
from Kcbl.Deposit.Deposit_Registration.individual_deposit_registration_page import IndividualDepositRegistrationPage


class TestIndividualDepositRegistration(BaseClass):
    def test_deposit_individual(self, browser):
        TestLogin().test_login(self)
        # Deposit Products Numbers for select specific product
        # 1. Current
        # 2. RF Deposit
        # 3. PLS
        # 4. MMA

        with open('C:\\Users\\muhammad.aswad\\PycharmProjects\\kcblProjectScripts\\TestData\\deposit.csv',
                  newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            p = "0"
            deposit = IndividualDepositRegistrationPage(p)
            deposit.deposit_menu()

            for row in reader:
                product_number = row['product_number']
                customer_number = row['customer_number']
                title = row['title']
                comments = row['comments']
                document_upload_image = row['document_upload_image']
                introducer_customer = row['introducer_customer']

                deposit_registration_page = IndividualDepositRegistrationPage(product_number)

                #################### Step 1: Registration #####################

                deposit_registration_page.deposit_individual_registration_step(customer_number, title)

                #################### Step 2: Documents #####################

                deposit_registration_page.deposit_individual_documents_step(comments, document_upload_image)

                #################### Step 3: Relations #####################

                success = deposit_registration_page.deposit_individual_relations_step(introducer_customer)
                assert success == "Success"
                # self.assertEqual("Success", success)
