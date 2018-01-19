'''
爬取笔趣小说 指定章节的文字

'''
from urllib import request
from urllib import error
from bs4 import BeautifulSoup

if __name__ == "__main__":
    try:
        download_url = 'http://www.biqukan.com/1_1094/5403177.html'
        agent = '''Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) 
           Gecko/20100101 Firefox/21.0'''
        header = {}
        header['UserAgent'] = agent
        req = request.Request(url=download_url, headers=header)
        response = request.urlopen(req)
        res = response.read().decode("gbk", 'ignore')
        sour = BeautifulSoup(res, 'lxml')
        sour_text = sour.find_all(id='content', class_='showtxt')
        # print(sour_text)
        soup_text = BeautifulSoup(str(sour_text), 'lxml')
        print(soup_text.div.text.replace('\xa0', ''))
    except error.HTTPError as e:
        pass
