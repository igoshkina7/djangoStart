from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DeleteView
from django.contrib import messages
from .models import Article, Comment
from .forms import CommentForm
from django.contrib.auth.models import User
from account.models import Liked_post
from django.urls import reverse_lazy
from .forms import ArticleFilterForm
from main.forms import Find



# Create your views here.


def news_home(request):
    news = Article.objects.all()
    form=ArticleFilterForm(request.GET)
    form4=Find(request.GET)
    if form.is_valid():
        if form.cleaned_data["find"]:
            news=news.filter(full_text__icontains=form.cleaned_data["find"])
    return render(request, 'news/news_home.html', {'news': news, "form":form,"form4":form4})


'''class NewsDetailView(DeleteView):
    model = Article
    template_name = 'news/detail_view.html'
    context_object_name = 'article'''
 

def news_detail(request, pk):
    form = CommentForm()
    news = get_object_or_404(Article, id=pk)
    comments = Comment.objects.filter(post=pk)
    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            comm = f.save(commit=False)
            comm.post = news
            comm.name=request.user
            comm.email=request.user.email
            comm.save()
    return render(request, 'news/detail_view.html', {'article': news, 'comments': comments, 'form': form, 'like': like})

def like(request, pk):
    news = get_object_or_404(Article, id=pk)
    if Liked_post.objects.filter(id_user=request.user, id_article=news).count() == 0:
        l = Liked_post(id_user=request.user, id_article=news)
        l.save()
    
    return redirect('home')

def unlike(request, pk):
    news = get_object_or_404(Article, id=pk)
    
    Liked_post.objects.filter(id_user=request.user, id_article=news).delete()
    
    return redirect('home')