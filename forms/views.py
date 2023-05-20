from django.shortcuts import render
from .models import *
from django.contrib import messages
from datetime import datetime

# Create your views here.
def index(request):
    banner = Banner.objects.all()
    cntx={
        'banner':banner[0]
    }
    return render(request, "index.html",cntx)

def about(request):
    
    return render(request, "about.html")

def schedule(request):
    
    return render(request, "schedule.html")

def gallery(request):
    
    return render(request, "gallery.html")

def instruction(request):
    
    return render(request, "instruction.html")

def team(request):
    
    return render(request, "team.html")
   
# def blog(request):
    
#     return render(request, "blog.html")

# def blog_details(request):
    
#     return render(request, "blog_details.html")


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST["message"]
        # subject = request.POST["subject"]
        
        contact = Contact(name=name, email= email, message= message, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent.')

    return render(request, "contact.html")

# def enquiry(request):
#     if request.method == "POST":
#         name = request.POST['name']
#         email = request.POST['email']
#         phone = request.POST["phone"]
#         description = request.POST["description"]
        
#         enquiry = Enquiry(name=name, email= email, phone= phone,description=description, date= datetime.today())
#         enquiry.save()
#         messages.success(request, 'Your message has been sent.')

#     return render(request, "enquiry.html")

def dietenquiry(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST["phone"]
        age = request.POST["age"]
        height = request.POST["height"]
        weight = request.POST["weight"]
        reason = request.POST["reason"]
        goal = request.POST["goal"]
        
        dietenquiry = Dietenquiry(name=name, email= email, phone= phone,age= age,height= height,weight= weight,reason= reason,goal=goal, date= datetime.today())
        dietenquiry.save()
        messages.success(request, 'Your message has been sent.')

    return render(request, "components/modules/home/home-diet.html")