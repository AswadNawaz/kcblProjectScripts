import time
from unittest import TestCase
from Kcbl.TermDeposit.Term_Deposit_Registration.individual_term_deposit_registration_test import \
    IndividualTermDepositRegistrationTest
from Kcbl.TermDeposit.Term_Deposit_Approval.individual_term_deposit_approval_page import \
    IndividualTermDepositApprovalPage

from Kcbl.Base.BasePage import BaseClass

base = BaseClass()


class IndividualDepositApprovalTest(TestCase):

    def test_term_deposit_individual_accept(self):
        # LoginTest().test_login("0003", "aswad", "Aswad@123")
        IndividualTermDepositRegistrationTest().test_term_deposit_individual()
        term_deposit_approval_page = IndividualTermDepositApprovalPage()
        term_deposit_approval_page.term_deposit_menu()

        ############ Accept ##########
        for i in range(4):
            success = term_deposit_approval_page.term_deposit_individual_approval_with_accept()
            self.assertEqual('Success', success)
            term_deposit_approval_page.term_deposit_refresh_menu()
            time.sleep(3)

        base.browser_close()

    def test_term_deposit_individual_reject(self):
        # LoginTest().test_login()
        IndividualTermDepositRegistrationTest().test_term_deposit_individual()
        term_deposit_approval_page = IndividualTermDepositApprovalPage()

        ############ Reject ##########

        reject_data = term_deposit_approval_page.term_deposit_individual_approval_with_reject()
        status_rejected, workflow_stage_registration = reject_data
        self.assertEqual('Rejected', status_rejected)
        self.assertEqual('BN_MS_TR_TDRREGISTRATION', workflow_stage_registration)
        self.test_term_deposit_individual_save()

    def test_term_deposit_individual_save(self):
        term_deposit_approval_page = IndividualTermDepositApprovalPage()

        ############ Save ##########

        save_data = term_deposit_approval_page.term_deposit_individual_approval_with_save()
        status_pending, workflow_stage_authorization = save_data
        self.assertEqual('Pending', status_pending)
        self.assertEqual('BN_MS_TA_TDRAUTHORIZATION', workflow_stage_authorization)

        ############ Accpet ##########

        term_deposit_approval_page.term_deposit_individual_approval_with_accept()

        base.browser_close()
