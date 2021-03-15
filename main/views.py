from django.shortcuts import render,HttpResponse,redirect
from acount import models
from datetime import datetime
from static.py import FY
import random
import json
from main import Form
def index(request):
    if request.session.get('user'):
        us_id = str(models.Userinfo.objects.filter(user=request.session['user']).values('id')[0]['id'])
        file_path = models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
        return render(request,'index.html',{'file_path':file_path,'u_id':us_id})
    else:
        return redirect('/acount/sigh_in.html')

def sys(request):
    pass

def stu(request):
    if request.session.get('user'):
        if request.method == 'GET':
            obj = Form.StuForm()
            us_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')[0]['id']
            file_path ='/' +  models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
            last_id = models.student.objects.filter(id__gt=1).count()
            page_info  = FY.Pageinfo(request.GET.get('page'),all_count=last_id,per_page=10,base_url='/main/stu.html')
            student_list = models.student.objects.all()[page_info.start():page_info.end()]
            return render(request,'student.html',{'stu_list':student_list,'page_info':page_info,'file_path':file_path,'u_id':us_id,'obj':obj})
        else:
            if request.POST.get('ys'):
                page = request.POST.get('ys')
                if int(page) <=0:
                    return redirect('/main/stu.html?page=1')
                else:
                    all_id = models.student.objects.filter(id__gt=1).count()
                    if int(page)>int(all_id):
                        last_page = all_id // 10
                        if all_id%10:
                            last_page += 1
                            return redirect('/main/stu.html?page=%s'%last_page)
                        return redirect('/main/stu.html?page=%s'%last_page)
                    return redirect('/main/stu.html?page=%s'% page)
            if request.POST.get('ss'):
                msg = request.POST.get('ss')
                return redirect('http://127.0.0.1:8000/main/serch/%s'%msg)
            else:
                obj = Form.StuForm()
                us_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')[0]['id']
                file_path ='/' +  models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
                last_id = models.cls.objects.filter(id__gt=1).count()
                page_info  = FY.Pageinfo(request.GET.get('page'),all_count=last_id,per_page=10,base_url='/main/cls.html')
                student_list = models.student.objects.all()[page_info.start():page_info.end()]
                msg = '搜索框不能为空'
                return render(request,'student.html',{'stu_list':student_list,'page_info':page_info,'file_path':file_path,'u_id':us_id,'obj':obj,'msg':msg})
    else:
        return redirect('/acount/sigh_up.html')

def serch(request,msg):
    us_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')[0]['id']
    s_info = models.student.objects.filter(name__contains=msg)
    file_path ='/' +  models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
    return render(request,'serch.html',{'file_path':file_path,'s_info':s_info,'u_id':us_id})

def edit_s(request,s_id):
    if request.session.get('user'):
        if request.method == 'GET':
            su_info = models.student.objects.filter(id=s_id)
            for i in su_info:
                s_info = i
            obj = Form.StuForm(initial={'name':s_info.name,'age':s_info.age,'sex':s_info.sex,'cls_id':s_info.cls.id})
            us_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')[0]['id']
            file_path ='/' +  models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
            return render(request,'edit_s.html',{'file_path':file_path,'obj':obj,'sid':s_id})
        else:
            obj = Form.StuForm(request.POST)
            if obj.is_valid():
                models.student.objects.filter(id=s_id).update(**obj.cleaned_data)
                return redirect('http://127.0.0.1:8000/main/stu.html?page=1')
            else:
                return render(request,'edit_s.html',{'obj':obj})

def delete(request):
    ret = {'status':True,'msg':None}
    try:
        s_id = request.POST.get('s_id')
        models.student.objects.filter(id=s_id).delete()
    except Exception as e:
        ret['status'] = False
        ret['msg'] = str(e)
    return HttpResponse(json.dumps(ret))

def add(request):
    ret = {'status':True,'msg':None}
    name = request.POST.get('name')
    age = request.POST.get('age')
    sex = request.POST.get('sex')
    cls_id = request.POST.get('cls_id')
    try:
        models.student.objects.create(name=name,age=age,sex=sex,cls_id=cls_id)
    except Exception as e:
        ret['status'] = False
        ret['msg']  = str(e)
    return HttpResponse(json.dumps(ret))

def cls(request):
    if request.session.get('user'):
        if request.method == 'GET':
            last_id = models.cls.objects.filter(id__gt=1).count()
            page_info  = FY.Pageinfo(request.GET.get('page'),all_count=last_id,per_page=10,base_url='/main/cls.html')
            us_id = str(models.Userinfo.objects.filter(user=request.session['user']).values('id')[0]['id'])
            file_path = '/' + models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
            cls_list = models.cls.objects.all()[page_info.start():page_info.end()]
            obj = Form.ClsForm()
            return render(request,'cls.html',{'file_path':file_path,'cls_list':cls_list,'obj':obj,'page_info':page_info,'u_id':us_id})
        else:
            if request.POST.get('ys'):
                page = request.POST.get('ys')
                if int(page) <=0:
                    return redirect('/main/cls.html?page=1')
                else:
                    all_id = models.cls.objects.filter(id__gt=1).count()
                    if int(page)>int(all_id):
                        last_page = all_id // 10
                        if all_id%10:
                            last_page += 1
                            return redirect('/main/cls.html?page=%s'%last_page)
                        return redirect('/main/cls.html?page=%s'%last_page)
                    return redirect('/main/cls.html?page=%s'% page)
            if request.POST.get('ss'):
                msg = request.POST.get('ss')
                return redirect('http://127.0.0.1:8000/main/serch_cls/%s'%msg)
            else:
                obj = Form.StuForm()
                us_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')[0]['id']
                file_path ='/' +  models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
                last_id = models.cls.objects.filter(id__gt=1).count()
                page_info  = FY.Pageinfo(request.GET.get('page'),all_count=last_id,per_page=10,base_url='/main/cls.html')
                cls_list = models.cls.objects.all()[page_info.start():page_info.end()]
                msg = '搜索框不能为空'
                return render(request,'cls.html',{'cls_list':cls_list,'page_info':page_info,'file_path':file_path,'u_id':us_id,'obj':obj,'msg':msg})

def add_cls(request):
    ret = {'status':True,'msg':None}
    try:
        title = request.POST.get('name')
        models.cls.objects.create(title = title)
    except Exception as e:
        ret['status'] = False
        ret['msg'] = str(e)
    return HttpResponse(json.dumps(ret))

def del_cls(request):
    ret = {'status':True,'msg':None}
    try:
        c_id = request.POST.get('c_id')
        models.cls.objects.filter(id=c_id).delete()
    except Exception as e:
        ret['status'] = False
        ret['msg'] = str(e)
    return HttpResponse(json.dumps(ret))

def cls_serch(request,msg):
    us_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')[0]['id']
    file_path ='/' +  models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
    c_info = models.cls.objects.filter(title__contains=msg)
    return render(request,'serch_cls.html',{'file_path':file_path,'s_info':c_info,'u_id':us_id})

def edit_cls(request,c_id):
    if request.method == 'GET':
        cls_info = models.cls.objects.filter(id=c_id)
        for i in cls_info:
            c_info = i
        obj = Form.ClsForm(initial={'title':c_info.title})
        us_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')[0]['id']
        file_path ='/' +  models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
        return render(request,'edit_cls.html',{'file_path':file_path,'obj':obj,'sid':c_id,'u_id':us_id})
    else:
        obj = Form.ClsForm(request.POST)
        if obj.is_valid():
            models.cls.objects.filter(id=c_id).update(**obj.cleaned_data)
            return redirect('http://127.0.0.1:8000/main/cls.html?page=1')
        else:
            return render(request,'edit_cls.html',{'obj':obj})



def tea(request):
    if request.session.get('user'):
        if request.method == 'GET':
            last_id = models.teacher.objects.filter(id__gt=1).count()
            page_info  = FY.Pageinfo(request.GET.get('page'),all_count=last_id,per_page=10,base_url='/main/tea.html')
            us_id = str(models.Userinfo.objects.filter(user=request.session['user']).values('id')[0]['id'])
            file_path = '/' + models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
            obj = Form.TeaForm()
            tea_list = models.teacher.objects.all()
            return render(request,'tea.html',{'obj':obj,'file_path':file_path,'tea_list':tea_list,'u_id':us_id,'page_info':page_info})
        else:
            if request.POST.get('ss'):
                msg = request.POST.get('ss')
                return redirect('http://127.0.0.1:8000/main/serch_tea/%s'%msg)
            if request.POST.get('ys'):
                page = request.POST.get('ys')
                if int(page) <=0:
                    return redirect('/main/tea.html?page=1')
                else:
                    all_id = models.teacher.objects.filter(id__gt=1).count()
                    if int(page)>int(all_id):
                        last_page = all_id // 10
                        if all_id%10:
                            last_page += 1
                            return redirect('/main/tea.html?page=%s'%last_page)
                        return redirect('/main/tea.html?page=%s'%last_page)
                    return redirect('/main/tea.html?page=%s'% page)
            else:
                obj = Form.TeaForm()
                us_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')[0]['id']
                file_path ='/' +  models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
                last_id = models.teacher.objects.filter(id__gt=1).count()
                page_info  = FY.Pageinfo(request.GET.get('page'),all_count=last_id,per_page=10,base_url='/main/tea.html')
                cls_list = models.teacher.objects.all()[page_info.start():page_info.end()]
                print(cls_list)
                msg = '搜索框不能为空'
                return render(request,'tea.html',{'tea_list':cls_list,'page_info':page_info,'file_path':file_path,'u_id':us_id,'obj':obj,'msg':msg})

def edit_tea(request,tid):
    if request.method == 'GET':
        us_id = str(models.Userinfo.objects.filter(user=request.session['user']).values('id')[0]['id'])
        file_path = '/' + models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
        t_obj = models.teacher.objects.filter(id=tid).first()
        t2c = t_obj.cls_set.all()
        cls_list = models.cls.objects.all()
        cls_id = []
        for i in t2c:
            cls_id.append(i.id)
        obj = Form.TeaForm(initial={'name':t_obj.name,'age':t_obj.age,'sex':t_obj.sex})
        return render(request,'edit_tea.html',{'file_path':file_path,'u_id':us_id,'obj':obj,'tid':tid,'cls_list':cls_list,'t2c':t2c,'cls_id':cls_id})
    else:
        obj = Form.TeaForm(request.POST)
        if obj.is_valid():
            t_obj = models.teacher.objects.filter(id=tid).first()
            c_list = request.POST.getlist('select')
            t_info = models.teacher.objects.filter(name=obj.cleaned_data['name'])
            t2c = t_obj.cls_set.all()
            cls_id = []
            rmv_id = []
            for i in t2c:
                cls_id.append(str(i.id))
            print('原有cls_id',cls_id)
            print('现在提交c_list',c_list)
            for i in cls_id:
                if i not in c_list:
                    rmv_id.append(i)
                else:
                    continue
            for i in t_info:
                 i.cls_set.add(*c_list)
                 i.cls_set.remove(*rmv_id)
            models.teacher.objects.filter(id=tid).update(**obj.cleaned_data)
            return redirect('http://127.0.0.1:8000/main/tea.html')

def tea_serch(request,msg):
    us_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')[0]['id']
    t_info = models.teacher.objects.filter(name__contains=msg)
    for i in t_info:
        print(i.name)
    file_path ='/' +  models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
    return render(request,'serch_tea.html',{'file_path':file_path,'t_info':t_info,'u_id':us_id})\



def del_tea(request):
    ret = {'status':True,'msg':None}
    try:
        t_id = request.POST.get('t_id')
        print(t_id)
        models.teacher.objects.filter(id=t_id).delete()
    except Exception as e:
        ret['status'] = False
        ret['msg'] = str(e)
    return HttpResponse(json.dumps(ret))

def add_tea(request):
    ret = {'status':True,'msg':None}
    try:
        name = request.POST.get('name')
        age = request.POST.get('age')
        sex = request.POST.get('sex')
        models.teacher.objects.create(name=name,age=age,sex=sex)
    except Exception as e:
        ret['status'] = False
        ret['msg'] = str(e)
    return HttpResponse(json.dumps(ret))

