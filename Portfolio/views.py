from multiprocessing import context
from turtle import heading
from django.shortcuts import render
from Portfolio.models import Message

# Create your views here.


def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')


def Projects(request):
    return render(request, 'projects.html')


def ContactMe(request):
    if request.method == "POST":
        email = request.POST['email']
        fname = request.POST['fname']
        lname = request.POST['lname']
        pnumber = request.POST['pnumber']
        linkedin = request.POST['linkedinurl']
        subject = request.POST['sbjt']
        message = request.POST['msg']
        Data = Message(e_mail=email, first_name = fname, last_name = lname, phone_number = pnumber, liurl = linkedin,subject = subject, message = message)
        Data.save()
    return render(request, 'contact.html')
