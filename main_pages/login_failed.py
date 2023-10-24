#Verify if the login failed.
#Steps:
#1. Driver
#2. Get err message.

from main_pages.base_page import BasePage
from main_pages.page_identifiers import LogInIdentifiers


class LoginFailed(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_err_message(self):
        return super().get_text(LogInIdentifiers.logged_in_unsuccessfully_xpath)
