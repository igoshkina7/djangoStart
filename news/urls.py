from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    #path('<int:pk>', views.NewsDetailView.as_view(), name='news_detail')
    path('<int:pk>', views.news_detail, name="news_detail"),
    path('<int:pk>/like', views.like, name="like"),
    path('<int:pk>/unlike', views.unlike, name="unlike"),


]

