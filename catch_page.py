# coding=utf-8
import urllib
import urllib.request
from urllib.parse import quote
import requests
import re
from urllib import request
import os
import time, datetime

#根据关键字字典翻页获取百度图片
#运行：python I:\work\project\python\catch_mm\catch_page.py
project_folder = "I://work//project//python//catch_mm//"  # 图片保存目录
images_folder = project_folder+"images//"  # 图片保存目录

headers = {
    "Referer":"http://image.baidu.com/search/index?tn=baiduimage&ps=1&ct=201326592&lm=-1&cl=2&nc=1&ie=utf-8&word=%E8%8C%83%E5%86%B0%E5%86%B0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36",
    "referer": "https://image.baidu.com"
}

def get_picture_list(keyword,biggest_pages):
    all_picture_list = []
    for page in range(biggest_pages):# 每一页20张图片， 所以翻页的是0 20 40 80 这样变化的
        page = page * 20
        url = 'https://image.baidu.com/search/flip?tn=baiduimage&ie=utf-8&word={}&pn={}'.format(keyword, page)
        html = requests.get(url, headers = headers, allow_redirects=False).content.decode('utf-8')
        picture_list = re.findall('{"thumbURL":"(.*?)",', html)# 用正则匹配，获得图片的url
        all_picture_list.extend(picture_list)
        img_list = list(set(all_picture_list))# 因为第二页也有后面两页的图片，所以要去重　　
        download_picture(keyword,img_list)

#---------------------------根据关键字采集百度图片
def catch_img(keyword,url,image_index):
    son_folder = images_folder + keyword
    if os.path.exists(son_folder) == False:
        os.mkdir(son_folder)

    f_req = urllib.request.Request(url, headers=headers)
    f_url = urllib.request.urlopen(f_req).read()
    fs = open(son_folder + "/" + keyword + str(image_index+1) + ".jpg", "wb+")
    fs.write(f_url)
    fs.close()
    print('采集完成：' + url)

# 下载图片
def download_picture(keyword,all_picture_list):
    for i, pic_url in enumerate(all_picture_list):
        catch_img(keyword, pic_url,i)

# 开始函数
def start():
    # 采集页数
    biggest_pages = 2
    with open(project_folder + "keywords.txt", "r", encoding='UTF-8') as f:
        for line in f.readlines():
            line = line.strip('\n')  # 去掉列表中每一个元素的换行符
            get_picture_list(line, biggest_pages)

if __name__ == "__main__":
    start()
    print('---------------全部采集完成！-----------------')