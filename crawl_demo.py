#coding=utf-8

import crawl_function as cf

url = "http://www.100szy.com/"
url_joke = "https://www.qiushibaike.com"


html = cf.get_html(url_joke)
joke_content = cf.get_certain_joke(html)
print joke_content
# jokes = []
#
# urls = cf.get_url_list(url_joke)
# page_num = 1
# page_max = 3

# for url in urls:
#     html = cf.get_html(url)
#     count = len(jokes)
#     cf.get_jokes(html, jokes)
#     print 'Page ' + str(page_num) + '\n'
#
#     for joke in jokes[count:]:
#         print '用户名：' + joke['Name'].encode("utf-8")
#         print '性别：' + joke['Gender']
#         print '年龄：' + joke['Age'].encode("utf-8")
#         print '内容：' + joke['Content'].encode("utf-8")
#         print '搞笑度：' + joke['FunnyLevel'].encode("utf-8")
#         print '\n\n'
#
#     page_num += 1
#
#     if page_num > page_max:
#         break