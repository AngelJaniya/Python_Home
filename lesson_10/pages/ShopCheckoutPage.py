from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class ShopCheckoutPage:
    """Класс Page Object для страницы оформления заказа (Checkout)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует класс страницы оформления заказа.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    def fill_form(self) -> None:
        """Заполняет форму персональных данных (имя, фамилия, индекс) и
        переходит к следующему шагу.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.change_input('#first-name', "Helga")
        self.change_input('#last-name', "Odintsova")
        self.change_input('#postal-code', "0144")
        self.click('#continue')

    def get_total(self) -> str:
        """Получает итоговую сумму заказа (Total) со страницы.

        Returns:
            str: Строка, содержащая только числовое значение
                итоговой суммы (без текста).
        """
        result = self.text('.summary_total_label')
        return result.split(" ")[1]

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

    def text(self, selector: str) -> str:
        """Ожидает появления элемента и возвращает его текстовое содержимое.

        Args:
            selector (str): CSS-селектор элемента.

        Returns:
            str: Текстовое содержимое найденного элемента.
        """
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        return self.wait.until(pres).text

    def click(self, selector: str) -> None:
        """Ожидает появления элемента на странице и кликает по нему.

        Args:
            selector (str): CSS-селектор элемента.

        Returns:
            None: Метод ничего не возвращает.
        """
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()
