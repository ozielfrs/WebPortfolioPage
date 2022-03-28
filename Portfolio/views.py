from django.shortcuts import redirect, render
from portfolio.models import Message

# Create your views here.
lastRequest = ""
newRequest = ""
context = {
    'Name': " Example"
}


def should_render_success(request, lrequest):
    if lrequest == "POST/contact" and request == "GET/contact":
        return True
    return False


def form_validation(form: dict) -> bool:
    for item in form:
        if str(form[item]).isspace():
            if item != 'linkedin':
                return False
    return True


def Home(request):
    return render(request, 'home.html')


def About(request):
    return render(request, 'about.html')


def Projects(request):
    return render(request, 'projects.html')


def ContactMe(request):
    global lastRequest, newRequest
    newRequest = request.method + request.path

    if should_render_success(newRequest, lastRequest):
        lastRequest = request.method + request.path
        return render(request, 'success.html', context)

    if request.method == "POST":
        form = {
            'email': request.POST['email'],
            'fname': request.POST['fname'],
            'lname': request.POST['lname'],
            'pnumber': request.POST['pnumber'],
            'linkedin': request.POST['linkedinurl'],
            'subject': request.POST['sbjt'],
            'message': request.POST['msg'],
        }

        lastRequest = request.method + request.path
        context['Name'] = " " + form['fname']

        if form_validation(form):
            Data = Message(
                e_mail=str(form['email']),
                first_name=form['fname'],
                last_name=form['lname'],
                phone_number=form['pnumber'],
                liurl=form['linkedin'],
                subject=form['subject'],
                message=form['message']
            )
            Data.save()
            return redirect(ContactMe)

    lastRequest = request.method + request.path
    return render(request, 'contact.html')
