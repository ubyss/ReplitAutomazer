from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time

# Emails a serem enviados

emails = [
    "acacio.santos@al.infnet.edu.br",
    "alvaro.ferreira@al.infnet.edu.br",
    "ana.figueiredo@al.infnet.edu.br",
    "andre.becker@al.infnet.edu.br",
    "athos.feitosa@al.infnet.edu.br",
    "augusto.espessoto@al.infnet.edu.br",
    "brenda.larrubia@al.infnet.edu.br",
    "bruce.ujiie@al.infnet.edu.br"
    "calebe.machado@al.infnet.edu.br",
    "carolina.medeiros@al.infnet.edu.br",
    "cassio.nsilva@al.infnet.edu.br",
    "caua.lando@al.infnet.edu.br",
    "danillo.silva@al.infnet.edu.br",
    "eduardo.sferreira@al.infnet.edu.br",
    "elaine.almeida@al.infnet.edu.br",
    "eloy.souza@al.infnet.edu.br",
    "erick.filho@al.infnet.edu.br",
    "ester.lemes@al.infnet.edu.br",
    "everton.rsilva@al.infnet.edu.br",
    "fabiana.severo@al.infnet.edu.br",
    "felipe.carmelo@al.infnet.edu.br",
    "felipe.tolentino@al.infnet.edu.br",
    "felipe.rsilva@al.infnet.edu.br",
    "felipe.coelho@al.infnet.edu.br",
    "filipe.fonceca@al.infnet.edu.br",
    "filipe.figueiroa@al.infnet.edu.br",
    "francisco.nascimento@al.infnet.edu.br",
    "gabriel.lalmeida@al.infnet.edu.br",
    "gabriel.porto@al.infnet.edu.br",
    "gerdson.lima@al.infnet.edu.br",
    "giovanni.leite@al.infnet.edu.br",
    "graham.tidey@al.infnet.edu.br",
    "guilherme.kmarques@al.infnet.edu.br",
    "guilherme.roliveira@al.infnet.edu.br",
    "guilherme.patrao@al.infnet.edu.br",
    "gustavo.souto@al.infnet.edu.br",
    "henzo.policena@al.infnet.edu.br",
    "ian.lima@al.infnet.edu.br",
    "igor.asantos@al.infnet.edu.br",
    "igor.hoffmann@al.infnet.edu.br",
    "igor.monteiro@al.infnet.edu.br",
    "isabella.araujo@al.infnet.edu.br",
    "jackson.silva@al.infnet.edu.br",
    "jean.berg@al.infnet.edu.br",
    "jonathan.campos@al.infnet.edu.br",
    "jose.asantos@al.infnet.edu.br",
    "jose.ecruz@al.infnet.edu.br",
    "jose.menezes@al.infnet.edu.br",
    "jose.barros@al.infnet.edu.br",
    "joao.gsouza@al.infnet.edu.br",
    "joao.klein@al.infnet.edu.br",
    "joao.vcarvalho@al.infnet.edu.br",
    "larissa.mcosta@al.infnet.edu.br",
    "lais.figueredo@al.infnet.edu.br",
    "leandra.nascimento@al.infnet.edu.br",
    "leandro.cgreijal@al.infnet.edu.br",
    "leila.oliveira@al.infnet.edu.br",
    "leonardo.camargo@al.infnet.edu.br",
    "leonardo.plima@al.infnet.edu.br",
    "leandra.nascimento@al.infnet.edu.br",
    "leandro.cgreijal@al.infnet.edu.br",
    "leila.oliveira@al.infnet.edu.br",
    "leonardo.camargo@al.infnet.edu.br",
    "leonardo.plima@al.infnet.edu.br",
    "leonardo.vpereira@al.infnet.edu.br",
    "leonardo.muniz@al.infnet.edu.br",
    "leonardo.ssantos@al.infnet.edu.br",
    "leonidas.junior@al.infnet.edu.br",
    "lucas.frodrigues@al.infnet.edu.br",
    "lucas.loliveira@al.infnet.edu.br",
    "lucas.qaraujo@al.infnet.edu.br",
    "luiz.gneto@al.infnet.edu.br",
    "luiz.pnascimento@al.infnet.edu.br",
    "luiz.pnascimento@al.infnet.edu.br",
    "maiara.silva@al.infnet.edu.br",
    "manoel.neto@al.infnet.edu.br",
    "marcus.boni@al.infnet.edu.br",
    "marcos.serpa@al.infnet.edu.br",
    "marcus.valbuquerque@al.infnet.edu.br",
    "maria.eoliveira@al.infnet.edu.br",
    "mateus.rosa@al.infnet.edu.br",
    "matheus.pinho@al.infnet.edu.br",
    "matheus.palmeida@al.infnet.edu.br",
    "miguel.pecanha@al.infnet.edu.br",
    "nicole.soares@al.infnet.edu.br",
    "paloma.lopes@al.infnet.edu.br",
    "patrick.morais@al.infnet.edu.br",
    "patricia.tabera@al.infnet.edu.br",
    "rachel.ramos@al.infnet.edu.br",
    "rafael.vasconcelos@al.infnet.edu.br",
    "rafael.valves@al.infnet.edu.br",
    "rhuan.dias@al.infnet.edu.br",
    "rian.santos@al.infnet.edu.br",
    "ruy.junior@al.infnet.edu.br",
    "samuel.costa@al.infnet.edu.br",
    "victor.gsilva@al.infnet.edu.br",
    "william.amorim@al.infnet.edu.br",
    "wislan.souza@al.infnet.edu.br",
    "ygor.cardoso@al.infnet.edu.br"
    "leila.oliveira@al.infnet.edu.br",
]

chrome_driver_path = "C:/caminho/para/o/chromedriver.exe"
chrome_service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=chrome_service)
wait = WebDriverWait(driver, 10)

# Abre o Google
driver.get("https://replit.com/team/INF-GRLSOF00C2-N2-L1-23E2-OU")

# Cookies de autenticação

driver.add_cookie({'name': 'connect.sid', 'value': 's%3A3qXBVPICFrTsLDl3z1Fj_TWg4nLPq0Sg.%2FxJc%2BMzsKZ1vlT%2BZ7WQAGAPCMykZVjUsE%2Bt%2FQ%2B10dGk'})
driver.add_cookie({'name': 'replit_authed', 'value': '1'})
driver.add_cookie({'name': 'ajs_user_id', 'value': '20213999'})

driver.get("https://replit.com/team/INF-GRLSOF00C2-N2-L1-23E2-OU")

time.sleep(1)

driver.find_element(By.CSS_SELECTOR, '[data-cy="close-modal"]').click()

time.sleep(1)

driver.find_element(By.XPATH,'/html/body/div[1]/div/main/div[3]/div[1]/div/div[2]/div[2]/div/button').click()

time.sleep(1)

for email in emails:
    # Encontrar o campo de input e inserir o e-mail
    input_email =  driver.find_element(By.CSS_SELECTOR, "input.jsx-3685409278")
    input_email.send_keys(email)

    # Encontrar e clicar no botão
    button = driver.find_element(By.CSS_SELECTOR, 'button.jsx-3216776073')
    button.click()

    # Limpar o campo de input usando JavaScript
    input_email.click()
    input_email.send_keys(Keys.CONTROL + "a")
    input_email.send_keys(Keys.DELETE)
    time.sleep(1)

driver.quit()

