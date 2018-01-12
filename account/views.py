#-*-coding:utf-8 -*-

from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

from django.http import HttpResponse
from django.shortcuts import render, render_to_response, RequestContext
#filter 实现 or
from django.db.models import Q

import json
import datetime
from entity.models import Card, UserProfile, Location, Department, Tag, PublicNotice
from getNotice import BUPTSpider
from getSCSTeachers import GetTeachers

# Create your views here.

response_data = {}

def login_view(request):
    user = authenticate(username=request.POST['username'], password=request.POST['password'])
    if user is not None:
        login(request, user)
        response_data['response_message'] = 'Welcome, '+user.username + "!"
        return HttpResponse(json.dumps(response_data), content_type="application/json")
    else:
        response_data['response_message'] = 'failed'
        json.dumps(response_data)
        return HttpResponse(json.dumps(response_data), content_type="application/json")


def logout_view(request):
    logout(request)
    response_data['response_message'] = 'GoodBye!'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def register_view(request):
    if request.method == 'POST':
        username_p = request.POST['username']
        password_p = request.POST['password']
        user = User.objects.create_user(username=username_p, password=password_p, email=username_p)
        if user:
            user.save
            response_data['result'] = True
            response_data['response_message'] = u'Reg Success!'
        else:
            response_data['result'] = False
            response_data['response_message'] = u"Reg Failed!"

        return HttpResponse(json.dumps(response_data), content_type="application/json")

def createPersonalInfo_view(request):
    if request.method == 'POST':
        name_p = request.POST['name']
        tags_p = request.POST['tags']
        usertype_p = request.POST['usertype']
        description_p = request.POST['description']
        #print name_p, tags_p, usertype_p, description_p

        user_g = User.objects.get(username=request.user)

        try:
            newCard = Card.objects.get(name = name_p)
        #创建新的名片
        except Card.DoesNotExist:
            newCard = Card(name = name_p, type_status = usertype_p, description = description_p, praise_count = 0)
            newCard.save()

        tagsList = tags_p.split(' ')
        for tag in tagsList:
            try:
                tagInstance = Tag.objects.get(key=tag)
            except Tag.DoesNotExist:
                newTag = Tag(key=tag, reference_count=1)
                newTag.save()
                newCard.tags.add(newTag)
            else:
                tagInstance.reference_count += 1
                tagInstance.save()
                newCard.tags.add(tagInstance)
        newCard.save()
        newUserProfile = UserProfile(user = user_g, card = newCard)
        newUserProfile.save()

        response_data['response_message'] = u'Success!'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def toPersonalManagement_view(request):
    return render_to_response('PersonalManage.html', RequestContext(request))

def toSharePosition_view(request):
    return render_to_response('SharePosition.html', RequestContext(request))

def sharePosition_view(request):
    if request.method == 'POST':
        positionx = request.POST['positionx']
        positiony = request.POST['positiony']
        #print positionx, positiony

        nowTime = str(datetime.datetime.now())
        locName = str(request.user) + " " + nowTime
        newLoc = Location(location_name=locName, position_x=positionx, position_y=positiony)
        #newLoc = Location(location_name=str(request.user), position_x=positionx, position_y=positiony)
        newLoc.save()

        user_g = User.objects.get(username=request.user)
        user_g.userprofile.card.location = newLoc
        user_g.userprofile.card.save()

        response_data['response_message'] = u'Success!'
        return HttpResponse(json.dumps(response_data), content_type="application/json")

def showSelfPosition_view(request):
    user_g = User.objects.get(username=request.user)
    if user_g.userprofile.card.location:
        positionx = user_g.userprofile.card.location.position_x
        positiony = user_g.userprofile.card.location.position_y
        return render_to_response('ShowSelfPosition.html', {'positionx': positionx, 'positiony': positiony}, RequestContext(request))
    else:
        return render_to_response('ShowSelfPosition.html', RequestContext(request))

def showPersonPosition_view(request):
    if request.method == 'GET':
        cId = request.GET['cardId']
        card = Card.objects.get(id=cId)
        positionx = card.location.position_x
        positiony = card.location.position_y
        return render_to_response('ShowPersonPosition.html', {'positionx': positionx, 'positiony': positiony, 'pName': card.name}, RequestContext(request))

def toFindPerson_view(request):
    #获取老师的爬虫
    '''
    crawler = GetTeachers()
    teacherList = crawler.start()
    for teacher in teacherList:
        if teacher[0].strip():
            Card.objects.create(name=teacher[0].strip(), type_status='TC', praise_count=0, description=teacher[1].strip())
    '''
    cardList = Card.objects.all()
    return render_to_response('FindPerson.html', {'cardList': cardList, 'found':False, 'findPersonPage':True}, RequestContext(request))
def findPerson_view(request):
    if request.method == 'GET':
        keywords = request.GET['keywords']

        try:
            tagList = Tag.objects.get(key=keywords)
        except Tag.DoesNotExist:
            cardList = Card.objects.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords))
        else: 
            cardList = Card.objects.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords)  |  Q(tags=tagList)).distinct()
        
        return render_to_response('FindPerson.html', {'cardList': cardList, 'found':True, 'findPersonPage':True}, RequestContext(request))

def toFindPlace_view(request):
    departmentList = Department.objects.all()
    return render_to_response('FindPlace.html', {'departmentList': departmentList, 'found':False, 'findPlacePage':True}, RequestContext(request))

def findPlace_view(request):
    if request.method == 'GET':
        keywords = request.GET['keywords']
        #print keywords
        #tagList = Tag.objects.filter(key__icontains=keywords)
        try:
            tagList = Tag.objects.get(key=keywords)
        except Tag.DoesNotExist:
            departmentList = Department.objects.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords))
        else: 
            departmentList = Department.objects.filter(Q(name__icontains=keywords) | Q(description__icontains=keywords) | Q(tags=tagList)).distinct()
        print departmentList
        return render_to_response('FindPlace.html', {'departmentList': departmentList, 'found':True, 'findPlacePage':True}, RequestContext(request))

def showPlacePosition_view(request):
    if request.method == 'GET':
        dId = request.GET['departmentId']
        department = Department.objects.get(id=dId)
        locationList = department.location.all()
        return render_to_response('ShowPlacePostion.html', {'locationList': locationList, 'dName': department.name, 'findPlacePage':True}, RequestContext(request))

def toFindNotice_view(request):
    #获取北邮要闻的爬虫
    '''
    s = BUPTSpider(1)
    noticeList = s.getNews()
    for notice in noticeList:
        #print notice[0].decode('utf-8')
        #print notice[3].decode('utf-8')
        try:
            noticeInstance = PublicNotice.objects.get(title=notice[0])
        except PublicNotice.DoesNotExist:
            newNotice = PublicNotice(title=notice[0], pub_time=notice[2], content=notice[3])
            newNotice.save()
        else:
            pass
    '''
    publicNoticeList = PublicNotice.objects.all()
    return render_to_response('FindNotice.html', {'publicNoticeList': publicNoticeList, 'found':False, 'findNoticePage':True}, RequestContext(request))

def findPublicNotice_view(request):
    if request.method == 'GET':
        keywords = request.GET['keywords']
        publicNoticeList = PublicNotice.objects.filter(Q(title__icontains=keywords) | Q(content__icontains=keywords))
        return render_to_response('FindNotice.html', {'publicNoticeList': publicNoticeList, 'found':True, 'findNoticePage':True}, RequestContext(request))

def showPublicNotice_view(request):
    if request.method == 'GET':
        nID = request.GET['noticeID']
        notice = PublicNotice.objects.get(id=nID)
        print notice.title
        return render_to_response('ShowPublicNotice.html', {'notice': notice, 'findNoticePage':True}, RequestContext(request))

def toFindPlaceByMap_view(request):
     return render_to_response('FindPlace_Map.html', RequestContext(request))

def toFindPersonTeacher_view(request):
    cardList = Card.objects.filter(type_status='TC')
    return render_to_response('FindPerson_Teacher.html', {'cardList': cardList, 'found':False, 'findPersonPage':True}, RequestContext(request))