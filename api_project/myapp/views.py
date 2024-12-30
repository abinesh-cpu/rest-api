from django.shortcuts import render,redirect

# Create your views here.
def contact(request):
    return render(request,'contact.html')
def livecameras(request):
    return render(request,'livecameras.html')
def news(request):
    return render(request,'news.html')
def photos(request):
    return render(request,'photos.html')
def single(request):
    return render(request,'single.html')