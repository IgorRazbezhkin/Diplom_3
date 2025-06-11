import allure
from urls import BASE_URL, LOGIN_PAGE_URL, RECOVERY_PAGE_URL, PASSWORD_RESET_PAGE_URL
from pages.password_recovery_page import PasswordRecoveryPage
from pages.personal_account_page import PersonalAccountPage


@allure.suite("Восстановление пароля.")
class TestPasswordRecovery:

    @allure.title("Успешный переход на страницу восстановления пароля.")
    @allure.description("Тест для проверки перехода на страницу восстановления пароля.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_navigate_to_recovery_page_success(self, browser):
        with allure.step("Инициализировать страницы."):
            recovery_page = PasswordRecoveryPage(browser)
            account_page = PersonalAccountPage(browser)

        with allure.step("Кликнуть по кнопке 'Личный кабинет'."):
            account_page.click_personal_account_button()

        with allure.step("Ожидать перехода на страницу личного кабинета."):
            account_page.wait_for_url(LOGIN_PAGE_URL)

        with allure.step("Кликнуть по ссылке 'Восстановить пароль'."):
            recovery_page.click_recover_password_link()

        with allure.step("Ожидание перехода на страницу восстановления пароля."):
            recovery_page.wait_for_url(RECOVERY_PAGE_URL)

        with allure.step("Проверить текущий URL."):
            assert recovery_page.get_current_url() == RECOVERY_PAGE_URL, \
                f"Ожидался URL: {RECOVERY_PAGE_URL}, Фактический URL: {recovery_page.get_current_url()}"

    @allure.title("Успешный переход на страницу сброса пароля по email.")
    @allure.description("Тест для проверки перехода на страницу сброса пароля по email.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_password_recovery_with_email_success(self, registered_user, browser):
        with allure.step("Инициализировать страницы."):
            recovery_page = PasswordRecoveryPage(browser)
            account_page = PersonalAccountPage(browser)

        with allure.step("Получить email зарегистрированного пользователя."):
            email = registered_user['email']

        with allure.step("Кликнуть по кнопке 'Личный кабинет'."):
            account_page.click_personal_account_button()

        with allure.step("Кликнуть по ссылке 'Восстановить пароль'."):
            recovery_page.click_recover_password_link()

        with allure.step("Заполнить поле email."):
            account_page.fill_email_field(email)

        with allure.step("Кликнуть по кнопке 'Восстановить'."):
            recovery_page.click_restore_button()

        with allure.step("Ожидать перехода на страницу сброса пароля."):
            recovery_page.wait_for_url(PASSWORD_RESET_PAGE_URL)

        with allure.step("Проверить текущий URL."):
            assert recovery_page.get_current_url() == PASSWORD_RESET_PAGE_URL, \
                f"Ожидался URL: {PASSWORD_RESET_PAGE_URL}, Фактический URL: {recovery_page.get_current_url()}"

    @allure.title("Успешная активация подсветки поля 'пароль'.")
    @allure.description("Тест для проверки функционала подсветки поля 'пароль' при клике на него.")
    @allure.link(BASE_URL, name="Тестовый сайт")

    def test_password_visibility_toggle_success(self, registered_user, browser):
        with allure.step("Инициализировать страницы."):
            recovery_page = PasswordRecoveryPage(browser)
            account_page = PersonalAccountPage(browser)

        with allure.step("Получить email зарегистрированного пользователя."):
            email = registered_user['email']

        with allure.step("Кликнуть по кнопке 'Личный кабинет'."):
            account_page.click_personal_account_button()

        with allure.step("Кликнуть по ссылке 'Восстановить пароль'."):
            recovery_page.click_recover_password_link()

        with allure.step("Заполнить поле email."):
            account_page.fill_email_field(email)

        with allure.step("Кликнуть по кнопке 'Восстановить'."):
            recovery_page.click_restore_button()

        with allure.step("Кликнуть на иконку глаза для показа/скрытия пароля."):
            recovery_page.toggle_password_visibility()

        with allure.step("Проверить активацию поля 'пароль'(поле подсвечивается)."):
            assert recovery_page.is_password_field_highlighted(), \
                "Поле пароля не выделено после переключения видимости."