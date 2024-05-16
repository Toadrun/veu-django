import os

from django.shortcuts import render
from student.models import Student
# Create your views here.
from django.http import JsonResponse
import json
from django.db.models import Q
import uuid
import hashlib
from django.conf import settings
import os
def get_student(request):
    try:
        obj_students = Student.objects.all().values()
        students = list(obj_students)

        return JsonResponse({'code': 1, 'data': students})

    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "The error is :" + str(e)})


def query_student(request):
    # search, jieshou AXIOS, json geshi, zidianleixing
    data = json.loads(request.body.decode('utf-8'))

    try:
        obj_student = Student.objects.filter(Q(sno__icontains=data['inputstr']) |
                                             Q(name__icontains=data['inputstr']) |
                                             Q(gender__icontains=data['inputstr']) |
                                             Q(mobile__icontains=data['inputstr']) |
                                             Q(email__icontains=data['inputstr']) |
                                             Q(address__icontains=data['inputstr'])).values()
        students = list(obj_student)

        return JsonResponse({'code': 1, 'data': students})

    except Exception as e:
        return JsonResponse({'code': 0, 'msg': "The error is :" + str(e)})


def is_exsits_sno(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_students = Student.objects.filter(sno=data['sno'])
        if obj_students.count() == 0:
            return JsonResponse({'code': 1, 'exsits': 'False'})
        else:
            return JsonResponse({'code': 1, 'exsits': 'True'})
    except Exception as e:
        return JsonResponse({'code': 0, 'msg': 'error:' + str(e)})


def add_student(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_student = Student(sno=data['sno'],
                              name=data['name'],
                              gender=data['gender'],
                              mobile=data['mobile'],
                              email=data['email'],
                              address=data['address'])
        obj_student.save()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': '0', 'msg': 'error:' + str(e)})


def update_student(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_student = Student.objects.get(sno=data['sno'])
        obj_student.name = data['name']
        obj_student.gender = data['gender']
        obj_student.mobile = data['mobile']
        obj_student.email = data['email']
        obj_student.address = data['address']

        obj_student.save()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': '0', 'msg': 'error:' + str(e)})


def delete_student(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        obj_students = Student.objects.filter(sno=data['sno'])
        obj_students.delete()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': '0', 'msg': 'error:' + str(e)})

def delete_students(request):
    data = json.loads(request.body.decode('utf-8'))
    try:
        for cur_student in data['students']:
            obj_student = Student.objects.get(sno = cur_student['sno'])
            obj_student.delete()
        obj_students = Student.objects.all().values()
        students = list(obj_students)
        return JsonResponse({'code': 1, 'data': students})
    except Exception as e:
        return JsonResponse({'code': '0', 'msg':'error' + str(e)})


def upload(request):
    rev_file = request.FILES.get('avatar')
    if not rev_file:
        return JsonResponse({'code':'0','msg':'no image'})
    new_name = get_random_str()
    file_path = os.path.join(settings.MEDIA_ROOT,new_name )
    print(file_path)
    try:
        f = open(file_path,'wb')
        for i in rev_file.chunks():
            f.write(i)
        f.close()
        return JsonResponse({'code':'1','name':new_name })
    except Exception as e:
        return JsonResponse({'code':'0','msg':'error:' + str(e)})



def get_random_str():
    uuid_val = uuid.uuid4()
    uuid_str = str(uuid_val).encode('utf-8')
    md5 = hashlib.md5()
    md5.update(uuid_str)
    return md5.hexdigest()


def import_students_excel(request):
    rev_file = request.FILES.get('excel')
    if not rev_file:
        return JsonResponse({'code':'0','msg':'no exists'})
    new_name = get_random_str()
    file_path = os.path.join(settings.MEDIA_ROOT, new_name+os.path.splitext(rev_file)[1])
