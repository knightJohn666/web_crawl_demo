# coding=utf-8

import requests
from bs4 import BeautifulSoup

from web_crawler import WebCrawler


class XiCiDaiLiWebCrawler(WebCrawler):
    """实现对西刺代理国内匿名代理的数据爬取"""

    def get_html(self, url=''):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'}

        html = ''
        if url != '':
            response = requests.get(url, headers=headers)
            response.encoding = 'utf-8'
            html = response.text

        elif self.url != '':
            response = requests.get(self.url, headers=headers)
            response.encoding = 'utf-8'
            html = response.text

        else:
            print 'no available url!'

        return html

    def fetch_the_next_waiting_url(self, current_page_url):
        """get next url which needed to crawl"""

        html = self.get_html(self.url)

        soup = BeautifulSoup(html, 'lxml')

        page_url_module = soup.find('div', {'class': 'pagination'})
        # print page_url_module
        next_page_url = ''

        if page_url_module.find('a', {'class': 'next_page'}):
            # 下一页存在
            temp_next_page_url = page_url_module.find('a').attrs['href'].split('/')
            next_page_url = self.url + '/' + temp_next_page_url[len(next_page_url) - 1]

        return next_page_url

    def get_contents(self, html, contents=[]):

        soup = BeautifulSoup(html, 'lxml')

        trs = soup.find('table', id='ip_list').find_all('tr')
        for tr in trs[1:]:
            content = dict()
            tds = tr.find_all('td')

            content['IPAddress'] = tds[1].get_text()
            # print content['IPAddress']
            content['Port'] = tds[2].get_text()
            # print content['Port']

            contents.append(content)

