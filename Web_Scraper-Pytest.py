import requests

url = 'https://infobae.com'
response = requests.get(url)

# Verifica si la solicitud fue exitosa
if response.status_code == 200:
    page_content = response.text
else:
    print(f'Error: {response.status_code}')

from bs4 import Beautifulsoup

soup = BeautifulSoup(page_content, 'html.parser')

# Encuentra los datos que necesitas, por ejemplo, todos los títulos de artículos
titles = soup.find_all('h2', class_='article-title')

for title in titles:
    print(title.get_text())

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

options = Options()
options.headless = True  # Ejecuta el navegador en modo headless (sin interfaz gráfica)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

url = 'https://infobae.com'
driver.get(url)

# Espera a que el contenido cargue y luego encuentra los elementos necesarios
titles = driver.find_elements(By.CLASS_NAME, 'article-title')

for title in titles:
    print(title.text)

driver.quit()

headers = {'User-Agent': 'Microsoft Edge'}
response = requests.get(url, headers=headers)
