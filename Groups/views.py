from django.shortcuts import render
from Groups.forms import GroupForm
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
# Create your views here
def home(request):
    return render(request,'sociat/index.html')
@login_required
def Groups(request):
    logi=True
    if request.method=='post':
        form = GroupForm(request.post)
        grform=form.save()
        grform.save()
        ti= request.POST.get('Title', )
        print(ti)
        #form=get_user_model().objects.create_group(username)
        return HttpResponseRedirect('/group/')
    else:
        form=GroupForm()
        return render(request,'sociat/Group.html',{'logi':logi,'form':form})
