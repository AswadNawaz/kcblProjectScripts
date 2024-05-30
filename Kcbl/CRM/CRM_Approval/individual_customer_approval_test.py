from unittest import TestCase
from Kcbl.CRM.CRM_Registration.individual_customer_registration_test import IndividualCRMRegistrationTest
from Kcbl.CRM.CRM_Approval.individual_customer_approval_page import IndividualCRMApprovalPage

from Kcbl.Base.BasePage import BaseClass

base = BaseClass()

class CRMApprovalTest(TestCase):

    def test_crm_individual_customer_accept(self):

        # Kcbl/LoginTest().test_login()
        IndividualCRMRegistrationTest().test_crm_individual_customer()
        crm_approval_page = IndividualCRMApprovalPage()

        ############ Accept ##########

        success = crm_approval_page.crm_individual_customer_approval_step_with_accept()
        self.assertEqual('Success', success)

        base.browser_close()

    def test_crm_individual_customer_reject(self):
        # LoginTest().test_login()
        IndividualCRMRegistrationTest().test_crm_individual_customer()
        crm_approval_page = IndividualCRMApprovalPage()

        ############ Reject ##########

        reject_data = crm_approval_page.crm_individual_customer_approval_step_with_reject()
        status_rejected, workflow_stage_registration = reject_data
        self.assertEqual('Rejected', status_rejected)
        self.assertEqual('Customer Registration', workflow_stage_registration)
        self.test_crm_individual_customer_save()

    def test_crm_individual_customer_save(self):

        crm_approval_page = IndividualCRMApprovalPage()

        ############ Save ##########

        save_data = crm_approval_page.crm_individual_customer_approval_step_with_save()
        status_pending, workflow_stage_authorization = save_data
        self.assertEqual('Pending', status_pending)
        self.assertEqual('Customer Authorization', workflow_stage_authorization)

        ############ Accpet ##########

        crm_approval_page.crm_individual_customer_approval_step_with_accept()

        base.browser_close()


