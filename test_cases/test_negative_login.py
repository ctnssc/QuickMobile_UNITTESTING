import unittest
from selenium import webdriver

from main_pages.login_failed import LoginFailed
from main_pages.login_page import LogInPage
from main_pages.page_identifiers import LogInPageData



class TestNegativeLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(LogInPageData.log_in_page_url)
        self.driver.implicitly_wait(5)

    def test_invalid_email(self):
        login_page = LogInPage(self.driver)
        logged_in_failed = LoginFailed(self.driver)

        login_page.execute_invalid_email_login()

        assert LogInPageData.invalid_login_expected_message in logged_in_failed.get_err_message(), "err message not found."

    def test_invalid_password(self):
        login_page = LogInPage(self.driver)
        logged_in_failed = LoginFailed(self.driver)

        login_page.execute_invalid_password_login()

        assert LogInPageData.invalid_login_expected_message in logged_in_failed.get_err_message(), "err message not found."

    def test_invalid_login(self):
        login_page = LogInPage(self.driver)
        logged_in_failed = LoginFailed(self.driver)

        login_page.execute_invalid_login()

        assert LogInPageData.invalid_login_expected_message in logged_in_failed.get_err_message(), "err message not found."


def tearDown(self) -> None:
        self.driver.quit()