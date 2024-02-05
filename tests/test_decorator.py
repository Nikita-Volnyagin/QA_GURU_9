import allure
from allure_commons.types import Severity
from selene import browser, by, be
from selene.support.shared.jquery_style import s


@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "Nikita-Volnyagin")
@allure.feature("Issues")
@allure.story("Поиск в Issues")
def test_with_labels(open_browser):
    open_page()
    search_repo()
    go_to_repo()
    open_issue()
    find_issue()


@allure.step("Открываем главную страницу")
def open_page():
    browser.open("https://github.com")


@allure.step("Ищем репозиторий")
def search_repo():
    s(".header-search-button").click()
    s("#query-builder-test").type("Nikita-Volnyagin/QA_GURU_9")
    s("#query-builder-test").submit()


@allure.step("Переходим по ссылке в репо")
def go_to_repo():
    s(by.link_text("Nikita-Volnyagin/QA_GURU_9")).click()


@allure.step("Открываем Issues")
def open_issue():
    s("#issues-tab").click()


@allure.step("Находим Issue")
def find_issue():
    s(by.partial_text("#1")).should(be.visible)