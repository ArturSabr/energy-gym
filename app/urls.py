from django.urls import path, include
from django.conf.urls.static import static
from .views import *
from django.conf import settings


urlpatterns= [
    path('', Home.as_view(), name='home'),
    path('service/', Service.as_view(), name='service'),
    path('about/', About.as_view(), name='about'),
    path('contact/', Contact.as_view(), name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
