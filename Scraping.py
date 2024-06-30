import requests
from bs4 import BeautifulSoup

def fetch_page(url, headers=None, requests_module=requests):
    response = requests_module.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f'Error: {response.status_code}')

def parse_titles(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    titles = soup.find_all('h2', class_='article-title')
    return [title.get_text() for title in titles]

def scrape_titles(url, requests_module=requests):
    headers = {'User-Agent': 'GoogleChrome'}
    page_content = fetch_page(url, headers=headers, requests_module=requests_module)
    return parse_titles(page_content)
