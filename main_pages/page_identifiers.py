#All the data we need to test the login.
from selenium.webdriver.common.by import By

# Saves all the data for the signin process: links, messages, text, values and informations.
class LogInPageData:
    log_in_page_url = 'https://www.quickmobile.ro/autentificare'
    valid_email = 'ctnssc@gmail.com'
    invalid_email = 'ctnss@gmail.com'
    valid_password = 'ITFfinalPROJECT'
    invalid_password = 'Parola123'
    successfully_logged_in_url = "https://www.quickmobile.ro/cont"
    successfully_logged_in_text = "Bun venit, Cristian!"
    invalid_login_expected_message = 'Adresa de email sau parola nu este corecta.'


# Saves all the objects/fields from the signin page using XPATH or others selectors.
class LogInIdentifiers:
    email_field_xpath = (By.XPATH,  "//input[@id='email']")
    password_field_xpath = (By.XPATH, "//input[@id='password']")
    login_button_xpath = (By.XPATH, "//button[contains(text(),'Autentificare')]")
    logged_in_successfully_xpath = (By.XPATH, "//h2[@class='section-title']")
    logged_in_unsuccessfully_xpath = (By.XPATH, "//div[@class='alert alert-with-icon alert-danger']")
    log_out_button = (By.XPATH, "//a[@href='/?logout']")

