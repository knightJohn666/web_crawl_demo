# coding=utf-8

import requests
from bs4 import BeautifulSoup




def get_html(url):
    """get the content of the url"""
    response = requests.get(url)
    response.encoding = 'utf-8'
    return response.text


def get_img(html):
    """get the image of the html"""
    soup = BeautifulSoup(html, 'lxml')
    img_objs = soup.select('div.header a img')
    return img_objs

def get_certain_joke(html):
    """get the joke of the html"""
    soup = BeautifulSoup(html, 'lxml')
    joke_content = soup.select('div.content')[0].get_text()

    return joke_content

def get_url_list(url):
    """get all urls which needed to crawl"""
    urls = []
    urls.append(url)

    html = get_html(url)

    soup = BeautifulSoup(html, 'lxml')

    page_url_allover = soup.find('ul',{'class':'pagination'})

    for li_url in page_url_allover.find_all('li'):
        if li_url.find('span',{'class':'page-numbers'}):
            # print url + li_url.find('a').attrs['href']
            urls.append(url + li_url.find('a').attrs['href'])

    return urls


def get_jokes(html, jokes=[]):
    """get jokes of the html"""
    soup = BeautifulSoup(html, 'lxml')

    index = 0
    for joke_info in soup.find_all('div', {'class':'article block untagged mb15'}):
        joke = {}

        # 找到名字
        joke['Name'] = joke_info.find('h2').get_text()
        # print joke['Name']

        # 解析性别和年龄
        female = joke_info.find('div', {'class':'articleGender womenIcon'})
        male = joke_info.find('div', {'class':'articleGender manIcon'})
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
        joke['Content'] = joke_info.find('div',{'class':'content'}).get_text().strip()
        # print joke['Content']

        # 好笑度
        joke['FunnyLevel'] = joke_info.find('span', {'class':'stats-vote'}).get_text()
        # print joke['FunnyLevel']

        index += 1

        jokes.append(joke)
