import allure
from source_code.pages.main.main_page import MainPage


class TestMainPage:
    @allure.feature('Main page')
    @allure.story('Search string')
    def test_search_string(self, driver):
        main_page = MainPage(driver)

        input_word = 'lash'
        main_page.find_by_search_string(input_word)

        with allure.step('Check that search is performed as expected'):
            search_results = main_page.search_results.assert_element(return_many=True)
            for result in search_results:
                assert input_word in result.text.lower(), f"The search result '{result}' does not contain the keyword '{input_word}'."
