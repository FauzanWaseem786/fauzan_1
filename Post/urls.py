from . import views
from django.urls import path
app_name='Post'
urlpatterns=[
path('posts/',views.Posts,name='Posts'),
path('post/',views.posts,name='posts')

]
