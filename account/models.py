from django.db import models
from django.utils.timezone import now
from news.models import Article
from job.models import Job
from django.contrib.auth.models import User
from django.urls import reverse
    

# Create your models here.
class Liked_post(models.Model):
    id_user = models.ForeignKey(User, related_name='id_user', on_delete=models.CASCADE)
    id_article = models.ForeignKey(Article, related_name='article', on_delete=models.CASCADE)

class Liked_job(models.Model):
    id_user = models.ForeignKey(User, related_name='id_user_job', on_delete=models.CASCADE)
    id_job = models.ForeignKey(Job, related_name='job', on_delete=models.CASCADE)

class LK(models.Model):
    lk_user = models.ForeignKey(User, related_name='lk_user', on_delete=models.CASCADE)
    name_lk=models.CharField(max_length=50)
    surname_lk=models.CharField(max_length=50)
    email_lk=models.EmailField()
    upload = models.FileField(upload_to ='uploads/')

    def __str__(self):
       return str(self.lk_user)
