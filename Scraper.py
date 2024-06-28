import requests
from bs4 import BeautifulSoup

def fetch_page(url, headers=None):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        raise Exception(f'Error: {response.status_code}')

def parse_titles(page_content):
    soup = BeautifulSoup(page_content, 'html.parser')
    titles = soup.find_all('h2', class_='article-title')
    return [title.get_text() for title in titles]

def scrape_titles(url):
    headers = {'User-Agent': 'GoogleChrome'}
    page_content = fetch_page(url, headers=headers)
    return parse_titles(page_content)

infobae_url = 'https://infobae.com'
titles = scrape_titles(infobae_url)
for title in titles:
    print(title)
