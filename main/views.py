from re import template
from django.shortcuts import redirect, render
from job.models import Job
from news.models import Article
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import  AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from .forms import Find
from django.db.models import Q



def index(request):
    data = {
        'title': 'Главная страница'
    }
    news = Article.objects.all()[:5]
    jobs = Job.objects.all().order_by('-id')[:5]
    form4=Find(request.GET)
    return render(request, 'main/index.html', {'news': news, 'jobs':jobs,'form4':form4})

def find(request):
    news = Article.objects.all()
    jobs = Job.objects.all()
    jobs=jobs.filter(fac=2)
    form4=Find(request.GET)
    form5=Find(request.GET)
    if form5.is_valid():
        if form5.cleaned_data["find"]:
            jobs=jobs.filter(Q(title__icontains=form5.cleaned_data["find"])|Q(specialty__icontains=form5.cleaned_data["find"])|Q(work_graph__icontains=form5.cleaned_data["find"])|Q(company__icontains=form5.cleaned_data["find"])|Q(anons__icontains=form5.cleaned_data["find"])|Q(full_text__icontains=form5.cleaned_data["find"]))
            news=news.filter(Q(title__icontains=form5.cleaned_data["find"])|Q(anons__icontains=form5.cleaned_data["find"])|Q(full_text__icontains=form5.cleaned_data["find"]))
    return render(request, 'main/find.html', {'news': news, 'jobs':jobs,'form4':form4,'form5':form5})

def about(request):
    form4=Find(request.GET)
    return render(request, 'main/about.html',{'form4':form4})


class RegisterUser(CreateView):
    form_class = UserCreationForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('login')
    

def logout_user(request):
    logout(request)
    return redirect('login')

class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'
    def get_success_url(self):
        return reverse_lazy('home')
