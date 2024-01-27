from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Membernew
from django.views.decorators.csrf import csrf_exempt
from.forms import MemberForm

# Create your views here.
# def hello(reuest):
#     return HttpResponse("hello world")
def main(request):
    member_list= Membernew.objects.all().values()
    context ={
        'member_list':member_list
    }
    template = loader.get_template('main.html')
    return HttpResponse(template.render(context,request))

def hello(request,id):
    mymember = Membernew.objects.get(id=id)
    template = loader.get_template('hello.html')
    context ={
        'mymember':mymember
    }
    return HttpResponse(template.render(context,request))

def contact(request):
    t1 = loader.get_template('contact.html')
    return HttpResponse(t1.render())

def image(request):
    t1 = loader.get_template('image.html')
    return HttpResponse(t1.render())

def newmember(request):
    t1 = loader.get_template('newmember.html')
    return HttpResponse(t1.render())

def form(request):
    t1 = loader.get_template('form.html')
    return HttpResponse(t1.render())

@csrf_exempt
def addnewmember(request):
    if request.method =='POST':
        firstname =request.POST.get('firstname',)
        lastname =request.POST.get('lastname',)
        phoneno =request.POST.get('phoneno',)
        rollno =request.POST.get('rollno',)
        image=request.FILES['image']
        membernew=Membernew(firstname=firstname,lastname=lastname,phoneno=phoneno,rollno=rollno)
        membernew.save()
    t1=loader.get_template('addnewmember.html')
    return HttpResponse(t1.render())

def update(request,id):
    membernew=Membernew.objects.get(id=id)
    form=MemberForm(request.POST,instance=membernew)
    if form.is_valid():
        form.save()
        t1=loader.get_template('addnewmember.html')
        return HttpResponse(t1.render())
    return render(request,'update.html',{'form':form,'membernew':membernew})

@csrf_exempt
def delete(request,id):
    if request.method =='POST':
     membernew =Membernew.objects.get(id=id)
     membernew.delete()
     t1=loader.get_template('main.html')
     return HttpResponse(t1.render())
    return render(request,'delete.html')
























# def main(request):
#     template = loader.get_template('main.html')
#     return HttpResponse(template.render())
def prachi(request):
    template = loader.get_template('prachi.html')
    return HttpResponse(template.render())