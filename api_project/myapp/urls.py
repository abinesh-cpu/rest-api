from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('contact',views.contact),
    path('livecameras',views.livecameras),
    path('news',views.news),
    path('photos',views.photos),
    path('single',views.single),
]