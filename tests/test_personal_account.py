import allure
from urls import BASE_URL, LOGIN_PAGE_URL, ACCOUNT_ORDER_HISTORY_URL
from pages.personal_account_page import PersonalAccountPage


@allure.suite("Личный кабинет.")
class TestPersonalAccount:

    @allure.title("Успешный переход на страницу личного кабинета.")
    @allure.description("Тест для проверки перехода на страницу личного кабинета.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_navigate_to_personal_account_success(self, browser):
        with allure.step("Инициализировать страницы."):
            account_page = PersonalAccountPage(browser)

        with allure.step("Кликнуть по кнопке 'Личный кабинет'."):
            account_page.click_personal_account_button()

        with allure.step("Ожидать перехода на страницу личного кабинета."):
            account_page.wait_for_url(LOGIN_PAGE_URL)

        with allure.step("Проверить текущий URL."):
            assert account_page.get_current_url() == LOGIN_PAGE_URL, \
                f"Ожидался URL: {LOGIN_PAGE_URL}, Фактический URL: {account_page.get_current_url()}"

    @allure.title("Успешный переход в историю заказов.")
    @allure.description("Тест для проверки перехода на страницу истории заказов.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_navigate_to_order_history_success(self, logged_in_user, browser):
        with allure.step("Инициализировать страницы."):
            account_page = PersonalAccountPage(browser)

        with allure.step("Кликнуть по кнопке 'Личный кабинет'."):
            account_page.click_personal_account_button()

        with allure.step("Кликнуть по кнопке 'История заказов'."):
            account_page.click_order_history_button()

        with allure.step("Ожидать перехода на страницу истории заказов."):
            account_page.wait_for_url(ACCOUNT_ORDER_HISTORY_URL)

        with allure.step("Проверить текущий URL."):
            assert account_page.get_current_url() == ACCOUNT_ORDER_HISTORY_URL, \
                f"Ожидался URL: {ACCOUNT_ORDER_HISTORY_URL}, Фактический URL: {account_page.get_current_url()}"

    @allure.title("Успешный выход из аккаунта.")
    @allure.description("Тест для проверки выхода из аккаунта по кнопке 'Выход' в личном кабинете.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_logout_from_account_success(self, logged_in_user, browser):
        with allure.step("Инициализировать страницы."):
            account_page = PersonalAccountPage(browser)

        with allure.step("Кликнуть по кнопке 'Личный кабинет'."):
            account_page.click_personal_account_button()

        with allure.step("Кликнуть по кнопке 'Выход'."):
            account_page.click_logout_button()

        with allure.step("Ожидать перехода на страницу входа."):
            account_page.wait_for_url(LOGIN_PAGE_URL)

        with allure.step("Проверить текущий URL."):
            assert account_page.get_current_url() == LOGIN_PAGE_URL, \
                f"Ожидался URL: {LOGIN_PAGE_URL}, Фактический URL: {account_page.get_current_url()}"