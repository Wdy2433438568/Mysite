from django.shortcuts import render,HttpResponse,redirect
from acount import Form
from acount import models
from django.forms import forms
from django.views.decorators.clickjacking import xframe_options_exempt
import os
def sigh_up(request):
    if request.method == 'GET':
        obj = Form.SighupForm()
        return render(request,'sigh_up.html',{'obj':obj})
    else:
        obj = Form.SighupForm(request.POST)
        if obj.is_valid():
            if models.Userinfo.objects.filter(pwd = obj.cleaned_data['pwd'],user=obj.cleaned_data['user']):
                request.session['user'] = obj.cleaned_data['user']
                return redirect('/index.html')
        return render(request,'sigh_up.html',{'obj':obj})

@xframe_options_exempt
def sigh_in(request):
    if request.method == 'GET':
        obj = Form.SighForm()
        return render(request,'sigh_in.html',{'obj':obj})
    else:
        obj = Form.SighForm(request.POST)
        if obj.is_valid():
            models.Userinfo.objects.create(**obj.cleaned_data)
            request.session['user'] = obj.cleaned_data['user']
            return redirect('/acount/avata.html')

        return render(request,'sigh_in.html',{'obj':obj})

def avata(request):
    if request.method == 'GET':
        if models.Userinfo.objects.filter(user=request.session.get('user')).count():
            return render(request,'avata.html')
        else:
            return redirect('/acount/sigh_in.html')
    else:
        file_obj = request.FILES.get('upload')
        obj_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')
        us_id = obj_id[0]['id']
        file_path = os.path.join("static/img",file_obj.name)
        models.UserAva.objects.create(img_path=file_path,u_id=str(us_id))
        with open(file_path,'wb') as f:
            for chunk in file_obj.chunks():
                f.write(chunk)
            f.close()
        return HttpResponse(file_path)

def logout(request):
     del request.session['user']
     return redirect('/acount/sigh_up.html')


def mine(request,nid):
    us_id = nid
    user = models.Userinfo.objects.filter(id=us_id).values('user')[0]['user']
    if request.session['user'] == user:
        if request.method == 'GET':
            file_path ='/' + models.UserAva.objects.filter(u_id=us_id).values('img_path')[0]['img_path']
            db_obj = models.Userinfo.objects.filter(id=us_id).first()
            obj = Form.CsighForm(initial={'user':db_obj.user,'email':db_obj.email,'sex':db_obj.sex,'age':db_obj.age,'pwd':db_obj.pwd})
            return render(request,'mine.html',{'file_path':file_path,'obj':obj,'nid':nid,'db_obj':db_obj})
        else:
            obj = Form.CsighForm(request.POST)
            if request.FILES.get('upload'):
                file_obj = request.FILES.get('upload')
                obj_id = models.Userinfo.objects.filter(user=request.session.get('user')).values('id')
                us_id = obj_id[0]['id']
                file_path = os.path.join("static/img",file_obj.name)
                models.UserAva.objects.filter(u_id=us_id).update(img_path=file_path)
                with open(file_path,'wb') as f:
                    for chunk in file_obj.chunks():
                        f.write(chunk)
                    f.close()
                return HttpResponse(file_path)
            if obj.is_valid():
                request.session['user'] = obj.cleaned_data['user']
                models.Userinfo.objects.filter(id=us_id).update(**obj.cleaned_data)
                return redirect('/index.html')
            else:
                return render(request,'mine.html',{'obj':obj})
    return redirect('/acount/sigh_up.html')