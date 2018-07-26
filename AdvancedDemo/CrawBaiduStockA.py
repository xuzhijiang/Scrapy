import requests
from bs4 import BeautifulSoup
from urllib3.exceptions import HTTPError
import re
import traceback


def get_html_text(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except HTTPError:
        return ""


def get_stock_list(lst, stock_list_url):
    html_text = get_html_text(stock_list_url)
    soup = BeautifulSoup(html_text, "html.parser")
    a = soup.find_all('a')
    for t in a:
        try:
            href = t.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def get_stock_info(lst, stock_info_url, fpath):
    for stock in lst:
        url = stock_info_url + stock + ".html"
        html = get_html_text(url)
        try:
            if html == "":
                continue
            info_dict = {}
            soup = BeautifulSoup(html, 'html.parser')
            stock_info = soup.find('div', attrs={'class': 'stock-bets'})

            name = stock_info.find_all(attrs={'class': 'bets-name'})[0]
            info_dict.update({'股票名称': name.text.split()[0]})

            key_list = stock_info.find_all('dt')
            value_list = stock_info.find_all('dd')
            for i in range(len(key_list)):
                key = key_list[i].text
                val = value_list[i].text
                info_dict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(info_dict) + '\n')
        except:
            traceback.print_exc()
            continue


def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    # backup: http://finance.sina.com.cn/stock/
    output_file = "D:/BaiduStockInfo.txt"
    stock_list = []
    get_stock_list(stock_list, stock_list_url)
    get_stock_info(stock_list, stock_info_url, output_file)


main()
