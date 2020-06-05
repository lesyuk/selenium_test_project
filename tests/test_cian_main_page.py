from pages.cian_main_page import SearchHelpers
from pages.cian_search_result_page import SearchResultHelpers


class TestCianMainPage:
    def test_search(self, browser):
        cian_main_page = SearchHelpers(browser)
        cian_search_result_page = SearchResultHelpers(browser)
        cian_main_page.go_to_site()
        cian_main_page.enter_word('Подольск')
        cian_main_page.click_search_button()
        elements = cian_search_result_page.check_search_result_title()
        assert "Подольске" in elements
