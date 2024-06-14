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

class TestFirst():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_first(self):
    self.driver.get("https://chat.openai.com/")
    self.driver.set_window_size(1124, 816)
    self.driver.find_element(By.CSS_SELECTOR, "#radix-\\3Ara\\3A > .text-token-text-tertiary").click()
    self.driver.find_element(By.CSS_SELECTOR, "#radix-\\3Ara\\3A > .text-token-text-tertiary").click()
    self.driver.find_element(By.CSS_SELECTOR, ".flex:nth-child(1) > span:nth-child(1) .truncate:nth-child(1)").click()
  
