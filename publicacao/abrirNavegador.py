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
import subprocess

chrome_path = "chrome.exe"
remote_debugging_port = "9014"
user_data_dir = r"C:\Data\google-data"

chrome_command = f"{chrome_path} --remote-debugging-port={remote_debugging_port} --user-data-dir={user_data_dir}"

subprocess.Popen(chrome_command)

chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "localhost:9014")
service = Service(executable_path=ChromeDriverManager().install())

driver = webdriver.Chrome(options=chrome_options, service=service)

driver.get("https://replit.com/team/INFNET-GRLSOF00C2-N2-L1-23E2")
