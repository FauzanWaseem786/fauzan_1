from django.db import models

# Create your models here.
class Group(models.Model):
    Title=models.CharField(max_length=264)
    body=models.TextField(null=True,blank=True)
    img=models.ImageField(null=True,blank=True)
    admins=models.CharField(max_length=264)
    #date=models.DateTimeField(default=datetime.now, blank=True)
