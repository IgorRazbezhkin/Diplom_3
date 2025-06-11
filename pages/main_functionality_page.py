from selenium.webdriver.support import expected_conditions
from locators.main_functionality import MainFunctionalityLocators
from pages.base_pages import BasePage


class MainFunctionalityPage(BasePage):

    def click_constructor(self):
        """Клик по кнопке 'Конструктор' в шапке сайта."""
        self.click_element(MainFunctionalityLocators.CONSTRUCTOR)

    def click_order_feed(self):
        """Клик по кнопке 'Лента Заказов' в шапке сайта."""
        self.click_element(MainFunctionalityLocators.ORDER_FEED)

    def click_place_order(self):
        """Клик по кнопке 'Оформить заказ'."""
        self.click_element(MainFunctionalityLocators.CREATE_ORDER_BTN)

    def click_ingredient(self):
        """Открывает модальное окно с деталями ингредиента."""
        self.click_element(MainFunctionalityLocators.INGREDIENT)

    def wait_for_ingredient_details_visible(self):
        """Ожидает появления модального окна с деталями ингредиента."""
        self.wait.until(
            expected_conditions.visibility_of_element_located(
                MainFunctionalityLocators.INGREDIENT_DETAILS_WINDOW)
        )

    def close_ingredient_details(self):
        """Закрывает модальное окно с деталями ингредиента."""
        self.click_element(MainFunctionalityLocators.CROSS_BTN)

    def wait_for_ingredient_details_hidden(self):
        """Ожидает скрытия модального окна с деталями ингредиента."""
        self.wait.until(
            expected_conditions.invisibility_of_element_located(
                MainFunctionalityLocators.INGREDIENT_DETAILS_WINDOW)
        )

    def is_ingredient_details_visible(self):
        """Проверяет видимость модального окна с деталями ингредиента. Returns:
            bool: True если окно видимо, иначе False"""
        return self.is_element_visible(MainFunctionalityLocators.INGREDIENT_DETAILS_WINDOW)

    def is_ingredient_details_hidden(self):
        """Проверяет, что модальное окно с деталями ингредиента скрыто. Returns:
            bool: True если окно не видимо, иначе False"""
        return self.is_element_not_visible(MainFunctionalityLocators.INGREDIENT_DETAILS_WINDOW)

    def add_ingredient_to_constructor(self):
        """Добавляет ингредиент в конструктор бургеров через drag-and-drop."""
        ingredient = self.wait.until(
            expected_conditions.visibility_of_element_located(MainFunctionalityLocators.INGREDIENT)
        )
        target_field = self.wait.until(
            expected_conditions.visibility_of_element_located(MainFunctionalityLocators.FIELD_FOR_ADDING_INGREDIENTS)
        )
        self.drag_and_drop(ingredient, target_field)

    def drag_and_drop(self, source_element, target_element):
        """Эмулирует перетаскивание элемента через JavaScript.
            Args:
                source_element: Элемент, который нужно перетащить
                target_element: Целевой элемент, куда нужно перетащить"""
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

    def get_ingredient_count(self):
        """Получает значение счетчика у ингредиента. Returns:
            int: Числовое значение счетчика"""
        counter = self.wait.until(expected_conditions.visibility_of_element_located(MainFunctionalityLocators.INGREDIENT_COUNTER))
        return int(counter.text)

    def wait_for_ingredient_count_change(self, initial_count):
        """Ожидает изменения счетчика ингредиента.
        Args: initial_count (int): Начальное значение счетчика."""
        def count_changed(_):
            current_count = self.get_ingredient_count()
            return current_count != initial_count
        self.wait.until(count_changed)

    def wait_for_order_placed(self):
        """Ожидает появления модального окна оформленного заказа."""
        self.wait.until(
            expected_conditions.visibility_of_element_located(
                MainFunctionalityLocators.ORDER_FEED_WINDOW)
        )

    def is_order_placed_successfully(self):
        """Проверяет успешность оформления заказа по появлению модального окна. Returns:
            bool: True если окно заказа появилось, иначе False"""
        return self.is_element_visible(MainFunctionalityLocators.ORDER_FEED_WINDOW)