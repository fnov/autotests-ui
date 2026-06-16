from playwright.sync_api import sync_playwright, expect

with (sync_playwright() as playwright):
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    registration_button = page.get_by_test_id('registration-page-registration-button')
    expect(registration_button).to_be_disabled()

    # Хоть можно и через locator.fill(), но далее поля заполняются через page.keyboard.type() для практики уроков 5.5
    email_input = page.get_by_test_id('registration-form-email-input').locator('input')
    email_input.focus()
    page.keyboard.type("user.name@gmail.com")

    username_input = page.get_by_test_id('registration-form-username-input').locator('input')
    username_input.focus()
    page.keyboard.type("username")

    password_input = page.get_by_test_id('registration-form-password-input').locator('input')
    password_input.focus()
    page.keyboard.type("password")

    expect(registration_button).to_be_enabled()
