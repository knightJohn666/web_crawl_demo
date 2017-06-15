#coding=utf-8

import url_config
from joke_web_crawler import JokeWebCrawler

jokes = list()

joke_crawler = JokeWebCrawler(url_config.joke_url)
current_page_url = joke_crawler.url

page_min = 1
page_num = 1
page_max = 3

for page_num in range(page_min, page_max + 1):
    html = joke_crawler.get_html(current_page_url)
    count = len(jokes)
    joke_crawler.get_contents(html, jokes)
    print 'Page ' + str(page_num) + '\n'

    for joke in jokes[count:]:
        print '用户名：' + joke['Name'].encode("utf-8")
        print '性别：' + joke['Gender']
        print '年龄：' + joke['Age'].encode("utf-8")
        print '内容：' + joke['Content'].encode("utf-8")
        print '搞笑度：' + joke['FunnyLevel'].encode("utf-8")
        print '\n\n'

    current_page_url = joke_crawler.fetch_the_next_waiting_url(current_page_url)

    page_num += 1