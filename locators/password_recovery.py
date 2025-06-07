from selenium.webdriver.common.by import By


class PasswordRecoveryLocators:

    RESTORE_PASSWORD_BTN = (By.CSS_SELECTOR, "a[href='/forgot-password']")
    RESTORE_BTN = (By.CSS_SELECTOR, "form button")
    SHOW_HIDE_PASSWORD_BTN = (By.CSS_SELECTOR, "div.input__icon-action")
    FOCUSED_FIELD_PASSWORD = (By.CSS_SELECTOR, "label.input__placeholder-focused")