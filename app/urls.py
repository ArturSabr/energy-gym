from django.urls import  path
from .views import *

urlpatterns= [
    path('', Home.as_view(), name='home'),
    path('service/', Service.as_view(), name='service'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
]