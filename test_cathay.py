import logging
import os

import pytest
from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

logging.basicConfig(level=logging.INFO)
chrome_driver_path = "C:\\Users\\YIHSUAN\\Downloads\\chromedriver_win_84\\chromedriver.exe"
avd_uid = "emulator-5554"


class TestCathay:
    @pytest.fixture(scope="function", autouse=True)
    def driver(self):
        capabilities = dict(
            platformName='Android',
            automationName='uiautomator2',
            deviceName='Android',
            chromedriverExecutable=chrome_driver_path,
            browserName="Chrome",
            udid=avd_uid,
            showChromedriverLog=True,
            chromeOptions={'w3c': False}
        )
        appium_server_url = 'http://localhost:4723'
        self.driver = webdriver.Remote(appium_server_url, options=UiAutomator2Options().load_capabilities(capabilities))

    def test_enter_page_and_screenshot(self):
        self.driver.get("https://www.cathaybk.com.tw/cathaybk/")
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "searchBox")))
        self.driver.get_screenshot_as_file("index_page.png")
        # Go to credit card menu.
        menu_elem = self.driver.find_element(By.XPATH, "//header/div/div[1]")
        menu_elem.click()
        product_intro_elem = self.driver.find_element(By.XPATH,
                                                      "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[1]/div")
        product_intro_elem.click()
        credit_card_elem = self.driver.find_element(By.XPATH,
                                                    "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[1]/div")
        credit_card_elem.click()
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.XPATH, "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a")))
        credit_card_sub_elems = self.driver.find_elements(By.XPATH,
                                                          "/html/body/div[1]/header/div/div[3]/div/div[2]/div[1]/div/div[1]/div[2]/div/div[1]/div[2]/a")
        logging.info(f"There are {len(credit_card_sub_elems)} items under credit card menu.")
        self.driver.get_screenshot_as_file("credit_card_sub_item_01.png")
        self.driver.scroll(credit_card_sub_elems[0], credit_card_sub_elems[-1])
        self.driver.get_screenshot_as_file("credit_card_sub_item_02.png")
        self.driver.scroll(credit_card_sub_elems[-1], credit_card_sub_elems[0])
        credit_card_sub_elems[0].click()
        # Go to stop card section.
        card_title_elem = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, "/html/body/div[1]/main/div/div[2]/div[1]/p")))
        stop_card_block_elem = self.driver.find_element(By.XPATH,
                                                        "/html/body/div[1]/main/article/section[6]/div")
        self.driver.scroll(card_title_elem, stop_card_block_elem)
        # Create folder to save stop card screenshot.
        stop_card_folder = "stop_card"
        if not os.path.exists(stop_card_folder):
            os.makedirs(stop_card_folder)
        all_stop_card_elems = self.driver.find_elements(By.XPATH,
                                                        "/html/body/div[1]/main/article/section[6]/div/div[2]/div/div[1]/div")
        logging.info(f"There are {len(all_stop_card_elems)} stop cards.")
        for i in range(len(all_stop_card_elems)):
            WebDriverWait(all_stop_card_elems[i], 10).until(EC.visibility_of_element_located((By.TAG_NAME, 'img')))
            self.driver.get_screenshot_as_file(f"{stop_card_folder}/stop_card_{str(i + 1).zfill(2)}.png")
            if i + 1 < len(all_stop_card_elems):
                self.driver.scroll(all_stop_card_elems[i], all_stop_card_elems[i + 1])
        screenshot_files = os.listdir(stop_card_folder)
        assert len(screenshot_files) == len(all_stop_card_elems), \
            f"There should be {len(all_stop_card_elems)} screenshot files in folder({stop_card_folder})."
