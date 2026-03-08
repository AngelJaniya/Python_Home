from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class ShopBasketPage:
    """Класс Page Object для страницы корзины покупок."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует класс страницы корзины.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    def checkout(self) -> None:
        """Нажимает кнопку перехода к оформлению заказа (Checkout).

        Returns:
            None: Метод ничего не возвращает.
        """
        self.click('#checkout')

    def click(self, selector: str) -> None:
        """Ожидает появления элемента на странице и кликает по нему.

        Args:
            selector (str): CSS-селектор элемента.

        Returns:
            None: Метод ничего не возвращает.
        """
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()
