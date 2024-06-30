import requests
from bs4 import BeautifulSoup

def fetch_page(url, headers):
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.text
    else:
        print(f'Error: {response.status_code}')
        return None

def parse_titles(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    titles = soup.find_all('h2', class_='article-title')
    return [title.get_text() for title in titles]

def scrape_titles(url):
    headers = {'User-Agent': 'GoogleChrome'}
    page_content = fetch_page(url, headers=headers)
    if page_content:
        return parse_titles(page_content)
    else:
        return []

infobae_url = 'https://infobae.com'
titles = scrape_titles(infobae_url)
for title in titles:
    print(title)
