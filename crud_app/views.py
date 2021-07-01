from django.shortcuts import render,HttpResponseRedirect
from .forms import registeruser
from .models import user   
from django.core.mail import send_mail 
from django.conf import settings
from django.contrib import messages
# Create your views here.
#this function will take the input from user and save it into database and it will show tha all users input and it will also send the auto genrated mail to the user  
def addandshow(request):
    if request.method == 'POST':
        fm= registeruser(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data['name']
            em=fm.cleaned_data['email']
            ps=fm.cleaned_data['password']
            # ag=fm.cleaned_data['age']
            reg=user(name=nm,email=em,password=ps)
            reg.save()
            fm= registeruser()
            send_mail(
        'test',
        'this msg is for testing purpose.this is auto genrated mail plz dont reply to this msg ',
        settings.EMAIL_HOST_USER,
        [em],
        fail_silently=False,)   
        messages.add_message(request, messages.INFO, 'mail hase been sent')
    else:
        fm = registeruser()
    stud=user.objects.all()
    return render(request,'addandshow.html',{'form':fm,'st':stud})
# this function will update and edit
def update(request,id):
    if request.method =='POST':
        pi=user.objects.get(pk=id)
        fm= registeruser(request.POST,instance=pi)
        if fm.is_valid():
            fm.save()
    else:
        pi=user.objects.get(pk=id)
        fm= registeruser(instance=pi)
    return render(request, 'update.html',{'form':fm})
# this function is used to delete the pertcular data or user.
def delete_user(request,id):
    if request.method =='POST':
        pi=user.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/')