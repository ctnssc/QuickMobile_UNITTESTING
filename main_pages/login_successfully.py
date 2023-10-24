#Verify if the login was successfull.


from main_pages.base_page import BasePage
from main_pages.page_identifiers import LogInPageData, LogInIdentifiers


class LogInSuccesfully(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_expected_url(self):
        return LogInPageData.successfully_logged_in_url

    def get_succesfully_login_message(self):
        return super().get_text(LogInIdentifiers.logged_in_successfully_xpath)

    def is_log_out_button_displayed(self):
        return super().is_displayed(LogInIdentifiers.log_out_button)
