from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
import allure
from locators.personal_account import PersonalAccountLocators


class BasePage:

    def __init__(self, driver):
        """Инициализация базовой страницы.
            Args: driver: WebDriver экземпляр"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    @allure.step("Кликнуть по элементу.")
    def click_element(self, locator):
        element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self.wait_for_overlay_to_disappear()
        try:
            element.click()
        except Exception:
            try:
                ActionChains(self.driver).move_to_element(element).click().perform()
            except Exception:
                self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Ожидать исчезновения оверлея.")
    def wait_for_overlay_to_disappear(self):
        try:
            self.wait.until(expected_conditions.invisibility_of_element_located(PersonalAccountLocators.MODAL_OVERLAY))
        except:
            pass

    @allure.step("Кликнуть по элементу без ожидания.")
    def quick_click_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step("Заполнить поля.")
    def fill_field(self, locator, text):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    @allure.step("Получить текущий URL.")
    def get_current_url(self):
        return self.driver.current_url

    @allure.step("Ожидать URL.")
    def wait_for_url(self, url):
        self.wait.until(expected_conditions.url_to_be(url))

    @allure.step("Проверить видимость элемента.")
    def is_element_visible(self, locator):
        try:
            element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
            return element is not None
        except:
            return False

    @allure.step("Проверить отсутствие элемента.")
    def is_element_not_visible(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Найти элемент.")
    def find_element(self, locator):
        return self.driver.find_element(*locator)

    @allure.step("Получить текст элемента.")
    def get_element_text(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element.text

    @allure.step("Выполнить JavaScript.")
    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)

    @allure.step("Ожидать видимости элемента.")
    def wait_for_element_visible(self, locator):
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element

    @allure.step("Получить атрибут элемента.")
    def get_element_attribute(self, element, attribute):
        return element.get_attribute(attribute)

    @allure.step("Ожидать номер оформленного заказа.")
    def wait_for_order_number_update(self, locator, initial_value="9999"):
        def order_number_updated(_):
            current_value = self.get_element_text(locator)
            return current_value and current_value != initial_value
        self.wait.until(order_number_updated)