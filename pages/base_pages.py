from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import WebDriverException
import allure
import time


class BasePage:

    def __init__(self, driver):
        """Инициализация базовой страницы.
            Args: driver: WebDriver экземпляр"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Кликнуть по элементу.")
    def click_element(self, locator):
        try:
            element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
            element.click()
        except WebDriverException:
            time.sleep(3)
            element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
            element.click()

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
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element is not None

    @allure.step("Проверить отсутствие элемента.")
    def is_element_not_visible(self, locator):
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    @allure.step("Найти элемент.")
    def find_element(self, locator):
        return self.driver.find_element(*locator)