from .forms import ContactForm
from .models import Contact, Newsletter, Team, Events, Eventsgallery, Whoarewe, Whatwedo, About, Values, Partners, Whoareweimage, Home, Advisors
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from validate_email import validate_email

# Create your views here.
def program(request):
    data = request.GET['data']
    one_event = Events.objects.get(id=data)
    one_event_image = Eventsgallery.objects.filter(events_id=one_event.id)
    context = {
        'one_event': one_event,
        'one_event_image': one_event_image
    }
    return render(request, 'program.html', context)

def events(request):
    data = Eventsgallery.objects.all()
    events = Events.objects.all()
    context = {
        'photos': data,
        'events': events
    }
    return render(request, 'events.html', context)

def index(request):
    teams = Team.objects.all()
    home = Home.objects.get(active=True)
    body_one = Whoarewe.objects.get(active=True)
    body_image = Whoareweimage.objects.filter(events_id=body_one.id)
    body_image_count = Whoareweimage.objects.filter(events_id=body_one.id).count()
    body_values = Values.objects.get(active=True)
    events = Events.objects.all()
    advisors = Advisors.objects.all()
    partners = Partners.objects.all()
    context = {
        'teams': teams,
        'home': home,
        'body_one': body_one,
        'body_image': body_image,
        'body_values': body_values,
        'body_image_count': body_image_count,
        'events': events,
        'advisors': advisors,
        'partners': partners
    }
    return render(request, 'index.html', context)

def about(request):
    advisors = Advisors.objects.all()
    body_values = Values.objects.get(active=True)
    teams = Team.objects.all()
    context = {
        'advisors': advisors,
        'body_values': body_values,
        'teams': teams
    }
    return render(request, 'about.html', context)

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