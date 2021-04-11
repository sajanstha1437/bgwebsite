from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('index.html', views.index),
    path('intro.html', views.intro),
    path('message.html', views.message),
    path('contact.html', views.contact)
]

