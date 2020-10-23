from django.urls import re_path
from web_01 import views

urlpatterns = [
    re_path(r'^register/$', views.register),
    # re_path(r'^login/$', views.login),
    # 类视图URL地址配置
    re_path(r'^login/$', views.LoginView.as_view()),
]