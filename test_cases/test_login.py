import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from typing import Any

@pytest.mark.usefixtures("setup_driver")
class TestLogin:
    driver:webdriver.Chrome

    def test_01(self):
        self.driver.get("https://www.saucedemo.com/") #rgrg
