import allure
from locators.personal_account import PersonalAccountLocators
from pages.base_pages import BasePage


class PersonalAccountPage(BasePage):

    @allure.step("Кликнуть по кнопке 'Личный кабинет'.")
    def click_personal_account_button(self):
        self.click_element(PersonalAccountLocators.PERSONAL_CABINET_BTN)

    @allure.step("Заполнить поле Email.")
    def fill_email_field(self, email):
        self.fill_field(PersonalAccountLocators.EMAIL_FIELD, email)

    @allure.step("Заполнить поле Пароль.")
    def fill_password_field(self, password):
        self.fill_field(PersonalAccountLocators.PASSWORD_FIELD, password)

    @allure.step("Кликнуть по кнопке 'Войти'.")
    def click_login_button(self):
        self.click_element(PersonalAccountLocators.LOGIN_BTN)

    @allure.step("Кликнуть по кнопке 'История заказов'.")
    def click_order_history_button(self):
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_BTN)

    @allure.step("Кликнуть по кнопке 'Выход'.")
    def click_logout_button(self):
        self.click_element(PersonalAccountLocators.LOGOUT_BTN)