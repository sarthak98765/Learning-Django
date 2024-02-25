from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def home(request):
    peoples=[
        {'name':"rohit","age":23},
        {'name':"Akash","age":19},
        {"name":"Rahul","age":26}
    ]
    return render(request,'index.html',context={'peoples':peoples})

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')
