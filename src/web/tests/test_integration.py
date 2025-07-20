import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from custom_logger import logger

# pytest tests --html=reports/report.html --self-contained-html --capture=tee-sys --log-cli-level=INFO

@pytest.fixture
def browser():
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(
        command_executor='http://selenium-hub:4444/wd/hub',
        options=options
    )
    yield driver
    driver.quit()
    
def test_frontend(browser):
    web_port = os.getenv('WEB_PORT', '8501')  # Default to 8501 if not set
    browser.get(f"http://web:{web_port}")
    logger.info("Navigated to the frontend application.")
    time.sleep(1)
    
    current_title = str(browser.title)
    logger.info(f"Current Title: {current_title}")
    assert "Country Getter GUI" in current_title, f"Bad title. Actual title is: {current_title}"


def test_run(browser):
    web_port = os.getenv('WEB_PORT', '8501')  # Default to 8501 if not set
    browser.get(f"http://web:{web_port}")
    logger.info("Navigated to the frontend application.")
    time.sleep(1)

    # Click the submit button
    wait = WebDriverWait(browser, 10)
    submit_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[data-testid='stBaseButton-secondaryFormSubmit']")))
    submit_button.click()

    logger.info("Clicked the submit button.")

    # Verify the data appears on the page
    data_element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".stDataFrame")))
    assert data_element.is_displayed(), "Data table did not appear on the page."

    logger.info("Data displayed successfully.")
