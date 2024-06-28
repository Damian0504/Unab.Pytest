import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Realiza la solicitud HTTP con requests
url = 'https://infobae.com'
response = requests.get(url)

if response.status_code == 200:
    page_content = response.text
else:
    print(f'Error: {response.status_code}')

# Parsea el contenido con BeautifulSoup
soup = BeautifulSoup(page_content, 'html.parser')
titles = soup.find_all('h2', class_='article-title')

for title in titles:
    print(title.get_text())

# Configura Selenium para ejecutar en modo headless
options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# Abre la página con Selenium
driver.get(url)

# Espera a que el contenido cargue completamente
driver.implicitly_wait(10)  # Espera 10 segundos

# Encuentra los elementos necesarios
titles = driver.find_elements(By.CLASS_NAME, 'article-title')

for title in titles:
    print(title.text)

driver.quit()
