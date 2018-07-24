import requests
import re


def get_html_txt(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def parse_page(lst, html):
    try:
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*\"', html)
        tlt = re.findall(r'\"raw_title\"\:\".*?\"', html)
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            lst.append([price, title])
    except:
        print("")
    pass


def print_goods_info(lst):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format("序号", "价格", "商品名称"))
    count = 0
    for g in lst:
        count += 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    start_url = "https://s.taobao.com/search?q=" + goods
    depth = 3
    info_list = []
    for i in range(depth):
        try:
            url = start_url + "&s=" + str(44 * i)
            html = get_html_txt(url)
            parse_page(info_list, html)
        except:
            continue
    print_goods_info(info_list)


main()
