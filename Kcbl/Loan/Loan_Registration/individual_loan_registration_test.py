import time
from unittest import TestCase
from Kcbl.Login.login_test import LoginTest
from Kcbl.Loan.Loan_Registration.individual_loan_registration_page import IndividualLoanRegistrationPage


class IndividualLoanRegistrationTest(TestCase):
    def test_loan_individual(self):
        LoginTest().test_login()
        # Loan Products Numbers for select specific product             Payment frequency
        # 1. Salary Advance Scheme                                      1. Weekly
        # 2. Pension Advance Scheme                                     2. Monthly
        # 3. Running Finance (Loan)                                     3. Half Yearly
        # 4. Enterprise Loan (Project Finance Scheme)                   4. Bullet
        # 9. Loan Against TDR                                           5. Bi-Weekly

        product_number = "1"
        # Payment Frequency in Loan detail
        frequency = "2"
        loan_registration_page = IndividualLoanRegistrationPage(product_number, frequency)

        #################### Step 1: Registration #####################

        customer_number = "0000001"
        title = "Individual Loan"
        supplier_pm = "Card"
        customer_pm = "Online"

        loan_registration_page.loan_individual_registration_step(customer_number, title, supplier_pm, customer_pm)

        #################### Step 3: Cash Flow #####################

        income_amount = 150000000
        expense_amount = 100
        value = 100
        loan_registration_page.loan_individual_cashflow_step(income_amount, expense_amount, value)

        #################### Step 4: Documents #####################

        comments = "A"
        document_upload_image = "E:\\Office Work\\Images\\sampleFile.jpeg"
        loan_registration_page.loan_individual_documents_step(comments, document_upload_image)

        #################### Step 5: Guarantor #####################

        guarantor_customer = "0000002"
        loan_registration_page.loan_individual_guarantor_step(guarantor_customer)

        #################### Step 6: Correlation #####################

        correlation_account = "0000001"
        loan_registration_page.loan_individual_correlation_step(correlation_account)

        #################### Step 6: Loan Detail #####################

        amount = 100000
        duration = 12
        success = loan_registration_page.loan_individual_details_step(amount, duration)
        self.assertEqual("Success", success)

        # time.sleep(20)

        LoginTest().test_logout()

        time.sleep(3)
