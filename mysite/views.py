from .forms import ContactForm, ApplyForm
from .models import Contact, Newsletter, Team, Events, Eventsgallery, Whoarewe, About, Values, Partners, Whoareweimage, Home, Advisors, Admin, HomeTitles, AboutGallery
from datetime import datetime, date
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import random
from validate_email import validate_email

# Create your views here.

def program(request):
    data = request.GET['data']
    one_event = Events.objects.get(id=data)
    one_event_image = Eventsgallery.objects.filter(events_id=one_event.id)
    one_event_image_count = Eventsgallery.objects.filter(events_id=one_event.id).count()
    nextdata = Events.objects.filter(id__gt=one_event.id).order_by('id').first()
    prevdata = Events.objects.filter(id__lt=one_event.id).order_by('id').last()

 
    context = {
        'one_event': one_event,
        'one_event_image': one_event_image,
        'one_event_range': range(one_event_image_count),
        'prevdata': prevdata,
        'nextdata': nextdata
    }
    return render(request, 'program.html', context)

def affiliates(request):
    advisors = Advisors.objects.all()
    teams = Team.objects.all()
    partners = Partners.objects.all()
    pg = request.GET.get('page', 1)
    p = Paginator(partners, 20)
    page = p.page(pg)
    context = {
        'advisors': advisors,
        'teams': teams,
        'partners': partners,
        'page': page
    }
    return render(request, 'affiliates.html', context)

def events(request):
    titles = HomeTitles.objects.get(active=True)

    
    events = Events.objects.order_by('-organized_at')
    pg = request.GET.get('page', 1)
    p = Paginator(events, 3)
    print(pg)
    page = p.page(pg)
    items = sorted(Eventsgallery.objects.all().order_by('?')[:10], key=lambda x: random.random())
    imgs = Eventsgallery.objects.all()
    my_list = list(imgs)

    i = Paginator(items, 10)
    
    context = {
        'photos': i.page(1),
        'events': events,
        'titles': titles,
        'page': page
    }
    return render(request, 'events.html', context)

def index(request):
    titles = HomeTitles.objects.get(active=True)
    teams = Team.objects.all()
    data = Admin.objects.get(active=True)
    home = Home.objects.get(active=True)
    body_one = Whoarewe.objects.get(active=True)
    body_image = Whoareweimage.objects.filter(events_id=body_one.id)
    body_image_count = Whoareweimage.objects.filter(events_id=body_one.id).count()
    body_values = Values.objects.get(active=True)
    events = Events.objects.order_by("-organized_at")
    advisors = Advisors.objects.all()
    partners = Partners.objects.all()
    upcoming_event = Events.objects.filter(upcoming=True)
    p = Paginator(upcoming_event, 3)
    page1 = p.page(1)
    event_paginator = Paginator(events, 6)
    pg1 = event_paginator.page(1)
    context = {
        'teams': teams,
        'home': home,
        'body_one': body_one,
        'body_image': body_image,
        'body_values': body_values,
        'body_range': range(body_image_count),
        'events': pg1.object_list,
        'advisors': advisors,
        'partners': partners,
        'data': data,
        'titles': titles,
        'recent_post': page1.object_list
    }
    return render(request, 'index.html', context)

def about(request):
    titles = HomeTitles.objects.get(active=True)

    advisors = Advisors.objects.all()
    body_values = Values.objects.get(active=True)
    about = About.objects.get(active=True)
    gallery = AboutGallery.objects.filter(data_id=about.id)
    teams = Team.objects.all()
    partners = Partners.objects.all()
    upcoming_event = Events.objects.filter(upcoming=True)
    p = Paginator(upcoming_event, 6)
    page1 = p.page(1)
    context = {
        'advisors': advisors,
        'body_values': body_values,
        'teams': teams,
        'partners': partners,
        'titles': titles,
        'about': about,
        'gallery': gallery,
        'upcoming': page1.object_list
    }
    return render(request, 'about.html', context)

@csrf_exempt  
def joinus(request):
    form = ApplyForm()
    if request.method == 'POST':
        form = ApplyForm(request.POST, request.FILES)
        if form.is_valid():
            email = form.cleaned_data['email']
            form.save()
            resp = {
                'result': 'ok'
            }
            subject = 'Join Youthcan'
            message = 'Congratulations, your resume has been updated successfully sent. We shall review your application and contact you in the provided email address or phone number'
            from_email = 'prabinoiid@gmail.com'
            recipient_list = [email]
            fail_silently = False
            send_mail(subject, message, from_email, recipient_list, fail_silently)
            return JsonResponse(resp)
        else:
            resp = {
                'result': 'FRM-INV'
            }
            return JsonResponse(resp)


def contact(request):
    data = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
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
        admindata = Admin.objects.get(active=True)
        data = ContactForm()
        context = {
            'form': data,
            'data': admindata
        }
        return render(request, 'contact.html', context)

@csrf_exempt  
def subscribe(request):
    if request.method == 'POST':
        if request.is_ajax():
            email = request.POST['email']
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