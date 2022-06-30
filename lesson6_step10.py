from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"    
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.CSS_SELECTOR, "input.form-control.first:required")
    input1.send_keys("Anna")
    input2 = browser.find_element(By.CSS_SELECTOR, "input.form-control.second:required")
    input2.send_keys("Venev")
    input3 = browser.find_element(By.CSS_SELECTOR, "input.form-control.third:required")
    input3.send_keys("test@test.com")
    input4 = browser.find_element(By.CSS_SELECTOR, ".second_block input.form-control.first")
    input4.send_keys("000000000")
    input5 = browser.find_element(By.CSS_SELECTOR, ".second_block input.form-control.second")
    input5.send_keys("Los Angeles, Hollywood")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()