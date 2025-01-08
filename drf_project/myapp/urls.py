from django.urls import path
from . import views
urlpatterns=[
    path('',views.stud1.as_view()),
    # path('stud1',views.stud1)
]