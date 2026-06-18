import pytest
from playwright.sync_api import sync_playwright, Page  # Имопртируем класс страницы для аннотации типов


@pytest.fixture  # Объявляем фикстуру, по умолчанию скоуп function
def chromium_page() -> Page:
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        # Передаем страницу для использования в тесте
        yield browser.new_page()
