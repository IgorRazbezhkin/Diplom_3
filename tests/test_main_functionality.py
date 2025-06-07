import allure
from urls import BASE_URL, LOGIN_PAGE_URL, ORDER_FEED_PAGE_URL
from pages.main_functionality_page import MainFunctionalityPage
from pages.personal_account_page import PersonalAccountPage
from pages.base_pages import BasePage


@allure.suite("Основная функциональность.")
class TestMainFunctionality:

    @allure.title("Успешный переход на главную страницу по кнопке 'Конструктор'.")
    @allure.description("Тест для проверки перехода на главную страницу по клику на кнопку 'Конструктор'.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_constructor_navigation_success(self, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)
            account_page = PersonalAccountPage(browser)
            base_page = BasePage(browser)

        with allure.step("Кликнуть по кнопке 'Личный кабинет'."):
            account_page.click_personal_account_button()

        with allure.step("Ожидать перехода на страницу личного кабинета."):
            base_page.wait_for_url(LOGIN_PAGE_URL)

        with allure.step("Кликнуть по кнопке 'Конструктор'."):
            main_page.click_constructor()

        with allure.step("Ожидать перехода на главную страницу."):
            base_page.wait_for_url(BASE_URL)

        with allure.step("Проверить текущий URL."):
            assert base_page.get_current_url() == BASE_URL, \
                f"Ожидался URL: {BASE_URL}, Фактический URL: {base_page.get_current_url()}"

    @allure.title("Успешный переход на страницу 'Лента заказов'.")
    @allure.description("Тест для проверки перехода на страницу 'Лента заказов'.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_order_feed_navigation_success(self, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)
            base_page = BasePage(browser)

        with allure.step("Кликнуть по кнопке 'Лента заказов'."):
            main_page.click_order_feed()

        with allure.step("Ожидать перехода на страницу ленты заказов."):
            base_page.wait_for_url(ORDER_FEED_PAGE_URL)

        with allure.step("Проверить текущий URL."):
            assert base_page.get_current_url() == ORDER_FEED_PAGE_URL, \
                f"Ожидался URL: {ORDER_FEED_PAGE_URL}, Фактический URL: {base_page.get_current_url()}"

    @allure.title("Успешное отображения модального окна с деталями ингредиента.")
    @allure.description("Тест для проверки открытия модального окна с деталями ингредиента.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_ingredient_details_success(self, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)

        with allure.step("Кликнуть по ингредиенту."):
            main_page.click_ingredient()

        with allure.step("Ожидать появления модального окна с деталями ингредиента."):
            main_page.wait_for_ingredient_details_visible()

        with allure.step("Проверить появление модального окна с деталями ингредиента."):
            assert main_page.is_ingredient_details_visible(), \
                "Модальное окно с деталями ингредиента не отображается."

    @allure.title("Успешное закрытие модального окна с деталями ингредиента.")
    @allure.description("Тест для проверки закрытия модального окна с деталями ингредиента.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_ingredient_details_closing_success(self, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)

        with allure.step("Кликнуть по ингредиенту."):
            main_page.click_ingredient()

        with allure.step("Ожидать появления модального окна с деталями ингредиента."):
            main_page.wait_for_ingredient_details_visible()

        with allure.step("Кликнуть по кнопке закрытия модального окна с деталями ингредиента."):
            main_page.close_ingredient_details()

        with allure.step("Ожидать скрытия модального окна с деталями ингредиента."):
            main_page.wait_for_ingredient_details_hidden()

        with allure.step("Проверить закрытие модального окна с деталями ингредиента."):
            assert main_page.is_ingredient_details_hidden(), \
                "Модальное окно с деталями ингредиента не закрылось."

    @allure.title("Успешное увеличение счетчика ингредиента при добавлении ингредиента в конструктор.")
    @allure.description("Тест для проверки увеличение счетчика при добавлении ингредиента в конструктор.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_ingredient_counter_increase_success(self, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)

        with allure.step("Получить значение счетчика ингредиента."):
            initial_count = main_page.get_ingredient_count()

        with allure.step("Добавить ингредиент в конструктор."):
            main_page.add_ingredient_to_constructor()

        with allure.step("Ожидать обновления счетчика ингредиента."):
            main_page.wait_for_ingredient_count_change(initial_count)

        with allure.step("Получить значение счетчика ингредиента."):
            new_count = main_page.get_ingredient_count()

        with allure.step("Проверить увеличение счетчика ингредиента."):
            assert new_count > initial_count, \
                f"Счетчик не увеличился. Начальное значение: {initial_count}, Новое значение: {new_count}"

    @allure.title("Успешное оформление заказа авторизованным пользователем.")
    @allure.description("Тест для проверки возможности оформления заказа авторизованным пользователем.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_authorized_user_can_make_order_success(self, logged_in_user, browser):
        with allure.step("Инициализировать страницы."):
            main_page = MainFunctionalityPage(browser)

        with allure.step("Добавить ингредиент в конструктор."):
            main_page.add_ingredient_to_constructor()

        with allure.step("Кликнуть по кнопке 'Оформить заказ'."):
            main_page.click_place_order()

        with allure.step("Ожидать появления модального окна с деталями оформленного заказа."):
            main_page.wait_for_order_placed()

        with allure.step("Проверить появление модального окна с деталями оформленного заказа."):
            assert main_page.is_order_placed_successfully(), \
                "Не удалось оформить заказ."