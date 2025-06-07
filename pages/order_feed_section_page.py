from selenium.webdriver.support import expected_conditions
from locators.order_feed_section import OrderFeedSectionLocators
from locators.main_functionality import MainFunctionalityLocators
from pages.base_pages import BasePage


class OrderFeedSectionPage(BasePage):

    def click_order(self):
        """Клик по первому заказу в ленте заказов."""
        return self.click_element(OrderFeedSectionLocators.ORDER)

    def click_order_feed(self):
        """Клик по кнопке 'Лента Заказов'."""
        return self.click_element(MainFunctionalityLocators.ORDER_FEED)

    def click_close_order(self):
        """Закрывает модальное окно с деталями заказа."""
        self.wait.until(
            expected_conditions.visibility_of_element_located(OrderFeedSectionLocators.ORDER_ID_WINDOW)
        )
        return self.click_element(MainFunctionalityLocators.CROSS_BTN)

    def is_order_details_visible(self):
        """Проверяет видимость модального окна с деталями заказа. Returns:
            WebElement: Видимый элемент окна заказа"""
        return self.wait.until(
            expected_conditions.visibility_of_element_located(OrderFeedSectionLocators.ORDER_DETAILS_WINDOW)
        )

    def get_all_time_orders_count(self):
        """Получает количество заказов за все время. Returns:
            int: Число заказов"""
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderFeedSectionLocators.COMPLETED_ALL_TIME)
        )
        return int(element.text)

    def get_completed_orders_today_count(self):
        """Получает количество заказов за сегодня. Returns:
            int: Число заказов"""
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderFeedSectionLocators.COMPLETED_TODAY)
        )
        return int(element.text)

    def get_order_number_history(self):
        """Получает номер последнего заказа из истории заказов. Returns:
            str: Номер заказа (без символа #)"""
        element = self.wait.until(
            expected_conditions.visibility_of_element_located
            (OrderFeedSectionLocators.ORDER_ID_HISTORY)
        )
        return str(element.text).lstrip('#')

    def get_order_number_in_order_feed(self):
        """Получает номер заказа из ленты заказов. Returns:
            str: Номер заказа (без символа #)"""
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderFeedSectionLocators.ID_LAST_ORDER)
        )
        return str(element.text).lstrip('#')

    def get_order_number_in_progress(self):
        """Получает номер заказа в разделе 'В работе'. Returns:
            str: Номер заказа"""
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderFeedSectionLocators.ORDER_IN_PROGRESS
            )
        )
        return str(element.text)