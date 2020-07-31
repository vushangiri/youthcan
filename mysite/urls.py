
from django.urls import path, include
from . import views

app_name = 'mysite'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('subscribe', views.subscribe, name='subscribe')

]
