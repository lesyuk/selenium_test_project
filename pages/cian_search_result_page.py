from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CianSearchResultLocators:
    LOCATOR_CIAN_SEARCH_RESULT_TITLE = (By.XPATH, '//div[@data-name="Breadcrumbs"]//h1')


class SearchResultHelpers(BasePage):
    def check_search_result_title(self):
        result_title = self.find_element(CianSearchResultLocators.LOCATOR_CIAN_SEARCH_RESULT_TITLE, time=2).text
        return result_title
