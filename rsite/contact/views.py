from django.shortcuts import render , redirect
from django.core.mail import send_mail , BadHeaderError
from django.http import HttpResponse , HttpResponseRedirect
from django.conf import settings
# Create your views here.
from .forms import ContactForm

def send_email(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name     = form.cleaned_data['name']
            to_email = form.cleaned_data['email']
            message  = form.cleaned_data['message']

            try:
                subject        = f'welcome to our restaurant {name} '
                message        = f'Thank You For Contacting Us {name}\n Your response is been noted \n We will contact you shortly'
                email_from     = settings.EMAIL_HOST_USER
                recipient_list = [to_email]
                send_mail(subject,message,email_from,recipient_list)

            except BadHeaderError:
                return HttpResponse('invalid header')

            return redirect('contact:send_email')
    else:
        form = ContactForm()

    context = {
        'form' : form
    }

    return render(request, 'contact/contact.html', context)


def send_success(request):
        return render(request, 'contact/contact.html')
