from Kcbl.Login.login_page import LoginPage
from Kcbl.Base.BasePage import BaseClass

class TestLogin(BaseClass):
    def test_login(self, browser):
        login = LoginPage()

        url = "https://kcbltest.ciihive.com"
        organization_code = "0003"
        username = "aswad"
        password = "Aswad@1234"

        result = login.login_with_valid_credentials(url, organization_code, username, password)
        # time.sleep(3)
        assert "MFSys Financial Application" in result

    def test_logout(self, browser):
        logout = LoginPage()
        url1 = "https://kcbltest.ciihive.com"
        organization_code1 = "0003"
        username1 = "aswad"
        password1 = "Aswad@123"
        logout.login_with_valid_credentials(url1, organization_code1, username1, password1)
        result = logout.logout()
        assert "Logged Out Successfully" in result
