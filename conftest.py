import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

valid_email = '888grey.rus@mail.ru'
valid_password = '123121pf'


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome('/WebDriver/chromedriver.exe')
    pytest.driver.get('https://petfriends.skillfactory.ru/login')
    yield
    pytest.driver.quit()


@pytest.fixture()
def show_my_pets():
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "email")))
    # Вводим валидный email
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, "pass")))
    # Вводим валидный пароль
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    element = WebDriverWait(pytest.driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "button[type='submit']")))
    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    element = WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.LINK_TEXT, "Мои питомцы")))
    # Нажимаем на ссылку "Мои питомцы"
    pytest.driver.find_element(By.LINK_TEXT, "Мои питомцы").click()
