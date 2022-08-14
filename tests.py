import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



def get_driver(url):
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    chrom_driver_path = "D:\pythonProject\chromedriver.exe"
    driver = webdriver.Chrome(chrom_driver_path, chrome_options=chrome_options)
    driver.maximize_window()
    driver.get(url)
    return driver


def test_drag_drop():
    driver = get_driver('https://demo.guru99.com/test/drag_drop.html')
    actions = ActionChains(driver)
    actions.drag_and_drop(driver.find_element(By.CLASS_NAME, "block13"),
                          driver.find_element(By.CLASS_NAME, "field13")).perform()
    actions.drag_and_drop(driver.find_element(By.CLASS_NAME, "block13"),
                          driver.find_element(By.ID, "amt8")).perform()
    actions.drag_and_drop(driver.find_element(By.ID, "credit2"),
                          driver.find_element(By.CLASS_NAME, "ui-droppable")).perform()
    actions.drag_and_drop(driver.find_element(By.ID, "credit1"),
                          driver.find_element(By.ID, "loan")).perform()
    driver.quit()



