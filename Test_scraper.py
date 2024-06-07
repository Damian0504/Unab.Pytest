import pytest
from scraper import fetch_page, parse_titles

def test_fetch_page(monkeypatch):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    def mock_get(*args, **kwargs):
        return MockResponse('<html><h2 class="article-title">Test Title</h2></html>', 200)

    monkeypatch.setattr('requests.get', mock_get)

    url = 'https://example.com'
    headers = {'User-Agent': 'Mozilla/5.0'}
    page_content = fetch_page(url, headers=headers)
    assert 'Test Title' in page_content

def test_parse_titles():
    html_content = '<html><h2 class="article-title">Test Title</h2></html>'
    titles = parse_titles(html_content)
    assert titles == ['Test Title']

def test_scrape_titles(monkeypatch):
    class MockResponse:
        def __init__(self, text, status_code):
            self.text = text
            self.status_code = status_code

    def mock_get(*args, **kwargs):
        return MockResponse('<html><h2 class="article-title">Test Title</h2></html>', 200)

    monkeypatch.setattr('requests.get', mock_get)

    url = 'https://example.com'
    titles = scrape_titles(url)
    assert titles == ['Test Title']