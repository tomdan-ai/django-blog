from django.http import HttpResponse

def homepage(request):
    return HttpResponse("Hello World!! It Pyblog time.")


def about(request):
    return HttpResponse("This is the about Page.")