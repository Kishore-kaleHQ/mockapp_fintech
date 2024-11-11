from django.http import HttpResponse # type: ignore

def hello_world(request):
    return HttpResponse("Hello, World!")