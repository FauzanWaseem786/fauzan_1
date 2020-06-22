from django.db import models
#from django.contrib.auth.models import User
# Create your models here
class Register(models.Model):
      username=models.CharField(max_length=264)
      email=models.EmailField()
     # password=models.CharField(max_length=264)
      def __str__(self):
            return self.username
class profile(models.Model):
      profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
class set_passwor(models.Model):
    password=models.CharField(max_length=10)
