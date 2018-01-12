#coding:utf-8  
  
from django import template  
  
register = template.Library()  
  
def percent_decimal(value):  
    description = value.split('|')[4:6] 
    department = description[0]
    job = description[1]
    return department + ' ' + job
    #return str(value) + '%'  
register.filter('percent_decimal', percent_decimal)

def output_teacher(value): 
	
    description = value.split('|')
    column = [u'性别：',u'职务：',u'学术兼职：', u'老师类型：', u'所属中心：', u'职称：', u'承担课程：', u'研究方向：', u'个人介绍：','']
    output = u''
    for index,des in enumerate(description):
    	#print index, des.encode('utf-8')
   		output += column[index] + des + '<br />'
    return output
register.filter('output_teacher', output_teacher)

def output_teacher_self(value): 
    description = value.split('|')
    selfDescription = description[8]
    return selfDescription
register.filter('output_teacher_self', output_teacher_self)