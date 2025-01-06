from django.shortcuts import render
from django.http import JsonResponse
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# from .models import *

# Create your views here.
# def stud(request):
#     if request.method=='GET':
#         data=student.objects.all()
#         s=studSerializer(data,many=True)
#         return JsonResponse(s.data,safe=False)

@csrf_exempt
def stud(request,pk):
    try:
        demo=student.objects.get(pk=pk)
        print('helo')
    except:
        return JsonResponse("invalid")
    if request.method=='GET':
        s=studmodelserializer(demo)
        return JsonResponse(s.data)
    # elif request.method=='POST':
    #     d=JSONParser().parse(request)
    #     s=studmodelserializer(data=d)
    #     if s.is_valid():
    #         s.save()
    #         return JsonResponse(s.data,safe=False)
    #     else:
    #         return JsonResponse(s.errors)