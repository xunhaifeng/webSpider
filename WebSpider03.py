from urllib import request
from urllib import parse

if __name__=="__main__":
    url="http://www.csdn.net"
    #方法一
    headers={}
    # 写入User Agent信息
    #header['User-Agent'] = 'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'
    #req = request.Request(url,headers=header)
    req = request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19")
    response = request.urlopen(req)
    print(response.read().decode('utf-8'))