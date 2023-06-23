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

class TestClick():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_click(self):
    self.driver.get("https://www.wildberries.ru/")
    self.driver.find_element(By.CSS_SELECTOR, ".nav-element__burger-line").click()
    element = self.driver.find_element(By.LINK_TEXT, "Женщинам")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.LINK_TEXT, "Женщинам").click()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.LINK_TEXT, "Верхняя одежда").click()
    self.driver.find_element(By.ID, "searchInput").click()
    self.driver.find_element(By.ID, "searchInput").send_keys("куртка")
    self.driver.find_element(By.ID, "searchInput").send_keys(Keys.DOWN)
    self.driver.find_element(By.ID, "searchInput").send_keys(Keys.DOWN)
    self.driver.find_element(By.ID, "searchInput").send_keys("куртка женская весна")
    self.driver.find_element(By.ID, "applySearchBtn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-filter__btn--burger").click()
    self.driver.find_element(By.LINK_TEXT, "Одежда").click()
    self.driver.find_element(By.CSS_SELECTOR, ".dropdown-filter__btn--sorter").click()
    self.driver.find_element(By.CSS_SELECTOR, ".filter__item:nth-child(3) .radio-with-text__text").click()
    self.driver.find_element(By.CSS_SELECTOR, "#Zjc1Y2MyMTMtYTUwZS0yZjEyLTJkNTktYWMxM2IzZWMxMTY1 > .dropdown-filter__btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".filter__item:nth-child(1) .checkbox-with-text__text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".selected > .checkbox-with-text__text").click()
    self.driver.find_element(By.CSS_SELECTOR, ".filter__item:nth-child(7) .checkbox-with-text__text").click()
    self.driver.find_element(By.CSS_SELECTOR, "#c44655401 .product-card__link").click()
    element = self.driver.find_element(By.LINK_TEXT, "Все куртки сноубордические FORCELAB")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".active:nth-child(3)").click()
    self.driver.find_element(By.CSS_SELECTOR, "div:nth-child(2) > .order > .btn-main:nth-child(2)").click()
    self.driver.find_element(By.LINK_TEXT, "Перейти в корзину").click()
    element = self.driver.find_element(By.LINK_TEXT, "правилами пользования торговой площадкой")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    element = self.driver.find_element(By.CSS_SELECTOR, "body")
    actions = ActionChains(self.driver)
    actions.move_to_element(element, 0, 0).perform()
    self.driver.find_element(By.NAME, "ConfirmOrderByRegisteredUser").click()
  