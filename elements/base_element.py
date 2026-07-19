import allure
from playwright.sync_api import Page, Locator, expect

from tools.logger import get_logger

logger = get_logger("BASE_ELEMENT")  # Инициализируем logger


class BaseElement:
    def __init__(self, page: Page, locator: str, name: str):
        self.page = page
        self.name = name
        self.locator = locator

    @property
    def type_of(self) -> str:
        return "base element"

    # Метод принимает кейворд аргументы (kwargs)
    def get_locator(self, nth: int = 0, **kwargs) -> Locator:  # объект Locator для взаимодействия с элементом
        # Добавляем аргумент nth со значением по умолчанию 0
        # Инициализирует объект локатора, подставляя динамические значения в локатор.
        locator = self.locator.format(**kwargs)
        step = f'Getting locator with "data-testid={locator}" at index "{nth}"'
        with allure.step(step):
            logger.info(step)
            # Возвращаем объект локатора
            # Использовать self.page.locator(locator) если data-testid не стандартизирован в проекте
            return self.page.get_by_test_id(locator).nth(nth)  # Теперь выбираем элемент по индексу

    def click(self, nth: int = 0, **kwargs):
        step = f'Clicking {self.type_of} "{self.name}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            locator.click()

    def check_visible(self, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" is visible'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_be_visible()

    def check_have_text(self, text: str, nth: int = 0, **kwargs):
        step = f'Checking that {self.type_of} "{self.name}" has text "{text}"'
        with allure.step(step):
            locator = self.get_locator(nth, **kwargs)
            logger.info(step)
            expect(locator).to_have_text(text)
