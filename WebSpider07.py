'''
抓取笔趣小说的所有章节
'''
from urllib import request
from urllib import error
from bs4 import BeautifulSoup
import sys

if __name__ == '__main__':

    try:
        # 创建txt文件
        file = open('一念永恒.txt', 'w', encoding='utf-8')
        url = 'http://www.biqukan.com/1_1094/'
        header = {}
        header['UserAgent'] = '''Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0)
            Gecko/20100101 Firefox/21.0'''
        req = request.Request(url, headers=header)
        response = request.urlopen(req)
        res_txt = response.read().decode('gbk', 'ignore')
        # 创建BeautifulSoup对象
        listMain = BeautifulSoup(res_txt, 'lxml')
        # 读取齐总div标签 class=listmain
        listText = listMain.find_all('div', class_='listmain')
        listSoup = BeautifulSoup(str(listText), 'lxml')
        # 计算章节个数
        numbers = (len(listSoup.dl.contents) - 1) / 2 - 8
        index = 1
        # 开始记录内容标志位,只要正文卷下面的链接,最新章节列表链接剔除
        begin_flag = False

        for child in listSoup.dl.children:
            if child != '\n':
                if child.string == u'《一念永恒》正文卷':
                    begin_flag = True
                # 爬取链接
                if begin_flag is True and child.a is not None:
                    download_url = "http://www.biqukan.com" + child.a.get('href')
                    download_name = child.string
                    # print(download_name + " : " + download_url)
                    req = request.Request(url=download_url, headers=header)
                    response = request.urlopen(req)
                    res_section = response.read().decode('gbk', 'ignore')
                    soup_section = BeautifulSoup(res_section, 'lxml')
                    texts = soup_section.find_all(id='content', class_='content')
                    text_lxml = BeautifulSoup(str(texts), 'lxml')
                    write_flat = True
                    file.write(download_name + '\n\n')
                    for each in text_lxml.div.text.replace('\xa0', ''):
                        if each == 'h':
                            write_flag = False
                        if write_flag is True and each != ' ':
                            file.write(each)
                        if write_flag is True and each == '\r':
                            file.write('\n')
                file.write('\n\n')
                # 打印爬取进度
                sys.stdout.write("已下载:%.3f%%" % float(index/numbers) + '\r')
                sys.stdout.flush()
                index += 1
        file.close()
    except error.HTTPError as e:
        raise e
    except error.URLError as e:
        pass