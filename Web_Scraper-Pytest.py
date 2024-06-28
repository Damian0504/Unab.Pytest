import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

url = 'https://infobae.com'
response = requests.get(url)

if response.status_code == 200:
    page_content = response.text
else:
    print(f'Error: {response.status_code}')

soup = BeautifulSoup(page_content, 'html.parser')
titles = soup.find_all('h2', class_='article-title')

for title in titles:
    print(title.get_text())

options = Options()
options.headless = True
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

driver.get(url)

driver.implicitly_wait(10)  # Espera 10 segundos

titles = driver.find_elements(By.CLASS_NAME, 'article-title')

for title in titles:
    print(title.text)

driver.quit()
