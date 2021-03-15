from django.contrib import admin
from django.urls import path,re_path,include
from acount import views
urlpatterns = [
    re_path(r'^sigh_in.html$',views.sigh_in),
    re_path(r'^sigh_up.html$',views.sigh_up),
    re_path(r'^avata.html$',views.avata),
    re_path(r'^logout.html$',views.logout),
    re_path(r'^mine/(\d+).html$',views.mine)
]
