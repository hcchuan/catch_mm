# coding=utf-8
import urllib
import urllib.request
from urllib.parse import quote
import re
import os

#根据关键字单个获取百度图片
#运行：python I:\work\project\python\catch_mm\catch_one.py
images_folder = "I://work//project//python//catch_mm//images//"  # 图片保存目录

headers = {
    "Referer":"http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E8%8C%83%E5%86%B0%E5%86%B0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    "referer": "https://image.baidu.com"
}
print("****************************************************************************************")
keyword = input("请输入要下载的图片：")#手动输入关键字
son_folder = images_folder + keyword
if os.path.exists(son_folder) == False:
    os.mkdir(son_folder)
keyword1 = quote(keyword, encoding="utf-8")
url = "http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=" + keyword1
req = urllib.request.Request(url, headers=headers)
f = urllib.request.urlopen(req).read().decode("utf-8")
key = r'thumbURL":"(.+?)"'
key1 = re.compile(key)
num = 0
for string in re.findall(key1, f):
    print("正在下载" + string)
    f_req = urllib.request.Request(string, headers=headers)
    f_url = urllib.request.urlopen(f_req).read()
    fs = open(son_folder + "/" + keyword + str(num) + ".jpg", "wb+")
    fs.write(f_url)
    fs.close()
    num += 1
    print(string + "已下载成功")
input("按任意键结束程序：")