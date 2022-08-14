import logging
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


def test_iframe():
    driver = get_driver("http://automationpractice.com/index.php")
    product = driver.find_element(By.CLASS_NAME, "product-container")
    product.find_element(By.CLASS_NAME, "icon-eye-open").click()
    time.sleep(3)
    iframe = driver.find_element(By.CLASS_NAME, "fancybox-iframe")
    driver.switch_to.frame(iframe)
    driver.find_element(By.CSS_SELECTOR, ".box-cart-bottom button").click()
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="layer_cart"]/div[1]/div[2]/div[4]/a').click()
    proceed = driver.find_element(By.ID, "center_column") \
        .find_element(By.CLASS_NAME, "cart_navigation").find_element(By.CLASS_NAME, "button")
    actions = ActionChains(driver)
    actions.move_to_element(proceed).click().perform()
    proceed = driver.find_element(By.CLASS_NAME, "cart_navigation").find_element(By.TAG_NAME, "button")
    actions = ActionChains(driver)
    actions.move_to_element(proceed).click().perform()
    checkbox = driver.find_element(By.XPATH, '//*[@id="cgv"]')
    actions = ActionChains(driver)
    actions.move_to_element(checkbox).click().perform()
    proceed = driver.find_element(By.NAME, "processCarrier")
    actions = ActionChains(driver)
    actions.move_to_element(proceed).click().perform()
    proceed = driver.find_element(By.CLASS_NAME, "bankwire")
    actions = ActionChains(driver)
    actions.move_to_element(proceed).click().perform()
    proceed = driver.find_element(By.ID, "center_column").find_element(By.TAG_NAME, "button")
    actions = ActionChains(driver)
    actions.move_to_element(proceed).click().perform()
    assert driver.find_element(By.CLASS_NAME, "cheque-indent").text == "Your order on My Store is complete."
    logging.info("bought the product successfully!")
    driver.quit()

