import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestCathay:
    @pytest.fixture(scope="function", autouse=True)
    def driver(self):
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Android',
            appActivity='.Settings',
            language='en',
            locale='US',
            chromedriverExecutable="C:\\Users\\YIHSUAN\\Downloads\\chromedriver_win_84\\chromedriver.exe",
            browserName="Chrome",
            udid="emulator-5554",
            showChromedriverLog=True,
            chromeOptions={'w3c': False}
        )
        appium_server_url = 'http://localhost:4723'
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def test_enter_page_and_screenshot(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "searchBox")))
        self.driver.get_screenshot_as_file("index_page.png")
        menu_elem = self.driver.find_element(By.XPATH, "//header/div/div[1]")
        menu_elem.click()
