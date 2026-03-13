from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class ShopAuthPage:
    """Класс Page Object для страницы авторизации магазина."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует класс страницы авторизации.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    def open(self) -> None:
        """Открывает страницу авторизации магазина в браузере.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.driver.get("https://www.saucedemo.com/")

    def auth(self) -> None:
        """Выполняет вход в систему, заполняя поля логина и пароля стандартными
        тестовыми данными.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.change_input('#user-name', "standard_user")
        self.change_input('#password', "secret_sauce")
        self.click('#login-button')

    def change_input(self, selector: str, value: str) -> None:
        """Ожидает появления поля ввода и вводит в него переданное значение.

        Args:
            selector (str): CSS-селектор поля ввода.
            value (str): Текст для ввода в поле.

        Returns:
            None: Метод ничего не возвращает.
        """
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).send_keys(value)

    def click(self, selector: str) -> None:
        """Ожидает появления элемента на странице и кликает по нему.

        Args:
            selector (str): CSS-селектор элемента.

        Returns:
            None: Метод ничего не возвращает.
        """
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()
