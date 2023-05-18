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

nomes = []
    "Thiago(TESTE)",
    "Francisco N (Raphael)",
    "Maiara M. (Raphael)",
    "Felipe C.(Thiago)",
    "Gabriel P.(Thiago)",
    "Marcus V.(Thiago)",
    "Igor C. (Raphael)",
    "Matheus R. (Raphael)",
    "Patrick(Thiago)",
    "Matheus da S.(Thiago)",
    "Ester A. (Thiago)",
    "Felipe S (Alexander)",
    "Isabella O. (Thiago)",
    "Lucas Q (Alexander)",
    "Augusto E.(Thiago)",
    "Ruy B (Alexander)",
    "Gerdson L. (Raphael)",
    "Matheus P (Alexander)",
    "Rafael V. (Raphael)",
    "Gabriel A (Alexander)",
    "Everton R. (Thiago)",
    "Luiz P (Alexander)",
    "Victor G. (Raphael)",
    "Danillo L. (Thiago)",
    "Marcos P (Alexander)",
    "Patrícia(Thiago)",
    "Leonardo F.(Thiago)",
    "Leonidas J.(Thiago)",
    "Jean C. (Thiago)",
    "Cauã L. (Raphael)",
    "Leonardo S. (Raphael)",
    "Brenda E. (Raphael)",
    "João V.(Thiago)",
    "Leonardo V. (Raphael)",
    "Paloma M. (Raphael)",
    "Luiz G. (Raphael)",
    "Jackson S. (Raphael)",
    "Fillipe R. (Thiago)",
    "Henzo P (Alexander)",
    "Ygor C.(Thiago)",
    "Jose M. (Raphael)",
    "Elaine S. (Thiago)",
    "Joao G. (Raphael)",
    "Samuel D (Alexander)",
    "Calebe M. (Thiago)",
    "Leila H (Alexander)",
    "Cassio N. (Thiago)",
    "Rafael D (Alexander)",
    "André B.(Alexander)",
    "Eduardo S. (Thiago)",
    "Ian L. (Raphael)",
    "Lucas F. (Raphael)",
    "Alvaro F (Raphael)",
    "Rian P. (Thiago)",
    "Graham L (Alexander)",
    "Jose M (Alexander)",
    "Leonardo M (Alexander)",
    "Kevin O. (Alexander)",
    "Nicole P (Alexander)",
    "Igor F. (Raphael)",
    "João K.(Thiago)",
    "José Edson (Raphael)",
    "Acacio S (Alexander)",
    "Rian E. (Raphael)",
    "Gustavo C (Alexander)",
    "Larissa M. (Raphael)",
    "Miguel F. (Raphael)",
    "Leandra N. (Raphael)",
    "Manoel E (Alexander)",
    "Lucas L. (Thiago)",
    "Athos F. (Raphael)",
    "William S (Alexander)",
    "Bruce U (Alexander)",
    "Marcus B.(Thiago)",
    "Giovanni L (Alexander)",
    "Felipe B (Alexander)",
    "Guilherme T. (Thiago)",
    "Laís F. (Thiago)",
    "Maria J.(Thiago)",
    "Igor A. (Thiago)",
    "Rhuan D.(Thiago)",
    "Filipe F (Alexander)",
    "Leandro G (Alexander)",
    "Carlos A. (Raphael)",
    "Jonathan V. (Raphael)",
    "Erick E. (Thiago)",
    "Guilherme K.(Thiago)",
    "Jose Ams. (Raphael)",
    "Breno M. (Thiago)",
    "Eloy K.(Raphael)",
    "Leonardo P. (Raphael))",
    "Gabriel S.(Raphael)",
    "Elaine S.2(Thiago)",
    "Kevinhoneygain",
    "Fernando A. (Raphael)"
]

primeiro_grupo = nomes[:48]

# Segundo grupo: nomes de 30 a 59
segundo_grupo = nomes[48:72]

# Terceiro grupo: nomes de 60 até o final

def automatization():

    elements = driver.find_elements(By.CSS_SELECTOR, "input.jsx-3685409278")

    group_size_input = elements[-1]
    group_size_input.send_keys(Keys.DOWN)
    group_size_input.send_keys(Keys.DOWN)
    group_size_input.send_keys(Keys.DOWN)

for nome in primeiro_grupo:
    driver.find_element(By.CSS_SELECTOR, "button.default.jsx-3580467505:last-child").click()
    input_elements = driver.find_elements(By.CSS_SELECTOR, "input.jsx-3685409278")
    input_element = input_elements[-1]

    input_element.send_keys(nome)
    input_element.send_keys(Keys.ENTER)


def main():
    automatization()

# Inicialization


main()
