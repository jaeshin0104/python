# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("https://chicor.com/main")
    self.driver.set_window_size(1294, 1040)
    element = self.driver.find_element(By.LINK_TEXT, "자세히 보기")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "로그인").click()
    self.driver.find_element(By.ID, "lginId").click()
    self.driver.find_element(By.ID, "lginId").send_keys("820104")
    self.driver.find_element(By.ID, "lginPw").send_keys("2359145js>")
    self.driver.find_element(By.CSS_SELECTOR, ".btn-login > .btn").click()
    self.driver.close()
  
