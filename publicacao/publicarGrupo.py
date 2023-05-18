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

grupos = []
    ["Francisco N (Raphael)",
     "Maiara M. (Raphael)",
     "Larissa M. (Raphael)",],

    ["Felipe C.(Thiago)",
     "Igor A. (Thiago)",
     "Breno M. (Thiago)"],

    ["Gabriel P.(Thiago)",
     "Matheus da S.(Thiago)",
     "Jean C. (Thiago)"],

    ["Marcus V.(Thiago)",
     "Everton R. (Thiago)",
     "Laís F. (Thiago)"],

    ["Igor C. (Raphael)",
     "Cauã L. (Raphael)", 
     "Fernando A. (Raphael)"],

    ["Matheus R. (Raphael)",
     "Brenda E. (Raphael)",
     "Ian L. (Raphael)"],

    ["Patrick(Thiago)",
        "Rian P. (Thiago)",
        "Rhuan D.(Thiago)"],

    ["Ester A. (Thiago)",
     "Calebe M.(Thiago)",
     ],

    ["Felipe S (Alexander)",
     "Ruy B (Alexander)",
     "Gabriel A (Alexander)"],

    ["Isabella O. (Thiago)",
     "Cassio N. (Thiago)",
     "Eduardo S. (Thiago)"],

    ["Lucas Q (Alexander)",
     "Kevin O. (Alexander)"],

    ["Augusto E.(Thiago)",
     "Ygor C.(Thiago)",
     "Maria J.(Thiago)"],

    ["Gerdson L. (Raphael)",
     "Rafael V. (Raphael)",
     "José Edson (Raphael)"],

    ["Matheus P (Alexander)",
     "Luiz P (Alexander)",
     "Leandro G (Alexander)"],

    ["Victor G. (Raphael)",
     "Paloma M. (Raphael)",
     "Jose M. (Raphael)"],

    ["Danillo L. (Thiago)",
     "João K.(Thiago)",
     "Guilherme T. (Thiago)"],

    ["Marcos P (Alexander)",
     "Filipe F (Alexander)"],

    ["Patrícia(Thiago)",
     "Lucas L. (Thiago)"],

     ["Leonardo F.(Thiago)",
     "Erick E. (Thiago)"],

    ["Leonidas J.(Thiago)",
     "João V.(Thiago)",
     "Guilherme K.(Thiago)"],

    ["Leonardo S. (Raphael)",
     "Athos F. (Raphael)",
     "Eloy K.(Raphael)"],

    ["Leonardo V. (Raphael)",
     "Rian E. (Raphael)",
     "Jose Ams. (Raphael)"],

    ["Luiz G. (Raphael)",
     "Joao G. (Raphael)"],

    ["Jackson S. (Raphael)",
     "Leandra N. (Raphael)"],

    ["Fillipe R. (Thiago)",
     "Elaine S. (Thiago)",
     "Marcus B.(Thiago)",
     "Elaine S.2(Thiago)"],

    ["Henzo P (Alexander)",
     "Graham L (Alexander)",
     "William S (Alexander)"],

    ["Samuel D (Alexander)",
     "Jose M (Alexander)",
     "Bruce U (Alexander)"],

    ["Leila H (Alexander)",
     "Leonardo M (Alexander)",
     "Manoel E (Alexander)"],

    ["Rafael D (Alexander)",
     "Acacio S (Alexander)",
     "Gustavo C (Alexander)"],

    ["André B.(Alexander)",
     "Giovanni L (Alexander)"],

    ["Lucas F. (Raphael)",
     "Igor F. (Raphael)",
     "Jonathan V. (Raphael)"],

    ["Nicole P (Alexander)",
     "Felipe B (Alexander)"],

    ["Miguel F. (Raphael)",
     "Leonardo P.(Raphael))",
     "Gabriel S.(Raphael)"],
]


def automatization():
    
 # Seleciona a Data
    # new_due_date = driver.find_element(By.CSS_SELECTOR, "input.css-1d775yd")

    # new_due_date.click()
    # new_due_date.send_keys("15")
    # new_due_date.send_keys("05")
    # new_due_date.send_keys("2023")

    # # Hórario

    # new_due_hour = driver.find_elements(By.CSS_SELECTOR, "input.jsx-3685409278")

    # # Hora
    # new_due_hour[2].send_keys("11")

    # # minutos
    # new_due_hour[3].send_keys("59")

    # # De tarde
    # new_due_hour[4].send_keys("P")

    # checkbox = driver.find_element(By.XPATH, "//input[@id='modal4val-toggle']")
    # actions = ActionChains(driver)
    # actions.move_to_element(checkbox).click().perform()

    elements = driver.find_elements(By.CSS_SELECTOR, "input.jsx-3685409278")

    group_size_input = elements[-1]
    group_size_input.send_keys(Keys.DOWN)

    for grupo in grupos:
        driver.find_element(
            By.CSS_SELECTOR, "button.default.jsx-3580467505:last-child").click()

        input_elements = driver.find_elements(
            By.CSS_SELECTOR, "input.jsx-3685409278")
        input_element = input_elements[-1]

        for nome in grupo:
            input_element.send_keys(nome)
            input_element.send_keys(Keys.ENTER)


def main():
    automatization()

# Inicialization


main()
