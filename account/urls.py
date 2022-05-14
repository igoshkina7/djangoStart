from django.contrib import admin
from django.urls import path, include
from . import views
from .views import BlogUpdateView


urlpatterns = [
    path('liked', views.liked, name='liked'),
    path('liked/<int:pk>/edit', BlogUpdateView.as_view() , name='edit'),

]
