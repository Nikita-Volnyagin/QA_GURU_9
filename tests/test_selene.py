from selene import browser, by, be
from selene.support.shared.jquery_style import s


def test_classic_selene():
    browser.open("https://github.com")

    s(".header-search-button").click()
    s("#query-builder-test").type("Nikita-Volnyagin/QA_GURU_9")
    s("#query-builder-test").submit()

    s(by.link_text("Nikita-Volnyagin/QA_GURU_9")).click()

    s("#issues-tab").click()

    s(by.partial_text("#1")).should(be.visible)