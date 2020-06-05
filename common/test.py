import pytest
from selenium import webdriver
from common.helpers import CHROME_DRIVER_PATH

driver = webdriver.Chrome('/Users/paul/chromedriver')
driver.get("https://www.cian.ru/")
assert "ЦИАН" in driver.title