# BaiduImgSearch
百度图片爬虫

推荐运行在MacOS或linux操作系统下面，Windows运行会遇到字符编码的问题尚未解决<br>
如果在windows下运行可能会报ValueError: No JSON object could be decoded的错误

Python版本：2.7

运行方法：在命令行中输入下列命令，同时确保机器中已经安装了python的requests模块<br>
如果尚未安装requests模块，则使用命令<br>
```
pip install -U requests
```
<br>进行安装
```
python baiduImgSearch.py dog /Users/zhaoyukai/Python/baiduImgs/ 10
```
参数说明：<br>
(1)baiduImgSearch.py 这个是本文件的文件名<br>
(2)dog 这个是要搜索的关键字，可以是中文<br>
(3)/Users/zhaoyukai/Python/baiduImgs/ 指定下载的图片保存的路径<br>
(4)10 这个是要爬的百度图片页面范围，10代表第1至第10页内的所有图片<br>
