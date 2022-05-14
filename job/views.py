from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DeleteView

from .models import Job, Comment_job
from .forms import CommentForm,JobFilterForm,JobFilterFormGr,JobFilterFormZan,JobFilterFormFind
from main.forms import Find
from account.models import Liked_job
from django.db.models import Q
from django.http import HttpResponseRedirect
from account.models import LK
from django.core.mail import EmailMessage
from django.shortcuts import render, HttpResponse, HttpResponseRedirect


# Create your views here.



class NewsDetailView(DeleteView):
    model = Job
    template_name = 'job/detail_view.html'
    context_object_name = 'job'


def job_detail(request, pk):
    form = CommentForm()
    job = get_object_or_404(Job, id=pk)
    comments = Comment_job.objects.filter(post=pk)
    lk=LK.objects.get(lk_user=request.user)
    if request.method == 'POST':
        f = CommentForm(request.POST)
        if f.is_valid():
            comm = f.save(commit=False)
            comm.post = job
            comm.name=request.user
            comm.save()
        
    return render(request, 'job/detail_view.html', {'job': job, 'comments': comments, 'form': form, 'lk': lk})

def like(request, pk):
    print('like')
    job = get_object_or_404(Job, id=pk)
    print(Liked_job(id_user=request.user, id_job=job))
    if Liked_job.objects.filter(id_user=request.user, id_job=job).count() == 0:
        l = Liked_job(id_user=request.user, id_job=job)
        l.save()
    
    return redirect('/account/liked')

def unlike(request, pk):
    job = get_object_or_404(Job, id=pk)
    
    Liked_job.objects.filter(id_user=request.user, id_job=job).delete()
    
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def job_home(request):
    jobs = Job.objects.all()
    jobs=jobs.filter(fac=2)
    form=JobFilterForm(request.GET)
    form1=JobFilterFormGr(request.GET)
    form2=JobFilterFormZan(request.GET)
    form3=JobFilterFormFind(request.GET)
    form4=Find(request.GET)
    if form3.is_valid():
        if form3.cleaned_data["find"]:
            jobs=jobs.filter(Q(title__icontains=form3.cleaned_data["find"])|Q(specialty__icontains=form3.cleaned_data["find"]))
    if form.is_valid():
        if form.cleaned_data["min_price"]:
            jobs=jobs.filter(salary__gte=form.cleaned_data["min_price"])
        if form.cleaned_data["max_price"]:
            jobs=jobs.filter(salary__lte=form.cleaned_data["max_price"])
    if form1.is_valid():
        if form1.cleaned_data["gr_gib"] and form1.cleaned_data["gr_52"] and form1.cleaned_data["gr_22"]:
            jobs=jobs.filter(Q(work_graph__icontains="Гибкий")|Q(work_graph__icontains="5/2")|Q(work_graph__icontains="2/2"))
        elif form1.cleaned_data["gr_gib"] and form1.cleaned_data["gr_52"]:
            jobs=jobs.filter(Q(work_graph__icontains="5/2")|Q(work_graph__icontains="Гибкий"))
        elif form1.cleaned_data["gr_gib"] and form1.cleaned_data["gr_22"]:
            jobs=jobs.filter(Q(work_graph__icontains="2/2")|Q(work_graph__icontains="Гибкий"))
        elif form1.cleaned_data["gr_52"] and form1.cleaned_data["gr_22"]:
            jobs=jobs.filter(Q(work_graph__icontains="2/2")|Q(work_graph__icontains="5/2"))
        elif form1.cleaned_data["gr_gib"]:
            jobs=jobs.filter(work_graph__icontains="Гибкий")
        elif form1.cleaned_data["gr_52"]:
            jobs=jobs.filter(work_graph__icontains="5/2")
        elif form1.cleaned_data["gr_22"]:
            jobs=jobs.filter(work_graph__icontains="2/2")
    if form2.is_valid():
        if form2.cleaned_data["full"] and form2.cleaned_data["notfull"]:
            jobs=jobs.filter(Q(full_part_time=True)|Q(full_part_time=False))
        elif form2.cleaned_data["full"]:
            jobs=jobs.filter(full_part_time=True)
        elif form2.cleaned_data["notfull"]:
            jobs=jobs.filter(full_part_time=False)
    
    return render(request, 'job/job_home.html', {'jobs': jobs,"form":form,"form1":form1,"form2":form2,"form3":form3,"form4":form4})

