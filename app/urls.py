from django.urls import path
# current directory
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^signin/$', views.signin, name="signin"),
    url(r'^inbox/', views.inbox, name="inbox"),
    path(r'^<id>/message_view/', views.message_view, name="message_view"),
    path(r'^<id>/message_view2/', views.message_view2, name="message_view2"),
    url(r'^sent/', views.sent, name="sent"),
    url(r'^compose/', views.compose, name="compose"),
    url(r'^logout/', views.logout, name="logout"),

]