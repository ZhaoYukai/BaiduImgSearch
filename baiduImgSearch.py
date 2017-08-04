# -*- coding:utf-8 -*-

#推荐运行在MacOS或linux操作系统下面，Windows运行会遇到字符编码的问题尚未解决

#Python版本：2.7

#运行方法：在命令行中输入下列命令，同时确保机器中已经安装了python的requests模块
#如果尚未安装requests模块，则使用命令pip install -U requests进行安装

#python baiduImgSearch.py dog /Users/zhaoyukai/Python/baiduImgs/ 10
#参数说明：
#(1)baiduImgSearch.py 这个是本文件的文件名
#(2)dog 这个是要搜索的关键字，可以是中文
#(3)/Users/zhaoyukai/Python/baiduImgs/ 指定下载的图片保存的路径
#(4)10 这个是要爬的百度图片页面范围，10代表第1至第10页内的所有图片

import os
import sys
import urllib
import requests
import time


def CheckArgs():
    if len(sys.argv) < 3:
        print 'Usage: python baiduImgSearch.py [Keyword] [DownloadDir] [Pages=1]'
        return False
    return True


def Download(url, filename):
    if os.path.exists(sys.argv[2]) == False:
        os.mkdir(sys.argv[2])
    filepath = os.path.join(sys.argv[2], '%s' % filename)
    urllib.urlretrieve(url, filepath)
    return


def Request(param):
    searchurl = 'https://image.baidu.com/search/acjson'
    response = requests.get(searchurl, params=param)
    json = response.json()['data']

    for i in range(0, len(json)):
        if 'thumbURL' in json[i].keys():
            filename = json[i]['thumbURL']
            filename = filename.split(",")[-1]
            timeStr = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
            filename = timeStr + filename
            print 'Downloading from %s' % filename
            Download(json[i]['thumbURL'], filename)
    return


def file_count(dirname, filter_types=[]):
    count = 0
    filter_is_on = False
    if filter_types:
        filter_is_on = True
    for item in os.listdir(dirname):
        abs_item = os.path.join(dirname, item)
        # print item
        if os.path.isdir(abs_item):
            # Iteration for dir
            count += file_count(abs_item, filter_types)
        elif os.path.isfile(abs_item):
            if filter_is_on:
                # Get file's extension name
                extname = os.path.splitext(abs_item)[1]
                if extname in filter_types:
                    count += 1
            else:
                count += 1
    return count


def Search():
    params = {
        'tn': 'resultjson_com',
        'ipn': 'rj',
        'ct': '201326592',
        'is': '',
        'fp': 'result',
        'queryWord': sys.argv[1],
        'cl': '2',
        'lm': '-1',
        'ie': 'utf-8',
        'oe': 'utf-8',
        'adpicid': '',
        'st': '-1',
        'z': '',
        'ic': '0',
        'word': sys.argv[1],
        's': '',
        'se': '',
        'tab': '',
        'width': '',
        'height': '',
        'face': '0',
        'istype': '2',
        'qc': '',
        'nc': '1',
        'fr': '',
        'pn': '30',
        'rn': '30',
        'gsm': '1e',
        '1501831361559': ''
    }

    if len(sys.argv) == 4:
        pages = int(sys.argv[3])
    else:
        pages = 1

    for i in range(0, pages):
        params['pn'] = '%d' % i
        Request(params)
    return


if __name__ == '__main__':
    if CheckArgs() == False:
        sys.exit(-1)
    Search()
    print 'Total Images:%d' % file_count(sys.argv[2])