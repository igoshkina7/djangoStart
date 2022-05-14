from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.job_home, name='job_home'),
    #path('<int:pk>', views.NewsDetailView.as_view(), name='job_detail')
    path('<int:pk>', views.job_detail, name="job_detail"),
    path('<int:pk>/like', views.like, name="like_j"),
    path('<int:pk>/unlike', views.unlike, name="unlike_j"),

]
