from datetime import datetime

import pytest
import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# === Global variables ===
driver = None
report_dir = None
screenshots_dir = None

@pytest.fixture(scope="class")
def browserInstance(request):
    global driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("prefs", {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False
    })
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-blink-features=AutomationControlled")
    chrome_options.add_argument("--incognito")

    # Set up Chrome WebDriver
    driver_path = "/Users/deeps-devops/Documents/Python_Projects/chromedriver-mac-arm64/chromedriver"
    service_obj = Service(driver_path)
    driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    driver.implicitly_wait(10)


    request.cls.driver = driver

    yield driver
    driver.quit()


# Create timestamped report dir
def pytest_configure(config):
    global report_dir, screenshots_dir

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    report_dir = os.path.join(os.getcwd(), "Reports", f"report_{timestamp}")
    screenshots_dir = os.path.join(report_dir, "screenshots")
    os.makedirs(screenshots_dir, exist_ok=True)

    config.option.htmlpath = os.path.join(report_dir, "report.html")
    config.option.self_contained_html = True



# === Pytest configure to generate timestamped report dir ===
@pytest.hookimpl( hookwrapper=True )
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
        """
    global screenshots_dir
    outcome = yield
    report = outcome.get_result()

    if report.when in ("call", "setup") and report.failed:
        driver = item.funcargs.get("browserInstance", None)
        if driver:
            screenshot_file = os.path.join(screenshots_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_file)

            if os.path.exists(screenshot_file):
                extra = getattr(report, "extra", [])
                html = (
                    f'<div><img src="{screenshot_file}" alt="screenshot" '
                    f'style="width:304px;height:228px;" '
                    f'onclick="window.open(this.src)" align="right"/></div>'
                )
                report.extra = extra + [item.config.pluginmanager.getplugin("html").extras.html(html)]


def pytest_html_report_title(report):
    report.title = "Automation Test Report - ProtoCommerce"