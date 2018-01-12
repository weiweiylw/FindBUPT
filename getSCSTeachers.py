# -*- coding: utf-8 -*-

import re
import urllib2
import sys
from datetime import datetime
from bs4 import BeautifulSoup

reload(sys) 
sys.setdefaultencoding('utf-8')


class GetTeachers():

    def __init__(self):
        self.__BaseUrl = 'http://scs.bupt.edu.cn/cs_web/showTeacher1.aspx?id='
        self.__contentPtn = re.compile(r'<table width="616"  border="1" cellspacing="0" bordercolor="#dcdcdc" style="TABLE-LAYOUT: fixed;WORD-WRAP: break-word" class="border_table">(.*?)</table>',re.S)
        self.__teacherList = []

    def __crawl(self):

        for i in range(20,143):
            teacher = []
            description = ''

            response = urllib2.urlopen(self.__BaseUrl + str(i), timeout=5)
            content = BeautifulSoup(response, from_encoding="gb18030")

            infomation = content.find('table')
            trs = infomation.findAll('tr')

            #姓名
            tNametd = trs[0].findAll('td')
            tName = tNametd[1].text
            teacher.append(tName)
            #描述
            for tr in trs[1:10]:
                tds = tr.findAll('td')
                td = tds[1].text
                description = description + td.strip() + '|'
            teacher.append(description)
            self.__teacherList.append(teacher)

    def start(self):
        self.__crawl()
        return self.__teacherList