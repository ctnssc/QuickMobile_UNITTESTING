#All the actions we execute on a page:
#1. Constructor driver initialization.
#2. Open page url.
#3. Get current url
#3. Find an element
#4. Wait for elements to get visible/appear on page
#5. Get text
#6. Type
#7. Click
#8. Verify if an ellement is displayed


from selenium.common import NoSuchElementException
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver:WebDriver): #Creare constructor si instantiere driver
        self.driver = driver

    def open_url(self, url:str):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def find(self, identifier: tuple):
        return self.driver.find_element(*identifier)

    def wait_for_visible_element(self, identifier: tuple, time:int = 10):
        wait = WebDriverWait(self.driver, time)
        wait.until(expected_conditions.visibility_of_element_located(identifier), "Element not visible")

    def get_text(self, identifier: tuple, time: int = 10):
        self.wait_for_visible_element(identifier, time)
        return self.find(identifier).text

    def type(self, identifier:tuple, message:str,time: int = 10):
        self.wait_for_visible_element(identifier, time)
        self.find(identifier).send_keys(message)

    def click(self, identifier: tuple, time:int = 10):
        self.wait_for_visible_element(identifier,time)
        self.find(identifier).click()

    def is_displayed(self, identifier: tuple):
        try:
            return self.find(identifier).is_displayed()
        except NoSuchElementException:
            return False