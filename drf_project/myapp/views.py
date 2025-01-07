from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
from .serializers import *
from .models import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# from .models import *

# Create your views here.
# def stud(request):
#     if request.method=='GET':
#         data=student.objects.all()
#         s=studSerializer(data,many=True)
#         return JsonResponse(s.data,safe=False)

# @csrf_exempt
# def stud(request,pk):
#     try:
#         demo=student.objects.get(pk=pk)
#         print('helo')
#     except:
#         return JsonResponse("invalid")
#     if request.method=='GET':
#         s=studmodelserializer(demo)
#         return JsonResponse(s.data)
    # elif request.method=='POST':
    #     d=JSONParser().parse(request)
    #     s=studmodelserializer(data=d)
    #     if s.is_valid():
    #         s.save()
    #         return JsonResponse(s.data,safe=False)
    #     else:
    #         return JsonResponse(s.errors)
    # elif request.method=='PUT':
    #     d=JSONParser().parse(request)
    #     s=studmodelserializer(demo,data=d)
    #     if s.is_valid():
    #         s.save()
    #         return JsonResponse(s.data)
    #     else:
    #         return JsonResponse(s.errors)
    # elif request.method=='DELETE':
    #     demo.delete()
    #     return HttpResponse('deleted')
    
@api_view(['GET', 'POST'])

def stud(req):
    if req.method == 'GET':
        d = student.objects.all()
        s = studmodelserializer(d, many=True)
        return Response(s.data)
    elif req.method == 'POST':
        s = studmodelserializer (data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors, status=status.HTTP_400_BAD_REQUEST)