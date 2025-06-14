import allure
from urls import BASE_URL
from pages.order_feed_section_page import OrderFeedSectionPage
from pages.main_functionality_page import MainFunctionalityPage


@allure.suite("Лента заказов.")
class TestOrderFeedSection:

    @allure.title("Успешное отображение деталей заказа.")
    @allure.description("Тест для проверки открытия модального окна с деталями заказа.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_order_details_success(self, browser):
        with allure.step("Инициализировать страницы."):
            order_page = OrderFeedSectionPage(browser)
            main_page = MainFunctionalityPage(browser)

        with allure.step("Кликнуть по кнопке 'Лента заказов'."):
            main_page.click_order_feed()

        with allure.step("Кликнуть по заказу в ленте."):
            order_page.click_order()

        with allure.step("Проверить появление модального окна с деталями заказа."):
            assert order_page.is_order_details_visible(), \
                "Модальное окно с деталями заказа не отображается."

    @allure.title("Успешное появление заказа пользователя в ленте заказов.")
    @allure.description("Тест для проверки, что заказ пользователя появляется в ленте заказов.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_user_order_in_feed_order_success(self, logged_in_user, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)
            order_page = OrderFeedSectionPage(browser)

        with allure.step("Добавить ингредиенты в конструктор."):
            main_page.add_ingredient_to_constructor()

        with allure.step("Кликнуть по кнопке 'Оформить заказ'."):
            main_page.click_place_order()

        with allure.step("Получить номер заказа из модального окна."):
            id_order = order_page.get_order_number_from_modal()

        with allure.step("Кликнуть по кнопке 'Закрыть' для закрытия модального окна оформленного заказа."):
            order_page.click_close_order_without_waiting()

        with allure.step("Кликнуть по кнопке 'Лента заказов'."):
            main_page.click_order_feed()

        with allure.step("Получить номер последнего заказа в ленте."):
            orders_in_progress = order_page.get_order_number_in_order_feed()

        with allure.step("Проверить наличие номера созданного заказа в ленте заказов."):
            assert str(id_order) in orders_in_progress, \
                f"ID заказа {id_order} не найден в ленте заказов: {orders_in_progress}"

    @allure.title("Успешное увеличение счетчика 'Выполнено за все время' при оформлении заказа.")
    @allure.description("Тест для проверки увеличения счетчика выполненных заказов за все время при оформлении заказа.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_completed_orders_counter_increase_all_time_success(self, logged_in_user, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)
            order_page = OrderFeedSectionPage(browser)

        with allure.step("Кликнуть по кнопке 'Лента заказов'."):
            main_page.click_order_feed()

        with allure.step("Получить значение счетчика 'Выполнено за все время'."):
            initial_count = order_page.get_all_time_orders_count()

        with allure.step("Кликнуть по кнопке 'Конструктор'."):
            main_page.click_constructor()

        with allure.step("Добавить ингредиенты в конструктор."):
            main_page.add_ingredient_to_constructor()

        with allure.step("Кликнуть по кнопке 'Оформить заказ'."):
            main_page.click_place_order()

        with allure.step("Кликнуть по кнопке 'Закрыть' для закрытия модального окна оформленного заказа."):
            order_page.click_close_order()

        with allure.step("Кликнуть по кнопке 'Лента заказов'."):
            main_page.click_order_feed()

        with allure.step("Получить значение счетчика 'Выполнено за все время'."):
            new_count = order_page.get_all_time_orders_count()

        with allure.step("Проверка увеличение счетчика 'Выполнено за все время'."):
            assert new_count > initial_count, \
                f"Счетчик 'Выполнено за все время' не увеличился. Начальное значение: {initial_count}, Новое значение: {new_count}"

    @allure.title("Успешное увеличение счетчика 'Выполнено за сегодня' при оформлении заказа.")
    @allure.description("Тест для проверки увеличения счетчика выполненных заказов за сегодня при оформлении заказа.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_completed_orders_counter_increase_today_success(self, logged_in_user, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)
            order_page = OrderFeedSectionPage(browser)

        with allure.step("Кликнуть по кнопке 'Лента заказов'."):
            main_page.click_order_feed()

        with allure.step("Получить значение счетчика 'Выполнено за сегодня'."):
            initial_count = order_page.get_completed_orders_today_count()

        with allure.step("Кликнуть по кнопке 'Конструктор'."):
            main_page.click_constructor()

        with allure.step("Добавить ингредиенты в конструктор."):
            main_page.add_ingredient_to_constructor()

        with allure.step("Кликнуть по кнопке 'Оформить заказ'."):
            main_page.click_place_order()

        with allure.step("Кликнуть по кнопке 'Закрыть' для закрытия модального окна оформленного заказа."):
            order_page.click_close_order()

        with allure.step("Кликнуть по кнопке 'Лента заказов'."):
            order_page.click_order_feed()

        with allure.step("Получить значение счетчика 'Выполнено за сегодня'."):
            new_count = order_page.get_completed_orders_today_count()

        with allure.step("Проверить увеличение счетчика 'Выполнено за сегодня'."):
            assert new_count > initial_count, \
                f"Счетчик 'Выполнено за сегодня' не увеличился. Начальное значение: {initial_count}, Новое значение: {new_count}"

    @allure.title("Успешное отображение оформленного заказа в разделе 'В работе'.")
    @allure.description("Тест для проверки отображение оформленного заказа в разделе 'В работе'.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_order_number_appears_in_progress_section_success(self, logged_in_user, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)
            order_page = OrderFeedSectionPage(browser)

        with allure.step("Добавить ингредиенты в конструктор."):
            main_page.add_ingredient_to_constructor()

        with allure.step("Кликнуть по кнопке 'Оформить заказ'."):
            main_page.click_place_order()

        with allure.step("Получить номер заказа из модального окна."):
            id_order = order_page.get_order_number_from_modal()

        with allure.step("Кликнуть по кнопке 'Закрыть' для закрытия модального окна оформленного заказа."):
            order_page.click_close_order_without_waiting()

        with allure.step("Кликнуть по кнопке 'Лента заказов'."):
            main_page.click_order_feed()

        with allure.step("Получить номер заказа в разделе 'В работе'."):
            orders_in_progress = order_page.get_order_number_in_progress()

        with allure.step("Проверить наличие номера созданного заказа в разделе 'В работе'."):
            assert str(id_order) in orders_in_progress, \
                f"ID заказа {id_order} не найден в разделе 'В работе': {orders_in_progress}"