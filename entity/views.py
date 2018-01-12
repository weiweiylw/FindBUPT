from django.shortcuts import render,render_to_response,RequestContext
from models import UserProfile, Card, Tag, Department
import json
from django.http import HttpResponse
from middle import DepartmentSerializer, CardSerializer


# Create your views here.
response_data = {}


def card_create_view(request):
    if request.method == 'post':
        new_card = Card()
        new_card .name == request.POST['name'];
        new_card .praise_count = request.POST['type']
        new_card .description = request.POST['description']
        tags = Tag.objects.all()
        for i in tags:
            if i.key in new_card .description:
                new_card .tags.add(i)

        new_user_profile = UserProfile()
        new_user_profile.card = new_card
        request.user.userprofile = new_user_profile
        new_card.save()
        new_user_profile.save()
        response_data['result'] = True
        response_data['response_message'] = u'创建成功'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def card_change_view(request):
    if request.user.is_authenticated():
        this_card = request.user.userprofile.card
        this_card .name == request.POST['name']
        this_card .praise_count = request.POST['type']
        this_card .description = request.POST['description']
        this_card.save()
        response_data['result'] = True
        response_data['response_message'] = u'修改成功'
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def dag_create_view(request):
    return HttpResponse(json.dumps(response_data), content_type="application/json")


def department_view(request):
    if request.method == 'GET':
        this_department = Department.objects.get(id=request.POST['department_id'])
        department_data = DepartmentSerializer(this_department)
        return HttpResponse(json.dumps(department_data), content_type="application/json")


def card_view(request):
    if request.method == 'GET':
        this_card = Card.objects.get(id=request.POST['card_id'])
        card_data = CardSerializer(this_card)
        return HttpResponse(json.dumps(card_data), content_type="application/json")

