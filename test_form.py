import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_fill_form_valid(driver):
    driver.get("https://demoqa.com/automation-practice-form")

    driver.execute_script("window.scrollBy(0, 1000);")

    driver.find_element(By.ID, "firstName").send_keys("John")
    driver.find_element(By.ID, "lastName").send_keys("Doe")
    driver.find_element(By.ID, "userEmail").send_keys("john@example.com")
    driver.find_element(By.XPATH, "//label[text()='Male']").click()
    driver.find_element(By.ID, "userNumber").send_keys("9876543210")

    driver.execute_script("window.scrollBy(0, 600);")
    driver.find_element(By.ID, "submit").click()

    time.sleep(2)
    assert driver.find_element(By.ID, "example-modal-sizes-title-lg").is_displayed()
    print("✅ Form submitted successfully")
