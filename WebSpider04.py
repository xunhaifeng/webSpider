from urllib import request
from urllib import error
if __name__=="__main__":
    try:
        # 访问网址
        url = 'http://www.whatismyip.com.tw/'
        # 这是代理IP
        proxy = {'http': '61.135.217.7:80'}
        #创建代理对象
        proxy_handler=request.ProxyHandler(proxy)
        # 创建Opener
        opener =request.build_opener(proxy_handler)
        # 添加User Angent
        opener.addheaders = [('User-Agent',
                              'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
        # 安装OPener
        request.install_opener(opener)
        # 使用自己安装好的Opener
        response = request.urlopen(url,timeout=500)
        # 读取相应信息并解码
        html = response.read().decode("utf-8")
        # 打印信息
        print(html)
    except error.URLError as e:
        print(e.reason)
    except error.HTTPError as e:
        print(e.code+""+e.reason)