from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver import ChromeOptions
def pytest_addoption(parser):
    parser.addoption(
        "--browser_name" , action="store" , default="Chrome" , help="run tests slowly"   
    )
@pytest.fixture(scope="function")
def browserinstance(request):
    browsername=request.config.getoption("browser_name")
    if browsername=="Chrome":
        opt=webdriver.ChromeOptions()
        opt.add_argument("--incognito")
        driver=webdriver.Chrome(options=opt)
    elif browsername=="Firefox":
        driver=webdriver.Firefox
    driver.get("https://automationexercise.com/")
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()
    
import os

# Hook to take screenshot on failure or expected failure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    pytest_html = item.config.pluginmanager.getplugin("html")
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when in ("call", "setup"):
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            reports_dir = os.path.join(os.path.dirname(__file__), "reports", "screenshots")
            os.makedirs(reports_dir, exist_ok=True)

            file_name = os.path.join(
                reports_dir,
                report.nodeid.replace("::", "_").replace("/", "_") + ".png"
            )

            print("Screenshot saved to:", file_name)

            _capture_screenshot(item, file_name)

            if os.path.isfile(file_name):
                html = (
                    f'<div><img src="{file_name}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                extra.append(pytest_html.extras.html(html))
        report.extra = extra


# Helper function to capture screenshot
def _capture_screenshot(item, file_name):
    driver = item.funcargs.get("browserinstance")
    if driver:
        driver.save_screenshot(file_name)
