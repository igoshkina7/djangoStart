from tkinter import CASCADE
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

# Create your models here.
class Facultet(models.Model):
    facult=models.CharField('Факультет', max_length=50, default='')

    def __str__(self):
        return self.facult

class Job(models.Model):
    fac=models.ForeignKey(Facultet, related_name="fac_FK", on_delete=models.CASCADE)
    title = models.CharField('Название', max_length=50, default='')
    specialty = models.CharField('Специализация', max_length=50, default='')
    salary = models.IntegerField('Зарплата', default=0)
    full_part_time = models.BooleanField('Занятость', default=False)
    work_graph = models.CharField('График работы', max_length=20, default='')
    company = models.CharField('Название компании', max_length=50, default='')
    post_date = models.DateTimeField(default=now)
    score = models.BigIntegerField(default=0)
    number_of_ratings = models.BigIntegerField(default=0)
    anons = models.CharField('Анонс', max_length=250)
    full_text = models.TextField('Статья')
    email_company=models.EmailField('Email')

    def __str__(self):
        return self.title

class Comment_job(models.Model):
    post = models.ForeignKey(Job, related_name='comments', on_delete=models.CASCADE)
    name = models.TextField()
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)
