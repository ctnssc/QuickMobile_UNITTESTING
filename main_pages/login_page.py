#All the action we will take on the page

from main_pages.base_page import BasePage
from main_pages.page_identifiers import LogInPageData, LogInIdentifiers


class LogInPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)  #apelam driverul din clasa parinte.


    def open_page(self):
        return super().open_url(LogInPageData.log_in_page_url)


    def execute_valid_login(self):
        self.type(LogInIdentifiers.email_field_xpath, LogInPageData.valid_email)
        self.type(LogInIdentifiers.password_field_xpath, LogInPageData.valid_password)
        self.click(LogInIdentifiers.login_button_xpath)

    def execute_invalid_email_login(self):
        self.type(LogInIdentifiers.email_field_xpath, LogInPageData.invalid_email)
        self.type(LogInIdentifiers.password_field_xpath, LogInPageData.valid_password)
        self.click(LogInIdentifiers.login_button_xpath)

    def execute_invalid_password_login(self):
        self.type(LogInIdentifiers.email_field_xpath, LogInPageData.valid_email)
        self.type(LogInIdentifiers.password_field_xpath, LogInPageData.invalid_password)
        self.click(LogInIdentifiers.login_button_xpath)

    def execute_invalid_login(self):
        self.type(LogInIdentifiers.email_field_xpath, LogInPageData.invalid_email)
        self.type(LogInIdentifiers.password_field_xpath, LogInPageData.invalid_password)
        self.click(LogInIdentifiers.login_button_xpath)

