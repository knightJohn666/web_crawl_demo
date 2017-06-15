# coding=utf-8

from bs4 import BeautifulSoup

from web_crawler import WebCrawler


class HuXiuWebCrawler(WebCrawler):
    """爬取虎嗅网的文章列表的url"""

    def get_contents(self, html, contents=[]):

        soup = BeautifulSoup(html, 'lxml')
        # 获得虎嗅网的文章的url
        self.get_article_url_list(soup, contents)

    def get_article_url_list(self, soup, contents=[]):
        """获得虎嗅网的文章的url"""

        if soup:
            for div in soup.find_all('div', {'class':'mod-b mod-art '}):
                if div.find('div', {'class':'mod-thumb video-mod-thumb'}):
                    contents.append(self.url + div.find('div', {'class':'mod-thumb video-mod-thumb'}).find('a').attrs['href'])

                if div.find('div', {'class':'mod-thumb '}):
                    contents.append(self.url + div.find('div', {'class': 'mod-thumb '}).find('a').attrs['href'])

            for div in soup.find_all('div', {'class':'mod-b mod-art mod-b-push '}):
                if div.find('div', {'class':'mod-thumb '}):
                    contents.append(self.url + div.find('a').attrs['href'])