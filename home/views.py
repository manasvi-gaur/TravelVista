from django.shortcuts import render,HttpResponse
from home.models import Contact
from datetime import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    if(request.method == "POST"):
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        date = datetime.today()
        contact = Contact(name = name, email=email, phone=phone, desc= desc, date = date)
        contact.save()
        messages.success(request, "Profile details updated.")
    return render(request,"index.html")
    # return HttpResponse("hiiiiiii😁 I am Home Page ")

def about(request):
    return render(request,"about.html")
    # return HttpResponse("hiiiiiii😁 I am About Page ")

def explore(request):
    return render(request,"explore.html")
