import time
from unittest import TestCase

from Kcbl.Base.BasePage import BaseClass
from Kcbl.Login.login_test import LoginTest
from Kcbl.Loan.Loan_Approval.individual_loan_approval_page import IndividualLoanApprovalPage

base = BaseClass()


class IndividualLoanApprovalTest(TestCase):
    def test_loan_individual_credit_committee_1_accept(self):
        organization_code = "0003"
        username = "imtiaz712"
        password = "Approval@123"
        LoginTest().test_login(organization_code, username, password)

        loan_approval_page = IndividualLoanApprovalPage()
        ############ Accept ##########

        success = loan_approval_page.loan_individual_approval_with_accept()
        self.assertEqual('Success', success)

        # base.browser_close()
        # time.sleep(20)

        LoginTest().test_logout()

    def test_loan_individual_credit_committee_2_accept(self):
        organization_code = "0003"
        username = "faqir184"
        password = "Approval@123"
        LoginTest().test_login(organization_code, username, password)

        loan_approval_page = IndividualLoanApprovalPage()
        ############ Accept ##########

        success = loan_approval_page.loan_individual_approval_with_accept()
        self.assertEqual('Success', success)

        # base.browser_close()
        # time.sleep(20)

        LoginTest().test_logout()

        time.sleep(3)


