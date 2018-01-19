'''
抓取有道翻译接口
现在接口有校验获取的数据是乱码
'''
from urllib import request
from urllib import parse
import json
# res = request.urlopen("http://www.baidu.com")
# html = res.read()
# html = html.decode("utf-8")
# print(html)


def getResponseFromYouDao():
    Url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
    # 创建Form_Data字典，存储上图的Form Data
    Form_Data = {}
    Form_Data['type'] = 'AUTO'
    Form_Data['i'] = '赛利亚'
    Form_Data['doctype'] = 'json'
    Form_Data['version'] = '2.1'
    Form_Data['keyfrom'] = 'fanyi.web'
    Form_Data['ue'] = 'ue:UTF-8'
    Form_Data['action'] = 'FY_BY_CLICKBUTTON'
    # 使用urlencode方法转换标准格式
    data = parse.urlencode(Form_Data).encode("utf-8")
    # 传递Request对象和转换完格式的数据
    response = request.urlopen(Url, data)
    # 读取信息并解码
    html = response.read().decode("utf-8")
    # 使用JSON
    trans_data = json.loads(html)
    print(trans_data)
    # 找到翻译结果
    translate_Result = trans_data['translateResult'][0][0]['tgt']
    # 打印翻译信息
    print("翻译的结果是：%s" % translate_Result)


if __name__ == "__main__":
    getResponseFromYouDao()
