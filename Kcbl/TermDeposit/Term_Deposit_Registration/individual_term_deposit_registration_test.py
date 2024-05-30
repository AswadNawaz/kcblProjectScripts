import csv
import time
from unittest import TestCase
from Kcbl.Login.login_test import LoginTest
from Kcbl.TermDeposit.Term_Deposit_Registration.individual_term_deposit_registration_page import \
    IndividualTermDepositRegistrationPage


class IndividualTermDepositRegistrationTest(TestCase):

    def test_term_deposit_individual(self):
        LoginTest().test_login("0003", "aswad", "Aswad@123")
        # Term Deposit Products Numbers for select specific product ########### Roll Over
        # 1. Term Deposit 3M [18.50]                                           # 1. No Instruction
        # 2. Term Deposit 6M [19.00]                                           # 2. On Principle
        # 3. Term Deposit 1Y [20.00]                                          # 3. Principle and Profit
        # 9. MIS 1Y          [20.00]                                           # 4. Credit on Maturity
        # 14. MIS 5Y         [11.00]
        # enter [product number] [rate] and [roll over] which you want to create TDR

        with open('C:\\Users\\muhammad.aswad\\PycharmProjects\\kcblProjectScripts\\TestData\\termDeposit.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            p = "0"
            r = "0"
            loop_number = 0
            term_deposit = IndividualTermDepositRegistrationPage(p, r)
            term_deposit.term_deposit_menu()

            for row in reader:
                product_number = row['product_number']
                roll_over = row['roll_over']
                customer_number = row['customer_number']
                title = row['title']
                duration = row['duration']
                amount = row['amount']
                comment = row['comment']
                deposit_account = row['deposit_account']
                document_comments = row['document_comments']
                document_upload_image = row['document_upload_image']

                term_deposit_registration_page = IndividualTermDepositRegistrationPage(product_number, roll_over)

                #################### Step 1: Registration #####################

                term_deposit_registration_page.term_deposit_individual_registration_step(customer_number, title, loop_number)

                #################### Step 2: Booking #####################

                term_deposit_registration_page.term_deposit_individual_booking_step(duration, amount, comment)

                #################### Step 3: Correlation #####################

                term_deposit_registration_page.term_deposit_individual_correlation_step(deposit_account)

                #################### Step 4: Documents #####################

                term_deposit_registration_page.term_deposit_individual_documents_step(document_comments, document_upload_image)

                #################### Step 5: Profit #####################

                profit_type_rate = term_deposit_registration_page.term_deposit_individual_profit_step()
                profit_type, rate = profit_type_rate

                # change profit type and rate according to product

                self.assertEqual("Fixes Rate", profit_type)
                # self.assertEqual("18.50", rate)

                #################### Step 6: Overview #####################

                success = term_deposit_registration_page.term_deposit_individual_overview_step()
                self.assertEqual("Success", success)

                loop_number = loop_number + 1

                # time.sleep(3)
