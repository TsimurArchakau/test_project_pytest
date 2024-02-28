import allure

from source_code.pages.cart.cart_page import CartPage
from source_code.pages.main.main_page import MainPage


class TestCartPage:
    @allure.feature('Cart')
    @allure.story('Add item to cart')
    def test_add_to_cart(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)

        main_page.add_to_cart('lips')
        main_page.go_to_cart_page()

        with allure.step('Ensure that added item is present in cart'):
            cart_page.items_in_cart.assert_element()
            assert cart_page.notification_in_cart.text() == 'TWÓJ KOSZYK (1 PRODUKT)', 'The notification text above the products does not match the expected one.'
        cart_page.delete_one_item()
        cart_page.first_item_in_cart.wait_until_invisibility()

    @allure.feature('Cart')
    @allure.story('Change quantity of item in cart')
    def test_change_items_quantity_in_cart(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)

        main_page.add_to_cart('glow')
        main_page.go_to_cart_page()
        first_total = cart_page.total()

        with allure.step('Click "+" button'):
            cart_page.plus_button.click()

        with allure.step('Ensure that one more item added to cart and total cost are doubled'):
            cart_page.notification_in_cart.wait_text_to_be_present('TWÓJ KOSZYK (2 PRODUKTY)')
            second_total = cart_page.total()
            assert second_total == first_total * 2
        cart_page.delete_one_item()
        cart_page.first_item_in_cart.wait_until_invisibility()

    @allure.feature('Cart')
    @allure.story('Delete products from cart')
    def test_delete_products_from_cart(self, driver):
        main_page = MainPage(driver)
        cart_page = CartPage(driver)

        main_page.add_to_cart('lash')
        with allure.step('Click "Continue shopping" button'):
            main_page.continue_shopping_button.click()

        main_page.add_to_cart('krem')
        main_page.go_to_cart_page()

        with allure.step('Ensure that 2 items are added to cart'):
            items_quantity = cart_page.count_items()
            assert items_quantity == 2, 'Expected 2 items in Cart, but found a different quantity.'
        cart_page.delete_one_item()
        cart_page.second_item_in_cart.wait_until_invisibility()
        with allure.step('Ensure that 1 product is present in cart'):
            items_quantity_new = cart_page.count_items()
            assert items_quantity_new == 1, 'Expected 1 item in Cart, but found a different quantity.'
        cart_page.delete_one_item()
        cart_page.first_item_in_cart.wait_until_invisibility()
        with allure.step("Ensure that cart is empty"):
            assert cart_page.empty_cart_notification.text() == 'Twój koszyk jest pusty', 'Cart is not empty.'