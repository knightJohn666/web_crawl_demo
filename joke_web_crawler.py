# coding=utf-8

import requests
from bs4 import BeautifulSoup

from web_crawler import WebCrawler


class JokeWebCrawler(WebCrawler):
    """爬取糗事百科中的前3篇数据"""

    def fetch_the_next_waiting_url(self, current_page_url):
        """get next url which needed to crawl"""

        html = self.get_html(self.url)

        soup = BeautifulSoup(html, 'lxml')

        page_url_module = soup.find('ul', {'class': 'pagination'})
        next_page_url = ''

        for li_url in page_url_module.find_all('li'):
            if li_url.find('span', {'class': 'next'}) is not None \
                    and li_url.find('span', {'class': 'next'}).get_text().strip() == u'下一页':
                # 判断下一页是否存在
                next_page_url = self.url + li_url.find('a').attrs['href']
                break

        return next_page_url

    def get_contents(self, html, contents=[]):
        """get jokes of the html"""
        soup = BeautifulSoup(html, 'lxml')

        index = 0
        for joke_info in soup.find_all('div', {'class': 'article block untagged mb15'}):
            joke = dict()

            # 找到名字
            joke['Name'] = joke_info.find('h2').get_text()
            # print joke['Name']

            # 解析性别和年龄
            female = joke_info.find('div', {'class': 'articleGender womenIcon'})
            male = joke_info.find('div', {'class': 'articleGender manIcon'})
            if female:
                joke['Gender'] = '女'
                joke['Age'] = female.get_text()

            elif male:
                joke['Gender'] = '男'
                joke['Age'] = male.get_text()

            else:
                joke['Gender'] = '未知'
                joke['Age'] = u'未知'
            # print joke['Gender']
            # print joke['Age']

            # 内容
            joke['Content'] = joke_info.find('div', {'class': 'content'}).get_text().strip()
            # print joke['Content']

            # 好笑度
            joke['FunnyLevel'] = joke_info.find('span', {'class': 'stats-vote'}).get_text()
            # print joke['FunnyLevel']

            index += 1

            contents.append(joke)