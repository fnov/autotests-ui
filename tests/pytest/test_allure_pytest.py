import allure

'''
Шаги можно использовать с контекстным менеджером with allure.step()
А можно с декторатором @allure.step
У метода с контекстным менеджером нет ограничений по количеству шагов внутри одной функции. 
С декоратором @allure.step, один шаг = одна функция, что ограничивает его гибкость. 
Однако это не делает декоратор бесполезным. Он очень полезен для создания агрегированных или вложенных шагов
'''


def open_browser():
    ...


@allure.step("Creating course with title '{title}'")
def create_course(title: str):
    ...


@allure.step("Closing browser")
def close_browser():
    ...


def test_feature():
    with allure.step("Opening browser"):
        open_browser()
        ...
    create_course()
    close_browser()
