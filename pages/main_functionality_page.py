from selenium.webdriver.support import expected_conditions
import allure
from locators.main_functionality import MainFunctionalityLocators
from pages.base_pages import BasePage


class MainFunctionalityPage(BasePage):

    @allure.step("Кликнуть по кнопке 'Конструктор'.")
    def click_constructor(self):
        self.click_element(MainFunctionalityLocators.CONSTRUCTOR)

    @allure.step("Кликнуть по кнопке 'Лента Заказов'.")
    def click_order_feed(self):
        self.click_element(MainFunctionalityLocators.ORDER_FEED)

    @allure.step("Кликнуть по кнопке 'Оформить заказ'.")
    def click_place_order(self):
        self.click_element(MainFunctionalityLocators.CREATE_ORDER_BTN)

    @allure.step("Кликнуть по ингредиенту.")
    def click_ingredient(self):
        self.click_element(MainFunctionalityLocators.INGREDIENT)

    @allure.step("Ожидать видимости модального окна с деталями ингредиента.")
    def wait_for_ingredient_details_visible(self):
        self.wait.until(
            expected_conditions.visibility_of_element_located(
                MainFunctionalityLocators.INGREDIENT_DETAILS_WINDOW)
        )

    @allure.step("Закрыть модальное окно с деталями ингредиента.")
    def close_ingredient_details(self):
        self.click_element(MainFunctionalityLocators.CROSS_BTN)

    @allure.step("Ожидать скрытия модального окна с деталями ингредиента.")
    def wait_for_ingredient_details_hidden(self):
        self.wait.until(
            expected_conditions.invisibility_of_element_located(
                MainFunctionalityLocators.INGREDIENT_DETAILS_WINDOW)
        )

    @allure.step("Проверить видимость модального окна с деталями ингредиента.")
    def is_ingredient_details_visible(self):
        return self.is_element_visible(MainFunctionalityLocators.INGREDIENT_DETAILS_WINDOW)

    @allure.step("Проверить скрытие модального окна с деталями ингредиента.")
    def is_ingredient_details_hidden(self):
        return self.is_element_not_visible(MainFunctionalityLocators.INGREDIENT_DETAILS_WINDOW)

    @allure.step("Добавить ингредиент в конструктор.")
    def add_ingredient_to_constructor(self):
        ingredient = self.wait.until(
            expected_conditions.visibility_of_element_located(MainFunctionalityLocators.INGREDIENT)
        )
        target_field = self.wait.until(
            expected_conditions.visibility_of_element_located(MainFunctionalityLocators.FIELD_FOR_ADDING_INGREDIENTS)
        )
        self.drag_and_drop(ingredient, target_field)

    @allure.step("Перетащить элемент.")
    def drag_and_drop(self, source_element, target_element):
        js_script = """
        function simulateDragDrop(source, target) {
            const dataTransfer = new DataTransfer();
            const eventOptions = { bubbles: true, cancelable: true, dataTransfer };

            source.dispatchEvent(new DragEvent('dragstart', eventOptions));
            target.dispatchEvent(new DragEvent('drop', eventOptions));
            source.dispatchEvent(new DragEvent('dragend', eventOptions));
        }
        simulateDragDrop(arguments[0], arguments[1]);
        """
        self.driver.execute_script(js_script, source_element, target_element)

    @allure.step("Получить значение счетчика ингредиента.")
    def get_ingredient_count(self):
        counter = self.wait.until(expected_conditions.visibility_of_element_located(MainFunctionalityLocators.INGREDIENT_COUNTER))
        return int(counter.text)

    @allure.step("Ожидать изменения значения счетчика ингредиента.")
    def wait_for_ingredient_count_change(self, initial_count):
        def count_changed(_):
            current_count = self.get_ingredient_count()
            return current_count != initial_count
        self.wait.until(count_changed)

    @allure.step("Ожидать появления модального окна с деталями заказа.")
    def wait_for_order_placed(self):
        self.wait.until(
            expected_conditions.visibility_of_element_located(
                MainFunctionalityLocators.ORDER_FEED_WINDOW)
        )

    @allure.step("Проверить видимость модального окна с деталями заказа для подтверждения оформления заказа.")
    def is_order_placed_successfully(self):
        return self.is_element_visible(MainFunctionalityLocators.ORDER_FEED_WINDOW)