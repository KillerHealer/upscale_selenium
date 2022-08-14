import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture()
def get_driver(url):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrom_driver_path = "D:\pythonProject\chromedriver.exe"
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    return driver


def test_drag_drop(get_driver):
    get_driver.get('https://demo.guru99.com/test/drag_drop.html')
    actions = ActionChains(get_driver)
    actions.drag_and_drop(get_driver.find_element(By.CLASS_NAME, "block13"),
                          get_driver.find_element(By.CLASS_NAME, "field13")).perform()
    actions.drag_and_drop(get_driver.find_element(By.CLASS_NAME, "block13"),
                          get_driver.find_element(By.ID, "amt8")).perform()
    actions.drag_and_drop(get_driver.find_element(By.ID, "credit2"),
                          get_driver.find_element(By.CLASS_NAME, "ui-droppable")).perform()
    actions.drag_and_drop(get_driver.find_element(By.ID, "credit1"),
                          get_driver.find_element(By.ID, "loan")).perform()
    get_driver.quit()



