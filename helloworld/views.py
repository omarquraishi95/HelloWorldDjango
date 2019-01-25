from django.http import HttpResponse


#Return the Hello World Statement
def index(request):
    return HttpResponse("Hello World!")
