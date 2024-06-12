import pytest
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from typing import Any


class LoginPage:
    driver: webdriver.Chrome

    textbox_username_id = "user-name"
    textbox_password_id = "password"
    btn_login_id = "login-button"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.ID, self.btn_login_id).click()
