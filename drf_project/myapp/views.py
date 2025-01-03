from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
# from .models import *

# Create your views here.
def stud(request):
    if request.method=='GET':
        data=student.objects.all()
        s=studSerializer(data,many=True)
        return JsonResponse(s.data,safe=False)