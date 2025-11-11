from django.shortcuts import render
from subscribe.models import Subscribe 
from subscribe.forms import Subscribeform
from django.shortcuts import redirect
from django.urls import reverse


# Create your views here.
def subscribe(request):
    email_error = ''
    subscribe_form = Subscribeform()
    if request.POST:
        subscribe_form = Subscribeform(request.POST)
        # print(request, ' ', email)
        if subscribe_form.is_valid():
            subscribe_form.save()
        #     email_error = 'no email entered'
        # # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
        # # subscribe.save()
        #     email = subscribe_form.cleaned_data['email']
        #     fname = subscribe_form.cleaned_data['first_name']
        #     lname = subscribe_form.cleaned_data['last_name']
        #     subscribe = Subscribe(first_name=fname, last_name=lname, email=email)
        #     subscribe.save()
            return redirect(reverse('thankyou'))
    context = {'form': subscribe_form, 'email_error': email_error}

    return render(request, 'subscribe/subscribe.html', context)


def thankyou(request):
    context = {}
    return render(request, 'subscribe/thankyou.html', context)