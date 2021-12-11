"""
功能：下载指定 url 页面内的所有的 pdf 链接内容
语法：运行时附带 url 为参数
"""

from bs4 import BeautifulSoup as Soup
import requests
from sys import argv

# 获得含有所有a标签的一个列表
def getTagA(root_url):
    res = requests.get(root_url)
    soup = Soup(res.text,'html.parser')
    temp = soup.find_all("a")
    return temp

def downPdf(root_url):
    # 获取所有 a 标签中
    list_a = getTagA(root_url)
    number = 0
    for a_label in list_a:
        href_name = a_label.get("href")
        # 筛选出以.pdf结尾的 a 标签
        if href_name.lower().endswith(".pdf"):
            index = href_name.rfind("/")
            pdf_name = href_name[index+1:]
            number += 1
            print("try to download pdf %d"%number,end='  ')
            print(pdf_name+' downing.....')
            response = requests.get( href_name )
            with open(pdf_name,'wb') as file:
                file.write(response.content)

if __name__ == "__main__":
    try:
        # 用于获取命令行参数
        root_url = argv[1]
    except:
        print("please input url behind the script!!")
        exit()
    downPdf(root_url)
