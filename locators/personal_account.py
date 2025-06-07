from selenium.webdriver.common.by import By


class PersonalAccountLocators:

    PERSONAL_CABINET_BTN = (By.CSS_SELECTOR, "a[href='/account']")
    EMAIL_FIELD = (By.CSS_SELECTOR, "fieldset:nth-child(1) input")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "fieldset:nth-child(2) input")
    LOGIN_BTN = (By.CSS_SELECTOR, "form button")
    ORDER_HISTORY_BTN = (By.XPATH, ".//a[contains(@class, 'Account_link__2ETsJ') and text() = 'История заказов']")
    LOGOUT_BTN = (By.CSS_SELECTOR, "nav ul li:nth-child(3) button")