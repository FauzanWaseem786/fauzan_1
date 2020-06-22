from . import views
from django.urls import path
app_name='Groups'
urlpatterns=[
path('',views.home,name='home'),
path('group/',views.Groups,name='Groups')
 ]
