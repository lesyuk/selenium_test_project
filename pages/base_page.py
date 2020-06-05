from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """
    Base PageObject for web application.

    Other screens inherit from this class.
    """
    def __init__(self, driver):
        """Constructor"""
        self.driver = driver
        self.base_url = "https://cian.ru"

    def find_element(self, locator, time=10):
        """WebDriverWait wrapper that find one element and return it"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_element_located(locator),
                                                      message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """WebDriverWait wrapper that find several elements and return them"""
        return WebDriverWait(self.driver, time).until(EC.presence_of_all_elements_located(locator),
                                                      message=f"Can't find elements by locator {locator}")

    def click_element(self):
        ...

    def go_to_site(self):
        """Go to the base URL of the web application"""
        return self.driver.get(self.base_url)
