from . import views
from django.urls import path
app_name='sociat'
urlpatterns=[
 path('', views.index, name='index'),
 path('register/',views.register,name='register'),
 path('login/',views.user_login,name='user_login'),
 path('logout/',views.user_logout,name='user_logout'),
 path('password_reset/',views.pass_resz,name='pass_resz'),
]
