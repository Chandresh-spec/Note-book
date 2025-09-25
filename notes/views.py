from django.shortcuts import render

# Create your views here.


def check(request):
    return render (request,'index.html')