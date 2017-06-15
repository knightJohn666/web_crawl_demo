#coding=utf-8

import url_config
from xicidaili_web_crawler import XiCiDaiLiWebCrawler

contents = list()

xicidaili_crawler = XiCiDaiLiWebCrawler(url_config.xicidaili_home_url)
current_page_url = xicidaili_crawler.url

page_min = 1
page_num = 1
page_max = 2

for page_num in range(page_min, page_max + 1):
    start_position = len(contents)

    # 获得html文档
    html = xicidaili_crawler.get_html(current_page_url)

    # 解析html文档
    xicidaili_crawler.get_contents(html, contents)

    # 获取下一个
    current_page_url = xicidaili_crawler.fetch_the_next_waiting_url(current_page_url)

    # 显示获取到的数据
    print '\nPage: ' + str(page_num) + "\n\n"
    for content in contents[start_position:]:
        print 'IPAddress:' + content['IPAddress'] + '\tPort: ' + content['Port']

    page_num += 1