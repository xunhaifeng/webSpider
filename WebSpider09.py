'''
 Python3网络爬虫(九)：使用Selenium爬取百度文库word文章
 TODO 失败获取的不对
https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html
'''
from selenium import webdriver
from bs4 import BeautifulSoup
import time

option = webdriver.ChromeOptions()
option.add_argument('user-agent="Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Mobile Safari/537.36"')

driver = webdriver.Chrome(chrome_options=option)
driver.get('https://wenku.baidu.com/view/aa31a84bcf84b9d528ea7a2c.html')
# 先点击继续阅读
float_button = driver.find_element_by_xpath("//div[@class='flod-button']")
float_button.click()
time.sleep(5)

# 延时5秒后 滑动到下一页
page_mark = driver.find_elements_by_xpath("//div[@class='page_mark']")
driver.execute_script('arguments[0].scrollIntoView();', page_mark[-1]) #拖动到可见的元素去

html = driver.page_source
b0 = BeautifulSoup(html, 'lxml')
print(b0)
result = b0.find_all(class_='sf-edu-wenku-id-page5')
for pItem in  result:
    b1 = BeautifulSoup(str(pItem), 'lxml')
    p_result = b1.find_all('p')
    for p_text in p_result:
        main_body = BeautifulSoup(p_text, 'lxml')
        for each in main_body.find(True):
            print(each.string.replace('\xa0',''),end='')
# page_next = driver.find_element_by_xpath("//div[@class='x-page next']")
# page_next.click()