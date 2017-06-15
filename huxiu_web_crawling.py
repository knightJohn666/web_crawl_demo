# coding=utf-8

import url_config
from huxiu_web_crawler import HuXiuWebCrawler

huxiu_crawler = HuXiuWebCrawler(url_config.huxiu_url)

html = huxiu_crawler.get_html(huxiu_crawler.url)

contents = list()
huxiu_crawler.get_contents(html, contents)

print len(contents)

for content in contents:
    print content