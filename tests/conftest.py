import pytest
from playwright.sync_api import Page, Playwright  # Имопртируем класс страницы для аннотации типов


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    # Передаем страницу для использования в тесте
    yield browser.new_page()
