from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class ShopMainPage:
    """Класс Page Object для главной страницы магазина (каталога товаров)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует класс главной страницы магазина.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера Selenium
                для управления браузером.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 4)

    def add(self, name: str) -> None:
        """Добавляет товар в корзину по его названию.

        Args:
            name (str): Часть ID товара для формирования селектора.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.click('#add-to-cart-sauce-labs-' + name)

    def go_to_basket(self) -> None:
        """Осуществляет переход в корзину покупок.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.click('.shopping_cart_link')

    def click(self, selector: str) -> None:
        """Ожидает появления элемента на странице и кликает по нему.

        Args:
            selector (str): CSS-селектор элемента, по которому нужно кликнуть.

        Returns:
            None: Метод ничего не возвращает.
        """
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()
