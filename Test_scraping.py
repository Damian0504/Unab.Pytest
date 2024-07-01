import pytest
import requests
from bs4 import BeautifulSoup
from Scraping import fetch_page, parse_titles, scrape_titles  

def test_fetch_page_success(requests_mock):
    url = 'https://infobae.com'
    headers = {'User-Agent': 'GoogleChrome'}
    mock_html = '<html><body><h2 class="article-title">Test Title</h2></body></html>'
    requests_mock.get(url, text=mock_html)

    result = fetch_page(url, headers)
    assert result == mock_html

def test_fetch_page_error(requests_mock):
    url = 'https://infobae.com'
    headers = {'User-Agent': 'GoogleChrome'}
    requests_mock.get(url, status_code=404)

    with pytest.raises(Exception, match="Error: 404"):
        fetch_page(url, headers)

def test_parse_titles():
    html_content = '<html><body><h2 class="article-title">Test Title 1</h2><h2 class="article-title">Test Title 2</h2></body></html>'
    expected_titles = ['Test Title 1', 'Test Title 2']

    titles = parse_titles(html_content)
    assert titles == expected_titles

def test_scrape_titles(requests_mock):
    url = 'https://infobae.com'
    headers = {'User-Agent': 'GoogleChrome'}
    mock_html = '<html><body><h2 class="article-title">Test Title</h2></body></html>'
    requests_mock.get(url, text=mock_html)

    expected_titles = ['Test Title']
    titles = scrape_titles(url)
    assert titles == expected_titles
