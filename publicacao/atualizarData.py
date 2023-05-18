from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9014")
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chrome_options, service=service)
wait = WebDriverWait(driver, 10)

def automatization():

    # Remove a data seleciona

    # delete_button = driver.find_element(By.CSS_SELECTOR, 'button.css-xb4ftf')

    # Seleciona a Data
    new_due_date = driver.find_element(By.CSS_SELECTOR, "input.css-1d775yd")

    new_due_date.click()
    new_due_date.send_keys("29")
    new_due_date.send_keys("05")
    new_due_date.send_keys("2023")

    # Hórario

    new_due_hour = driver.find_elements(By.CSS_SELECTOR, "input.jsx-3685409278")

    # Hora
    new_due_hour[2].send_keys("11")

    # minutos
    new_due_hour[3].send_keys("59")

    # De tarde
    new_due_hour[4].send_keys("P")


def main():
    automatization()

main()



