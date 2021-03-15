from django.contrib import admin
from django.urls import path,re_path,include
from main import views

urlpatterns = [
    re_path(r'^stu.html',views.stu),
    re_path(r'^tea.html',views.tea),
    re_path(r'^cls.html',views.cls),
    re_path(r'^(\d+)/edit.html',views.edit_s),
    re_path(r'^(\d+)/edit_cls.html',views.edit_cls),
    re_path(r'^(\d+)/edit_tea.html',views.edit_tea),
    re_path(r'^del.html',views.delete),
    re_path(r'^add.html',views.add),
    re_path(r'^serch/(.*)$',views.serch),
    re_path(r'^add_cls.html',views.add_cls),
    re_path(r'^add_tea.html',views.add_tea),
    re_path(r'^del_cls.html',views.del_cls),
    re_path(r'^del_tea.html',views.del_tea),
    re_path(r'^serch_cls/(.*)$',views.cls_serch),
    re_path(r'^serch_tea/(.*)$',views.tea_serch),
]