import allure

from source_code.pages.favorites.favorites_page import FavoritesPage
from source_code.pages.main.main_page import MainPage


class TestFavoritesPage:
    @allure.feature('Favorites')
    @allure.story('Add product to favorites')
    def test_add_to_favorites(self, driver):
        main_page = MainPage(driver)
        favorite_page = FavoritesPage(driver)

        main_page.add_to_favorites('lash')
        with allure.step('Ensure that quantity of items in favorites is displayed as expected'):
            assert main_page.favorites_quantity_icon.text() == '1', 'The quantity of items in Favorites is displayed incorrectly.'
        with allure.step('Ensure that favorites heart button color is pink'):
            favorites_heart_button_color = main_page.favorites_heart_button.extract_css_property_of_element('fill')
            assert favorites_heart_button_color == 'rgb(232, 0, 128)', f'The color of the favorites heart button does not match the expected one.'
        main_page.go_to_favorites_page()
        with allure.step('Ensure that product is added to favorites'):
            favorite_page.products_in_favorites.assert_element()
        favorite_page.delete_one_item()


    @allure.feature('Favorites')
    @allure.story('Delete product from favorites')
    def test_delete_from_favorites(self, driver):
        main_page = MainPage(driver)
        favorite_page = FavoritesPage(driver)

        main_page.add_to_favorites('lash')
        with allure.step('Clear search string'):
            main_page.search_string.clear()

        main_page.add_to_favorites('lips')
        main_page.go_to_favorites_page()

        with allure.step('Ensure that 2 products are added to favorites'):
            items_quantity = favorite_page.count_items()
            assert items_quantity == 2, 'Expected 2 items in Favorites, but found a different quantity.'
        favorite_page.delete_one_item()
        favorite_page.removed_item.wait_until_invisibility()

        with allure.step('Ensure that 1 product is present in favorites'):
            items_quantity_new = favorite_page.count_items()
            assert items_quantity_new == 1, "Expected 1 item in Favorites, but found a different quantity."
        favorite_page.delete_one_item()

        with allure.step('Ensure that favorites page is empty'):
            assert favorite_page.empty_favorites_notification.text() == 'Na tej liście życzeń nie ma żadnych produktów.', 'Favorites page is not empty.'
