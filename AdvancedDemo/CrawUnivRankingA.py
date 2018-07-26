import requests
from bs4 import BeautifulSoup
import bs4


def get_html_text(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fill_university_list(lst, html):
    soup = BeautifulSoup(html, "html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            lst.append([tds[0].string, tds[1].string, tds[3].string])


def print_university(lst, num):
    print("{:^10}\t{:^6}\t{:^10}".format("排名", "学校名称", "总分"))
    for i in range(num):
        u = lst[i]
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))
    pass


def main():
    university_list = []
    url = "http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html"
    html = get_html_text(url)
    fill_university_list(university_list, html)
    print_university(university_list, 20)


main()
