
from django.shortcuts import render,HttpResponseRedirect
from .forms import Registration
from .models import Data
def add(request):
    if request.method =="POST":
        form=Registration(request.POST)
        if form.is_valid():
            rn=form.cleaned_data['rollno']
            nm=form.cleaned_data['name']
            mm=form.cleaned_data['middle']
            sm=form.cleaned_data['surname']
            mb=form.cleaned_data['mobileno']
            em=form.cleaned_data['email']
            ad=form.cleaned_data['address']
            pw=form.cleaned_data['password']
            qq=Data(rollno=rn,name=nm,middle=mm,surname=sm,mobileno=mb,email=em,address=ad,password=pw)
            qq.save()
            form=Registration()
    else:
        form=Registration()
    Students=Data.objects.all()
    return render(request,'add.html',{'form':form,'Students':Students})

def delete(request,id):
    if request.method == "POST":
        de=Data.objects.get(pk=id)
        de.delete()
        return HttpResponseRedirect('/')

def update(request,id):
    if request.method=="POST":
        up=Data.objects.get(pk=id)
        form=Registration(request.POST,instance=up)
        if form.is_valid():
            form.save()
    else:
        up=Data.objects.get(pk=id)    
        form=Registration(instance=up)    
    return render(request,'update.html',{'form':form})

def home(request):
    return render(request,'home.html')


def contact(request):
    return render(request,'contact.html')
         

def about(request):
    return render(request,'about.html')