import unittest
from selenium import webdriver

from main_pages.login_page import LogInPage
from main_pages.login_successfully import LogInSuccesfully
from main_pages.page_identifiers import LogInPageData


class TestPositiveLogin(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(LogInPageData.log_in_page_url)
        self.driver.implicitly_wait(5)

    def test_valid_login(self):
        login_page_object = LogInPage(self.driver)
        succesfully_loged_in_page = LogInSuccesfully(self.driver)

        login_page_object.execute_valid_login()

        assert succesfully_loged_in_page.get_expected_url() == succesfully_loged_in_page.get_current_url(), "Actual URL is not the same as expected."
        assert LogInPageData.successfully_logged_in_text == succesfully_loged_in_page.get_succesfully_login_message(), "Login message not as expected."
        assert succesfully_loged_in_page.is_log_out_button_displayed(), "Logout button is not visible."


    def tearDown(self) -> None:
        self.driver.quit()