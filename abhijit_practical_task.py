from bs4 import BeautifulSoup
import json
import urllib.request

class WebScraper:
    def __init__(self, url):
        self.url = url
        self.news_data = {}

    def fetch_html_content(self):
        req = urllib.request.urlopen(self.url)
        self.html_content = req.read()

    def extract_data(self):
        soup = BeautifulSoup(self.html_content, 'html.parser')
        headline = soup.find('h1', itemprop='headline')

        if headline:
            self.news_data['headline'] = headline.get_text(strip=True)

        paragraphs = [p.get_text(separator=' ', strip=True) for p in soup.find_all('p')]
        self.news_data['content'] = paragraphs

    def save_to_json(self, filename):
        json_data = json.dumps(self.news_data, indent=4)
        with open(filename, 'w') as file:
            file.write(json_data)
            print("Data Scrapped SuccessFully..!")

url = 'https://indianexpress.com/article/india/parliament-winter-session-2023-live-news-updates-stalement-9072430/'

scraper = WebScraper(url)
scraper.fetch_html_content()
scraper.extract_data()
scraper.save_to_json('extracted_data.json')
