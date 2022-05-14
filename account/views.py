from curses.textpad import Textbox
from tkinter import Text
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Liked_post, Liked_job,LK
from main.forms import Find
from django.views.generic import DeleteView
from django.forms import Textarea
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import  UpdateView
# Create your views here.


@login_required
def liked(request):
    like_a = Liked_post.objects.filter(id_user=request.user)
    like_j = Liked_job.objects.filter(id_user=request.user)
    if LK.objects.filter(lk_user=request.user).count()==1:
        information=LK.objects.get(lk_user=request.user)
    else:
        information=LK.objects.create(lk_user=request.user, name_lk='', surname_lk='', email_lk='')
    form4=Find(request.GET)
    return render(request, 'account/home.html', {'information': information,'article': like_a, 'job': like_j,"form4":form4})

class BlogUpdateView(UpdateView): # Новый класс
    model = LK
    template_name = 'account/edit.html'
    fields = ['name_lk', 'surname_lk', 'email_lk']  
    success_url = reverse_lazy('liked')

    widgets={
            "surname_lk": Textarea(attrs={
                'class': 'form-control',
                'label': 'Комментарий',
                'style': 'height:15vh; margin-top:1vw;  width: 40vw;'
            })
        }
