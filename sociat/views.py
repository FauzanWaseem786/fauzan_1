from django.shortcuts import render
from sociat.forms import Reg_form,pro_form,passw
from sociat.models import Register,profile
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
def index(request):
    return render(request,'sociat/index.html')
def register(request):
    #login=False
    registered = False
    if request.method == 'POST':
        user_form = Reg_form(request.POST)
        profile_form = pro_form(request.POST,request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            username = request.POST.get('username', '')
            password = request.POST.get('password', '')
            email = request.POST.get('email', '')
            user.save()
            profil = profile_form.save()
            profil.save()
            user = authenticate(request, username=username, password=password)
            # if user account do not exist.
            if user is None:
                # create user account and return the user object.
                user = get_user_model().objects.create_user(username=username, password=password, email=email)
                registered = True
                user.save()

        else:
            print("user_form.errors")
    else:
        user_form = Reg_form()
        profile_form=pro_form()
    return render(request,'sociat/registration.html',
                           { 'pro_form':profile_form,
                          'user_form':user_form,
                           'registered':registered})
def user_login(request):
    if request.method == 'POST':
         username = request.POST.get('username','')
         password = request.POST.get('password', '')
         print(username,password)
         user=authenticate(username=username,password=password)
         if user:
            if user.is_active:
                logi=True
                login(request,user)
                #return HttpResponseRedirect(reverse('index'))
                return render(request,'sociat/index.html',{'logi':logi})
            else:
                return HttpResponse("Your account was inactive.")
         else:
            print("Someone tried to login and failed.")
            print("their credentials were username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'sociat/login.html', {})
@login_required
def user_logout(request):
    logout(request)
    return render(request,'sociat/blog.html')
def pass_resz(request):
    dest=list(Register.objects.all())
    return render(request,'sociat/pass.html',{'dest':dest})
