import requests
from api.endpoints import ENDPOINTS

class ApiClient:

    @staticmethod
    def register_user(user_data):
        """Регистрирует нового пользователя через API.
            Args:
                user_data (dict): Данные пользователя (email, password, name).
            Returns:
                dict: Ответ API с данными пользователя и токеном."""
        response = requests.post(ENDPOINTS['register'], json=user_data)
        response.raise_for_status()
        return response.json()

    @staticmethod
    def login(email, password):
        """Авторизует пользователя через API.
            Args:
                email (str): Email пользователя.
                password (str): Пароль пользователя.
            Returns:
                dict: Ответ API с токеном доступа."""
        response = requests.post(ENDPOINTS['login'], json={"email": email, "password": password})
        response.raise_for_status()
        return response.json()

    @staticmethod
    def delete_user(token):
        """Удаляет пользователя через API.
            Args:
                token (str): Токен авторизации пользователя.
            Returns:
                int: HTTP-статус код ответа."""
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        response = requests.delete(ENDPOINTS['delete_user'], headers=headers)
        return response.status_code

    @staticmethod
    def safe_delete_user(email, password, original_token=None):
        """Безопасное удаление пользователя с попыткой перелогина.
            Args:
                email (str): Email пользователя.
                password (str): Пароль пользователя.
                original_token (str, optional): Токен авторизации. Defaults to None."""
        if original_token:
            status_code = ApiClient.delete_user(original_token)
            if status_code != 403:
                return
        try:
            login_data = ApiClient.login(email, password)
            ApiClient.delete_user(login_data['accessToken'])
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 403:
                print(f"Ошибка: Пользователь {email} уже удален или неверные учетные данные")
            else:
                raise