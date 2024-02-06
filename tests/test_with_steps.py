import allure
from selene import browser, by, be
from selene.support.shared.jquery_style import s

def test_with_allure_steps():
    with allure.step("Открываем главную страницу"):
        browser.open("https://github.com")

    with allure.step("Ищем репозиторий"):
        s(".header-search-button").click()
        s("#query-builder-test").type("Nikita-Volnyagin/QA_GURU_9")
        s("#query-builder-test").submit()

    with allure.step("Переходим по ссылке репо"):
        s(by.link_text("Nikita-Volnyagin/QA_GURU_9")).click()

    with allure.step("Открываем Issues"):
        s("#issues-tab").click()

    with allure.step("Проверяем наличие Issue #1"):
        s(by.partial_text("#1")).should(be.visible)