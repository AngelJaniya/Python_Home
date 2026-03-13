from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver


class FormPage:
    """Класс Page Object для взаимодействия со страницей веб-формы (Data
    Types)."""

    def __init__(self, driver: WebDriver) -> None:
        """Инициализирует класс страницы формы.

        Args:
            driver (WebDriver): Экземпляр веб-драйвера Selenium.

        Returns:
            None: Метод ничего не возвращает.
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)
        self.fields = {
            'first-name': "Иван",
            'last-name': "Петров",
            'address': "Ленина, 55-3",
            'zip-code': "",
            'city': "Москва",
            'country': "Россия",
            'e-mail': "test@skypro.com",
            'phone': "+7985899998787",
            'job-position': "QA",
            'company': "SkyPro"
        }

    def change_input(self, name: str, value: str) -> None:
        """Находит поле ввода по атрибуту 'name' и вводит в него значение.

        Args:
            name (str): Значение атрибута 'name' поля ввода.
            value (str): Текст, который необходимо ввести.

        Returns:
            None: Метод ничего не возвращает.
        """
        selector = 'input[name="' + name + '"]'
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).send_keys(value)

    def submit_form(self) -> None:
        """Нажимает кнопку отправки формы (Submit).

        Returns:
            None: Метод ничего не возвращает.
        """
        selector = 'button[type="submit"]'
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        self.wait.until(pres).click()

    def check_result(self, name: str, cls: str) -> None:
        """Проверяет, содержит ли элемент с указанным ID определенный CSS-
        класс. Используется assert, поэтому в случае неудачи тест упадет.

        Args:
            name (str): Значение атрибута 'id' элемента для проверки.
            cls (str): CSS-класс, наличие которого ожидается у элемента.

        Returns:
            None: Метод ничего не возвращает (может выбросить AssertionError).
        """
        selector = '#' + name
        pres = EC.presence_of_element_located((By.CSS_SELECTOR, selector))
        classes = self.wait.until(pres).get_attribute('class')
        assert cls in classes

    def open(self) -> None:
        """Открывает тестовую веб-страницу с формой в браузере.

        Returns:
            None: Метод ничего не возвращает.
        """
        page = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"
        self.driver.get(page)

    def fill_form(self) -> None:
        """Заполняет все поля формы, используя словарь 'self.fields'.

        Returns:
            None: Метод ничего не возвращает.
        """
        for f, v in self.fields.items():
            self.change_input(f, v)

    def check_form_submission(self) -> None:
        """Проверяет корректность подсветки полей после отправки формы. Ожидает
        зеленую подсветку для заполненных полей и красную для пустого 'zip-
        code'.

        Returns:
            None: Метод ничего не возвращает.
        """
        fields = ['first-name', 'last-name', 'address', 'e-mail', 'phone',
                  'city', 'country', 'job-position', 'company']
        for f in fields:
            self.check_result(f, 'alert-success')

        self.check_result('zip-code', 'alert-danger')
