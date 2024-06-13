import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from typing import Any
from base_pages.LoginPage import LoginPage
from utilities.custom_logger import Log_Maker


@pytest.mark.usefixtures("setup_driver")
class TestLogin:
    driver: webdriver.Chrome
    logger = Log_Maker.log_gen()

    def test_verify_title(self):
        self.logger.info("**********test_verify_title Started**********")
        actual_title = self.driver.title
        exp_title = "Swag Labs"
        if actual_title == exp_title:
            self.logger.info("**********test_verify_title Passed**********")
            assert True
        else:
            self.logger.info("**********test_verify_title Failed**********")
            assert False

    @pytest.mark.parametrize("username,password",
                             [("standard_user", "secret_sauce"),
                              ("locked_out_user", "secret_sauce"),
                              ("problem_user", "secret_sauce"),
                              ("performance_glitch_user", "secret_sauce")])
    def test_valid_login(self, username, password):
        self.logger.info("**********test_valid_admin_login Started**********")
        self.tvl = LoginPage(self.driver)
        self.tvl.enter_username(username)
        time.sleep(2)
        self.tvl.enter_password(password)
        time.sleep(2)
        self.tvl.click_login()
        time.sleep(2)
