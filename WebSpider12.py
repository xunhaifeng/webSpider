'''
D:\icity365\develop\phantomjs-2.1.1-windows/bin/phantomjs.exe
'''
from lxml import etree
from bs4 import BeautifulSoup
import requests
if __name__ == "__main__":
    page = 1
    target_url = 'http://www.xicidaili.com/nn/%d' % page
    S = requests.session()
    headers={
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Referer': 'http://www.xicidaili.com/nn/',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8',
    }
    response = S.get(url=target_url, headers=headers)
    response.encoding = 'utf-8'
    target_html = response.text
    html = BeautifulSoup(target_html, 'lxml')
    iplist = html.find_all(id='ip_list')
    tab_list = BeautifulSoup(str(iplist), 'lxml')
    ip_list_info = tab_list.table.contents

    ip_list=[]

    for index in range(len(ip_list_info)):
        if index % 2 == 1 and index != 1:
            dom = etree.HTML(str(ip_list_info[index]))
            ip = dom.xpath('//td[2]')
            port = dom.xpath('//td[3]')
            protocol = dom.xpath('//td[6]')
            ip_list.append(protocol[0].text.lower() + '#' + ip[0].text + '#' + port[0].text)
    print(ip_list)
