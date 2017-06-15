# coding=utf-8

import requests
from bs4 import BeautifulSoup

class WebCrawler():
    """爬取网站的数据"""
    def __init__(self, url=None):
        self.url = url

    def get_html(self, url=None):
        """get the content of the url"""
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

        if url is not None:
            response = requests.get(url, headers=headers)
            response.encoding = 'utf-8'
            html = response.text

        elif self.url is not None:
            response = requests.get(self.url, headers=headers)
            response.encoding = 'utf-8'
            html = response.text

        return html

    def fetch_the_next_waiting_url(self, current_page_url):
        pass

    def get_contents(self, html, contents=[]):
        pass

