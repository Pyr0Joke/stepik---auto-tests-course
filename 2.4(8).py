import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Firefox(executable_path='D:/PythonProjects/geckodriver.exe')
    browser.get(link)
    WebDriverWait(browser, 15).until(expected_conditions.text_to_be_present_in_element((By.ID, "price", ), "$100"))
    browser.find_element_by_id("book").click()
    result = calc(browser.find_element_by_id("input_value").text)
    browser.find_element_by_xpath("//input[@id='answer']").send_keys(result)
    browser.find_element_by_xpath("//button[@type='submit']").click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()