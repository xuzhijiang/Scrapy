import requests
from bs4 import BeautifulSoup
import bs4


def get_html_text(url, coding='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = coding
        return r.text
    except:
        return ""


def fill_university_list(lst, html):
    soup = BeautifulSoup(html, 'html.parser')
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            lst.append([tds[0].string, tds[1].string, tds[3].string])


def print_university_list(lst, num):
    tplt = "{1:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("学校排名", "学校名称", "学校评分", chr(12288)))
    for i in range(num):
        item = lst[i]
        print(tplt.format(item[0], item[1], item[2], chr(12288)))


def main():
    university_list = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = get_html_text(url)
    fill_university_list(university_list, html)
    print_university_list(university_list, 35)


main()