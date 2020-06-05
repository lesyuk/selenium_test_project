from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class CianSearchLocators:
    LOCATOR_CIAN_SEARCH_FIELD = (By.XPATH, '//input[@id="geo-suggest-input"]')
    LOCATOR_CIAN_SEARCH_BUTTON = (By.XPATH, '//a[@data-mark="FiltersSearchButton"]')


class SearchHelpers(BasePage):
    def enter_word(self, word):
        search_field = self.find_element(CianSearchLocators.LOCATOR_CIAN_SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        sleep(2)
        search_field.send_keys(Keys.RETURN)
        sleep(2)
        return search_field

    def click_search_button(self):
        return self.find_element(CianSearchLocators.LOCATOR_CIAN_SEARCH_BUTTON, time=2).click()
