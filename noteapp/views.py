from django.http import HttpResponse


def helo(request):
    return HttpResponse('hello wolrd')