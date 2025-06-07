from locators.personal_account import PersonalAccountLocators
from pages.base_pages import BasePage


class PersonalAccountPage(BasePage):

    def click_personal_account_button(self):
        """Клик по кнопке 'Личный кабинет' в шапке сайта."""
        self.click_element(PersonalAccountLocators.PERSONAL_CABINET_BTN)

    def fill_email_field(self, email):
        """Заполняет поле 'Email' в формах входа/регистрации.
            Args: email (str): Email для ввода"""
        self.fill_field(PersonalAccountLocators.EMAIL_FIELD, email)

    def fill_password_field(self, password):
        """Заполняет поле 'Пароль' в формах входа/регистрации.
            Args: password (str): Пароль для ввода"""
        self.fill_field(PersonalAccountLocators.PASSWORD_FIELD, password)

    def click_login_button(self):
        """Клик по кнопке 'Войти' в форме входа."""
        self.click_element(PersonalAccountLocators.LOGIN_BTN)

    def click_order_history_button(self):
        """Клик по кнопке 'История заказов' в личном кабинете."""
        self.click_element(PersonalAccountLocators.ORDER_HISTORY_BTN)

    def click_logout_button(self):
        """Клик по кнопке 'Выход' в личном кабинете."""
        self.click_element(PersonalAccountLocators.LOGOUT_BTN)