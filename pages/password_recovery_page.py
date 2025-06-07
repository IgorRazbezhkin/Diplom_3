from selenium.webdriver.support import expected_conditions
from locators.password_recovery import PasswordRecoveryLocators
from pages.base_pages import BasePage


class PasswordRecoveryPage(BasePage):

    def click_recover_password_link(self):
        """Клик по ссылке 'Восстановить пароль' на странице входа."""
        self.click_element(PasswordRecoveryLocators.RESTORE_PASSWORD_BTN)

    def toggle_password_visibility(self):
        """Переключает видимость пароля (показ/скрытие)."""
        self.click_element(PasswordRecoveryLocators.SHOW_HIDE_PASSWORD_BTN)

    def is_password_field_highlighted(self):
        """Проверяет, выделено ли поле пароля после переключения видимости. Returns:
            bool: True если поле выделено, иначе False"""
        element = self.wait.until(
            expected_conditions.visibility_of_element_located(
                PasswordRecoveryLocators.FOCUSED_FIELD_PASSWORD
            )
        )
        return "input__placeholder-focused" in element.get_attribute("class")

    def click_restore_button(self):
        """Клик по кнопке 'Восстановить' на странице восстановления пароля."""
        self.click_element(PasswordRecoveryLocators.RESTORE_BTN)