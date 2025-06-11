from selenium.webdriver.support import expected_conditions
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
        self.wait.until(
            expected_conditions.visibility_of_element_located(OrderFeedSectionLocators.ORDER_ID_WINDOW)
        )
        self.click_element(MainFunctionalityLocators.CROSS_BTN)

    @allure.step("Проверить видимость модального окна с деталями заказа.")
    def is_order_details_visible(self):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(OrderFeedSectionLocators.ORDER_DETAILS_WINDOW)
        )

    @allure.step("Получить количество заказов за все время.")
    def get_all_time_orders_count(self):
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderFeedSectionLocators.COMPLETED_ALL_TIME)
        )
        return int(element.text)

    @allure.step("Получить количество заказов за сегодня.")
    def get_completed_orders_today_count(self):
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderFeedSectionLocators.COMPLETED_TODAY)
        )
        return int(element.text)

    @allure.step("Получить номер последнего заказа из истории.")
    def get_order_number_history(self):
        element = self.wait.until(
            expected_conditions.visibility_of_element_located
            (OrderFeedSectionLocators.ORDER_ID_HISTORY)
        )
        return str(element.text).lstrip('#')

    @allure.step("Получить номер заказа из ленты заказов.")
    def get_order_number_in_order_feed(self):
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderFeedSectionLocators.ID_LAST_ORDER)
        )
        return str(element.text).lstrip('#')

    @allure.step("Получить номер заказа из разделе 'В работе'.")
    def get_order_number_in_progress(self):
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(
                OrderFeedSectionLocators.ORDER_IN_PROGRESS
            )
        )
        return str(element.text)