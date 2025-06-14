import allure
from locators.password_recovery import PasswordRecoveryLocators
from pages.base_pages import BasePage


class PasswordRecoveryPage(BasePage):

    @allure.step("Кликнуть по ссылке 'Восстановить пароль'.")
    def click_recover_password_link(self):
        self.click_element(PasswordRecoveryLocators.RESTORE_PASSWORD_BTN)

    @allure.step("Переключить видимость пароля.")
    def toggle_password_visibility(self):
        self.click_element(PasswordRecoveryLocators.SHOW_HIDE_PASSWORD_BTN)

    @allure.step("Проверить выделение поля пароля.")
    def is_password_field_highlighted(self):
        element = self.wait_for_element_visible(PasswordRecoveryLocators.FOCUSED_FIELD_PASSWORD)
        return "input__placeholder-focused" in self.get_element_attribute(element, "class")

    @allure.step("Кликнуть по кнопке 'Восстановить'.")
    def click_restore_button(self):
        self.click_element(PasswordRecoveryLocators.RESTORE_BTN)