import requests
from bs4 import BeautifulSoup
import traceback
import re


def get_html_text(url, coding='utf-8'):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = coding
        return r.text
    except:
        return ""


def get_stock_list(lst, stock_list_url):
    html = get_html_text(stock_list_url, "GB2312")
    soup = BeautifulSoup(html, 'html.parser')
    a = soup.find_all('a')
    for i in a:
        try:
            href = i.attrs['href']
            lst.append(re.findall(r"[s][hz]\d{6}", href)[0])
        except:
            continue


def get_stock_info(lst, stock_info_url, fpath):
    # 1，splice stock info url
    # 2, get stock info from html page
    # 3, save stock info to file
    # 4, Continuously cycle this process
    count = 0
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
                key = key_list[i]
                val = value_list[i]
                info_dict[key] = val

            with open(fpath, 'a', encoding='utf-8') as f:
                f.write(str(info_dict) + '\n')
                count += 1
                print('\r当前进度: {:.2f}%'.format(count*100/len(lst)), end="")
        except:
            count += 1
            print('\r当前进度: {:.2f}%'.format(count * 100 / len(lst)), end="")
            continue


def main():
    stock_list_url = "http://quote.eastmoney.com/stocklist.html"
    stock_info_url = "https://gupiao.baidu.com/stock/"
    path = 'D:/StockInfo.txt'
    stock_list = []
    get_stock_list(stock_list, stock_list_url)
    get_stock_info(stock_list, stock_info_url, path)


main()
