from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import WebDriverException
import time


class BasePage:

    def __init__(self, driver):
        """Инициализация базовой страницы.
            Args: driver: WebDriver экземпляр"""
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_element(self, locator):
        """Клик по элементу с обработкой исключений и повторной попыткой.
            Args: locator: Локатор элемента для клика"""
        try:
            element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
            element.click()
        except WebDriverException:
            time.sleep(3)
            element = self.wait.until(expected_conditions.element_to_be_clickable(locator))
            element.click()

    def fill_field(self, locator, text):
        """Заполняет текстовое поле с предварительной очисткой.
            Args:
                locator: Локатор поля
                text: Текст для ввода"""
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        """Получает текущий URL страницы. Returns:
            str: Текущий URL"""
        return self.driver.current_url

    def wait_for_url(self, url):
        """Ожидает загрузки конкретного URL.
            Args: url: Ожидаемый URL"""
        self.wait.until(expected_conditions.url_to_be(url))

    def is_element_visible(self, locator):
        """Проверяет видимость элемента на странице.
            Args:
                locator: Локатор элемента
            Returns:
                bool: True если элемент видим, иначе False"""
        element = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        return element is not None

    def is_element_not_visible(self, locator):
        """Проверяет, что элемент не видим на странице.
            Args:
                locator: Локатор элемента
            Returns:
                bool: True если элемент не видим, иначе False"""
        return self.wait.until(expected_conditions.invisibility_of_element_located(locator))

    def find_element(self, locator):
        """Находит элемент по локатору.
            Args:
                locator: Локатор элемента
            Returns:
                WebElement: Найденный элемент"""
        return self.driver.find_element(*locator)