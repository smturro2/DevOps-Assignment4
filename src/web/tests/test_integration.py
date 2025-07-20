import pytest
from selenium import webdriver
import os

# pytest tests --driver Remote --selenium-host selenium-standalone --capability browserName chrome --html=reports/report.html --self-contained-html
# pytest tests --driver Remote --capability browserName chrome --html=reports/report.html --self-contained-html

# @pytest.fixture
# def browser():
#     driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

# def test_frontend(browser):
#     browser.get(f"web:{os.getenv('WEB_PORT')}")
#     assert "Country Getter GUI" in browser.title

def test_true():
    assert True