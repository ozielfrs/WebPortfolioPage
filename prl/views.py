from django.shortcuts import redirect, render
from prl.models import Message

# Create your views here.


def data_validation(data: dict) -> bool:
    for item in data:
        if str(data[item]).isspace():
            if item != 'linkedin':
                return False
    return True


def Success(request):
    return render(request, 'success.html')


def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')


def Projects(request):
    return render(request, 'projects.html')


def ContactMe(request):
    if request.method == "POST":
        data = {
            'email': request.POST['email'],
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
            'pnumber': request.POST['pnumber'],
            'linkedin': request.POST['linkedinurl'],
            'subject': request.POST['sbjt'],
            'message': request.POST['msg'],
        }

        if data_validation(data):
            dataAsMessage = Message(
                e_mail=str(data['email']),
                first_name=data['fname'],
                last_name=data['lname'],
                phone_number=data['pnumber'],
                liurl=data['linkedin'],
                subject=data['subject'],
                message=data['message']
            )
            dataAsMessage.save()
            return redirect(Success)
            
        return redirect(ContactMe)

    return render(request, 'contact.html')
