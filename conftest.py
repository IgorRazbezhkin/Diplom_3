import pytest
from selenium import webdriver
from urls import BASE_URL, LOGIN_PAGE_URL
from data import name
from helpers import generate_random_password, generate_random_email
from pages.personal_account_page import PersonalAccountPage
from api.client import ApiClient


@pytest.fixture(params=["chrome", "firefox"])
def browser(request):
    """Фикстура для инициализации браузера (Chrome/Firefox) и его закрытия после теста."""
    driver = webdriver.Chrome() if request.param == "chrome" else webdriver.Firefox()
    driver.maximize_window()
    driver.get(BASE_URL)
    yield driver
    driver.quit()

@pytest.fixture
def registered_user():
    """Фикстура для регистрации пользователя через API и его удаления после теста."""
    user_data = {
        "email": generate_random_email(),
        "password": generate_random_password(),
        "name": name
    }
    response = ApiClient.register_user(user_data)
    yield user_data
    ApiClient.safe_delete_user(
        email=user_data['email'],
        password=user_data['password'],
        original_token=response.get('accessToken')
    )

@pytest.fixture
def logged_in_user(browser, registered_user):
    """Фикстура для авторизации пользователя через UI."""
    account_page = PersonalAccountPage(browser)
    account_page.driver.get(LOGIN_PAGE_URL)
    account_page.fill_email_field(registered_user['email'])
    account_page.fill_password_field(registered_user['password'])
    account_page.click_login_button()
    return registered_user