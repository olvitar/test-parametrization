import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


# передача параметров командной строки
def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en-gb", help="Choose language")


# фикстура browser, которая создает нам экземпляр браузера для тестов с выбором браузера и языка пользователя
@pytest.fixture(scope="class")
def browser(request):
    browser_name = request.config.getoption("browser_name")  # тянем браузер из параметра CLI
    user_language = request.config.getoption("language")  # тянем язык браузера из параметра CLI
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)

    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)

    else:
        print("Browser {} still is not implemented".format(browser_name))
        raise Exception

    yield browser
    print("\nquit browser..")
    browser.quit()


"""
#фикстура browser, которая создает нам экземпляр браузера для тестов (базовая)
@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
"""
