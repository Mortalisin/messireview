from unicodedata import name
from urllib import response
from django.shortcuts import render,HttpResponse
from datetime import datetime
from messireview.models import Contact
from messireview.models import Contact
import requests
API_KEY='52A7DC0D4AB1402B9A1AE358433137AE'


# Create your views here.
def index(request):
    url=f'https://api.rainforestapi.com/request?api_key={API_KEY}&type=product&amazon_domain=amazon.com&asin=B073JYC4XM'
    response=requests.get(url)
    data=response.json()
    print(data)
    context ={
        'data':'data',
        'variable1':"ye variable sent kiya hu",
        "abhi":"ye v variable hai",
        'link':'http://127.0.0.1:8000/rating'
    }
    return render(request,'index.html',context,)

    #context is a set of variable jise hamne vejte hi apne templates pe,like here i send it to index.html file which is in templates folder andd remeber dont forget to return context 
    #return HttpResponse("This is messireview pageok")

def about(request):
    return render(request,'about.html')
    #return HttpResponse("This is messireview about pageok")

def services(request):

    return render(request,'services.html')
    return HttpResponse("This is messireview  hfbjfbjjh services pageok")

def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        address=request.POST.get('address')
        reason=request.POST.get('reason')

        contact= Contact (name=name,email=email,address=address,reason=reason,   date=datetime.today())
        contact.save()

    
    
    return render(request,'contact.html')
    #return HttpResponse("This is messireview contact pageok")

def rating(request):
    return render (request,'rating.html')


