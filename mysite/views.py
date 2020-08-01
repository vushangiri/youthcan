from .forms import ContactForm
from .models import Contact, Newsletter, Team
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from validate_email import validate_email

# Create your views here.
def index(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    data = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            info = Contact.objects.create(name=name, email=email, subject=subject, message=message)
            info.save()
            resp = {
                'sent': 'saved'
            }
            return JsonResponse(resp)
        else:
            resp = {
                'sent': 'error'
            }
            return JsonResponse(resp)
    else:
        data = ContactForm()
        context = {
            'form': data
        }
        return render(request, 'contact.html', context)

@csrf_exempt  
def subscribe(request):
    if request.method == 'POST':
        if request.is_ajax():
            email = request.POST['result']
            is_valid = validate_email(email)
            if is_valid:

                info = Newsletter.objects.create(email=email)
                info.save()
                
                resp = {
                    'result': 'ok'
                }
                return JsonResponse(resp)
                
                    
            else:
                
                resp = {
                    'result': 'error'
                }
                return JsonResponse(resp)
        else:
            email = request.POST['email']
            is_valid = validate_email(email)
            if is_valid:
                info = Newsletter.objects.create(email=email)
                info.save()
                messages.info(request, 'Subcribed Successfully')
                return redirect('/')
            else:
                messages.info(request, 'Please enter a valid email')
                return redirect('/')