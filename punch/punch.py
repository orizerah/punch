from selenium import webdriver
from selenium.webdriver.chromium.webdriver import ChromiumDriver
from selenium.webdriver.common.by import By

TIMEWATCH_LOGIN = 'https://checkin.timewatch.co.il/punch/punch.php'


def get_driver() -> ChromiumDriver:
    driver = webdriver.ChromiumEdge()
    return driver


def go_to_timewatch_website(driver: ChromiumDriver):
    driver.get(TIMEWATCH_LOGIN)


def login(driver: ChromiumDriver, company_id: str, employee_id: str, employee_pass: str):
    company_id_element = driver.find_element(value='compKeyboard')
    company_id_element.send_keys(company_id)

    employee_id_element = driver.find_element(value='nameKeyboard')
    employee_id_element.send_keys(employee_id)

    employee_pass_element = driver.find_element(value='pwKeyboard')
    employee_pass_element.send_keys(employee_pass)

    submit_button = driver.find_element(By.NAME, 'B1')
    submit_button.click()


def punch(driver: ChromiumDriver):
    punch_button = driver.find_element(By.CLASS_NAME, 'entry-btn')
    punch_button.click()

    try:
        confirm_button = driver.find_element(By.NAME, 'jqi_state0_button')
        confirm_button.click()
    except Exception:
        pass
