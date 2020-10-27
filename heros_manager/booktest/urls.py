from django.urls import re_path
from booktest import views

urlpatterns = [
    re_path('^heros/$', views.show_heros.as_view()),
    re_path(r'^heros/(?P<id>\d+)/$', views.GetById.as_view())
]
