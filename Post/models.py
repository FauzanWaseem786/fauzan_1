from django.db import models

# Create your models here.
class Post(models.Model):
      Title=models.CharField(max_length=264)
      img = models.ImageField(null=True,blank=True)
      published_date = models.DateTimeField(auto_now=False, auto_now_add=True)
