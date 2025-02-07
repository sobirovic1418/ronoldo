from django.urls import path
from .views import index, contact, salom, about

urlpatterns=[
    path('',index),
    path('contact/',contact),
    path('salom/',salom),
    path('about/',about)
]