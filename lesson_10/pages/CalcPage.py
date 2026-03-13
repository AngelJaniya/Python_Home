from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class CalcPage:
    """Класс Page Object для взаимодействия со страницей 'Slow Calculator'."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует класс страницы калькулятора.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера Selenium
                для управления браузером.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 45)

    def open(self) -> None:
        """Открывает веб-страницу калькулятора в браузере.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.driver.get(
            "https://bonigarcia.dev/" +
            "selenium-webdriver-java/slow-calculator.html"
        )

    def fill_delay(self) -> None:
        """Находит поле ввода задержки (delay), очищает его и устанавливает
        значение "45".

        Returns:
            None: Метод ничего не возвращает.
        """
        delay_field = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        delay_field.clear()
        delay_field.send_keys("45")

    def fill_form(self) -> None:
        """Вводит математическое выражение "7 + 8 =", нажимая соответствующие
        кнопки на странице.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.driver.find_element(By.XPATH, "//*[text()='7']").click()
        self.driver.find_element(By.XPATH, "//*[text()='+']").click()
        self.driver.find_element(By.XPATH, "//*[text()='8']").click()
        self.driver.find_element(By.XPATH, "//*[text()='=']").click()

    def check_result(self) -> bool:
        """Ожидает появления правильного результата ("15") на экране
        калькулятора.

        Returns:
            bool: Возвращает True, если ожидаемый текст появился
                в элементе за время ожидания (таймаут).
                  Если текст не появится, Selenium выбросит TimeoutException.
        """
        result = self.wait.until(
            EC.text_to_be_present_in_element(
                (By.CSS_SELECTOR, '.screen'), '15'
            )
        )

        return result
