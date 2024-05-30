import time
from unittest import TestCase
from Kcbl.Deposit.Deposit_Registration.individual_deposit_registration_test import IndividualDepositRegistrationTest
from Kcbl.Deposit.Deposit_Approval.individual_deposit_approval_page import IndividualDepositApprovalPage

from Kcbl.Base.BasePage import BaseClass

base = BaseClass()


class IndividualDepositApprovalTest(TestCase):

    def test_deposit_individual_accept(self):
        # LoginTest().test_login("0003", "aswad", "Aswad@123")
        IndividualDepositRegistrationTest().test_deposit_individual()
        deposit_approval_page = IndividualDepositApprovalPage()
        deposit_approval_page.deposit_menu()

        ############ Accept ##########
        for i in range(4):
            success = deposit_approval_page.deposit_individual_approval_with_accept()
            self.assertEqual('Success', success)
            deposit_approval_page.deposit_refresh_menu()
            time.sleep(3)

        base.browser_close()

    def test_deposit_individual_reject(self):
        # LoginTest().test_login("0003", "aswad", "Aswad@123")
        IndividualDepositRegistrationTest().test_deposit_individual()
        deposit_approval_page = IndividualDepositApprovalPage()

        ############ Reject ##########
        deposit_approval_page.deposit_menu()
        reject_data = deposit_approval_page.deposit_individual_approval_with_reject()
        status_rejected, workflow_stage_registration = reject_data
        self.assertEqual('Rejected', status_rejected)
        self.assertEqual('Registration', workflow_stage_registration)
        self.test_deposit_individual_save()

    def test_deposit_individual_save(self):
        deposit_approval_page = IndividualDepositApprovalPage()

        ############ Save ##########
        deposit_approval_page.deposit_menu()
        save_data = deposit_approval_page.deposit_individual_approval_with_save()
        status_pending, workflow_stage_authorization = save_data
        self.assertEqual('Pending', status_pending)
        self.assertEqual('Authorization', workflow_stage_authorization)

        ############ Accpet ##########

        deposit_approval_page.deposit_individual_approval_with_accept()

        base.browser_close()
