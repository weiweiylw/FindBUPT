# -*- coding: utf-8 -*-

import re
import urllib2
import sys
from datetime import datetime

class BUPTSpider():

    def __init__(self, pages, today=False):
        self.__titleBaseUrl = 'http://www.bupt.edu.cn/list/list.php?p=81_15_'
        self.__contentBaseUrl = 'http://www.bupt.edu.cn'
        self.__titlePtn = re.compile(r'<li><a\s+href="(.*?)"\s+title="(.*?)"><font\s+class="cor3 rt padl10">(.*?)</font>.*?</a></li>')
        self.__contentPtn = re.compile(r'<div class="content detail">(.*?)</div>', re.S)
        self.__pages = pages
        self.__today = today
        self.__news  = []

    def __getNewsTitle(self):
        if self.__today:
            pages = 10
        else:
            pages = self.__pages
        for p in range(pages):
            try:
                response = urllib2.urlopen(self.__titleBaseUrl + str(p+1), timeout=5)
            except Exception:
                pass
            else:
                html = response.read()
                titleList = self.__titlePtn.findall(html)
                for title in titleList:
                    url, title, time = title
                    date = datetime.strptime(time, '%Y-%m-%d').date()
                    if self.__today:
                        if date == datetime.now().date():
                            self.__news.append([title, url, date,''])
                    else:
                        self.__news.append([title, url, date,''])

    def __getNewsContent(self):
        for n in self.__news:
            try:
                response = urllib2.urlopen(self.__contentBaseUrl + n[1], timeout=5)
            except Exception:
                pass
            else:
                html = response.read()
                content = self.__contentPtn.findall(html)
                imgPtn = re.compile(r'<img\salt=""\ssrc="/upload')
                content_imgURL = imgPtn.sub('<img alt="" src="http://www.bupt.edu.cn/upload', content[0])
                n[3] = content_imgURL

    def getNews(self):
        self.__getNewsTitle()
        self.__getNewsContent()
        return self.__news