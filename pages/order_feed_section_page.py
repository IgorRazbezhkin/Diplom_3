import allure
from locators.order_feed_section import OrderFeedSectionLocators
from locators.main_functionality import MainFunctionalityLocators
from pages.base_pages import BasePage


class OrderFeedSectionPage(BasePage):

    @allure.step("Кликнуть по заказу в ленте.")
    def click_order(self):
        self.click_element(OrderFeedSectionLocators.ORDER)

    @allure.step("Кликнуть по кнопке 'Лента Заказов'.")
    def click_order_feed(self):
        self.click_element(MainFunctionalityLocators.ORDER_FEED)

    @allure.step("Закрыть модальное окно с деталями заказа.")
    def click_close_order(self):
        self.click_element(MainFunctionalityLocators.CROSS_BTN)

    @allure.step("Закрыть модальное окно с деталями заказа без ожидания.")
    def click_close_order_without_waiting(self):
        self.quick_click_element(MainFunctionalityLocators.CROSS_BTN)

    @allure.step("Проверить видимость модального окна с деталями заказа.")
    def is_order_details_visible(self):
        return self.is_element_visible(OrderFeedSectionLocators.ORDER_DETAILS_WINDOW)

    @allure.step("Получить количество заказов за все время.")
    def get_all_time_orders_count(self):
        count_text = self.get_element_text(OrderFeedSectionLocators.COMPLETED_ALL_TIME)
        return int(count_text)

    @allure.step("Получить количество заказов за сегодня.")
    def get_completed_orders_today_count(self):
        count_text = self.get_element_text(OrderFeedSectionLocators.COMPLETED_TODAY)
        return int(count_text)

    @allure.step("Получить номер последнего заказа.")
    def get_order_number_from_modal(self):
        self.wait_for_order_number_update(OrderFeedSectionLocators.ORDER_ID_WINDOW)
        return self.get_element_text(OrderFeedSectionLocators.ORDER_ID_WINDOW)

    @allure.step("Получить номер заказа из ленты заказов.")
    def get_order_number_in_order_feed(self):
        order_text = self.get_element_text(OrderFeedSectionLocators.ID_LAST_ORDER)
        return str(order_text).lstrip('#')

    @allure.step("Получить номер заказа из раздела 'В работе'.")
    def get_order_number_in_progress(self):
        order_text = self.get_element_text(OrderFeedSectionLocators.ORDER_IN_PROGRESS)
        return str(order_text)