from django.urls import path

from blog.views import index, index_2

urlpatterns=[
    path('',index),
    path('index_2',index_2)
]