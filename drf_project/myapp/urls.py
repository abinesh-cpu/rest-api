from django.urls import path
from . import views
urlpatterns=[
    path('stud',views.stud),
    path('<pk>',views.stud1.as_view()),
]