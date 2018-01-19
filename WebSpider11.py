'''
爬取煎蛋网 数据
'''
import requests
from bs4 import BeautifulSoup
def getOOXX(endPage):

    url = 'http://jandan.net/ooxx'
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }

    req = requests.get(url=url, headers=headers)
    req.encoding('utf-8')
    html = req.text
    bs0 = BeautifulSoup(html, 'lxml')
    result = bs0.find_all(class_='')
    for img_result in result:
        print(img_result)
