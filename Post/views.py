from django.shortcuts import render
from Post.forms import Post_form
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import Post

# Create your views here.
@login_required
def Posts(request):
    if request.method=='POST':
        postform = Post_form(request.POST,request.FILES)
        if postform.is_valid():
           post=postform.save()
           Title = request.POST.get('Title', '')
           img = request.POST.get('img', '')
           published_date= request.POST.get('published_date','')
        #post=Post.objects.create(Title=Title, img=img, published_date=published_date)
           post.save()
           return render(request,'sociat/posts.html',{'Title': Title,'img':img})
    else:
        postform=Post_form()
        return render(request,'sociat/crtpost.html',{'postform':postform})
def posts(request):
      pos=Post.objects.all()
      return render(request,'sociat/posts.html',{'pos':pos})
